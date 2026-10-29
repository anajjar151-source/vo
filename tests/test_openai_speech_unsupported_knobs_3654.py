"""/v1/audio/speech vs engines without quality-knob flags (#3654).

The GGUF backend's bundled CLI accepts no num_step/guidance_scale, so an
explicit value there used to 200 with audio identical to the default call —
the #1014 class one layer down. The fix rejects at this boundary (where
"the caller asked" is still known — deeper layers can't tell an explicit
request from dubbing previews' hardcoded num_step=8) with a 400 naming the
parameter, instead of a 500 or silent default-quality audio. Engine-layer
permissiveness is pinned in tests/backend/engines/test_omnivoice_gguf.py.
"""
from __future__ import annotations

import pytest


def _tts_mod():
    import importlib

    return importlib.import_module("services.tts_backend")


@pytest.fixture()
def client():
    from fastapi.testclient import TestClient
    from main import app

    return TestClient(app, client=("127.0.0.1", 50000))


def _register(monkeypatch, engine_id, *, supports_knobs, seen):
    import torch

    tts = _tts_mod()

    class _FakeEngine(tts.TTSBackend):
        id = engine_id
        display_name = "Fake Engine (test)"
        supports_quality_knobs = supports_knobs

        @property
        def sample_rate(self) -> int:
            return 24000

        @property
        def supported_languages(self) -> list[str]:
            return ["multi"]

        @classmethod
        def is_available(cls):
            return True, "ready"

        def generate(self, text, **kw) -> torch.Tensor:
            seen.update(kw)
            return torch.zeros(1, 24000)

    monkeypatch.setitem(tts._REGISTRY, engine_id, _FakeEngine)


def test_speech_rejects_explicit_knobs_on_unsupported_engine(client, monkeypatch):
    """Explicit num_step/guidance_scale on an engine without those flags →
    400 naming the parameter (was 200 with silently default audio)."""
    seen: dict = {}
    _register(monkeypatch, "no-knobs-engine", supports_knobs=False, seen=seen)

    def _explode(*a, **kw):
        raise AssertionError("evict_other_tts_engines must not run for a doomed request")

    monkeypatch.setattr(
        "services.engine_memory.evict_other_tts_engines", _explode
    )

    res = client.post("/v1/audio/speech", json={
        "model": "no-knobs-engine", "input": "hello",
        "response_format": "wav", "num_step": 32,
    })
    assert res.status_code == 400, res.text
    assert "num_step" in res.json()["detail"]
    assert seen == {}, "rejected before any synthesis work"

    res = client.post("/v1/audio/speech", json={
        "model": "no-knobs-engine", "input": "hello",
        "response_format": "wav", "guidance_scale": 5.0,
    })
    assert res.status_code == 400, res.text
    assert "guidance_scale" in res.json()["detail"]


def test_speech_passes_knobs_to_supporting_engines(client, monkeypatch):
    """Default backends keep accepting (and forwarding) the knobs."""
    seen: dict = {}
    _register(monkeypatch, "knobs-engine", supports_knobs=True, seen=seen)

    res = client.post("/v1/audio/speech", json={
        "model": "knobs-engine", "input": "hello",
        "response_format": "wav", "num_step": 32,
    })
    assert res.status_code == 200, res.text
    assert seen.get("num_step") == 32


def test_speech_omits_knobs_cleanly_on_unsupported_engine(client, monkeypatch):
    """No knobs passed → the request flows to synthesis untouched."""
    seen: dict = {}
    _register(monkeypatch, "no-knobs-quiet", supports_knobs=False, seen=seen)

    res = client.post("/v1/audio/speech", json={
        "model": "no-knobs-quiet", "input": "hello",
        "response_format": "wav",
    })
    assert res.status_code == 200, res.text
