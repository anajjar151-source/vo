<div align="center">
  <img src="../../docs/logo.png" alt="VoiceStudio" width="88" />
  <h1>VoiceStudio</h1>
  <p>
    <a href="https://trendshift.io/repositories/28176?utm_source=repository-badge&amp;utm_medium=badge&amp;utm_campaign=badge-repository-28176" target="_blank" rel="noopener noreferrer"><img src="https://trendshift.io/api/badge/repositories/28176" alt="Trendshift における VoiceStudio の人気ランキングバッジ" width="220" height="48" /></a>
  </p>
  <p><strong>ローカルで動くボイススタジオ。646 言語で、音声クローン、ボイスデザイン、吹き替え、音声入力、文字起こし、ナレーション。</strong><br />
  お使いのパソコンとスマートフォンで動作します。アカウントも API キーも不要。あなたが許可しない限り、データが端末の外に出ることはありません。</p>
  <p>
    <a href="https://voicestudio.sh/?utm_source=github&utm_medium=readme&utm_campaign=project">公式サイト</a> ·
    <a href="https://github.com/debpalash/VoiceStudio/releases/latest">ダウンロード</a> ·
    <a href="#はじめに">導入ガイド</a> ·
    <a href="#ドキュメント">ドキュメント</a> ·
    <a href="https://discord.gg/bzQavDfVV9">Discord</a> ·
    <a href="../../README.md">English</a> ·
    <a href="README_CN.md">简体中文</a> ·
    <a href="README_KO.md">한국어</a> ·
    <a href="README_RU.md">Русский</a>
  </p>
  <p>
    <a href="https://github.com/debpalash/VoiceStudio/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/debpalash/VoiceStudio/ci.yml?branch=main" alt="CI ステータス" /></a>
    <a href="https://github.com/debpalash/VoiceStudio/releases/latest"><img src="https://img.shields.io/github/v/release/debpalash/VoiceStudio" alt="最新リリース" /></a>
    <a href="../../LICENSE"><img src="https://img.shields.io/badge/license-AGPL--3.0-blue" alt="AGPL-3.0 ライセンス" /></a>
    <a href="https://supermetry.com"><img src="https://app.supermetry.com/px/zfjiv7psp4ed.svg?c=VoiceStudio&style=stats" alt="閲覧数" /></a>
  </p>
  <p>
    <sub>戦略スポンサー</sub><br />
    <a href="https://supermetry.com/?utm_source=voicestudio&utm_medium=sponsor&utm_campaign=strategic-sponsor&utm_content=readme-logo"><picture><source media="(prefers-color-scheme: dark)" srcset="../../docs/sponsors/supermetry-dark.svg" /><img src="../../docs/sponsors/supermetry.svg" alt="Supermetry" height="48" /></picture></a>
  </p>
</div>

![アプリのツアー：音声クローン、ボイスデザイン、吹き替え、モデル管理](../../docs/media/electron/voicestudio.gif)

## できること

| つくる | 仕上げる | つなぐ |
| :--- | :--- | :--- |
| 声をクローン、または独自にデザイン | タイミングを合わせた音声で動画を吹き替え | エージェント向けのローカル API と MCP |
| フローティングウィジェットで音声入力 | ストーリー、オーディオブック、バッチ処理 | 再利用できるレシピと監視フォルダー |

まずはデフォルトの **VoiceStudio**（k2-fsa/OmniVoice ベース）から。モデルマネージャーでは、ほかにも数十のエンジンから選べます。[機能とエンジンの一覧](../../docs/feature-catalog.md)を参照してください。

<details>
<summary><strong>スクリーンショット</strong></summary>

<table>
  <tr>
    <td><img src="../../docs/media/electron/voice-cloning.png" alt="同梱のデモ音声を使った音声クローンワークスペース" width="100%" /></td>
    <td><img src="../../docs/media/electron/dubbing.png" alt="動画吹き替えワークスペース" width="100%" /></td>
  </tr>
  <tr><td align="center">音声クローン</td><td align="center">動画吹き替え</td></tr>
  <tr>
    <td><img src="../../docs/media/electron/voice-design.png" alt="ボイスデザインワークスペースで声を説明する" width="100%" /></td>
    <td><img src="../../docs/media/electron/models.png" alt="ローカル音声モデルのインストールと管理" width="100%" /></td>
  </tr>
  <tr><td align="center">ボイスデザイン</td><td align="center">ローカルモデル</td></tr>
</table>

</details>

## 対応プラットフォーム

| プラットフォーム | ダウンロード | アクセラレーション | ステータス |
| :--- | :--- | :--- | :--- |
| **macOS**（Apple Silicon） | `.dmg` · [ガイド](../../docs/install/macos.md) | Metal（MPS） | 安定版 |
| **Windows 10/11**（x64） | `.exe` · [ガイド](../../docs/install/windows.md) | NVIDIA CUDA · [AMD ROCm（オプトイン）](../../docs/install/windows-rocm.md) · CPU | 安定版 |
| **Linux**（x64） | `.AppImage` · `.deb` · `snap` · [Nix](../../docs/install/nix.md) · [ガイド](../../docs/install/linux.md) | NVIDIA CUDA · CPU | 安定版 |
| **Docker** | [`ghcr.io/debpalash/voicestudio`](../../docs/install/docker.md) | NVIDIA CUDA · AMD ROCm | 安定版 |
| **Android** 10+ | `.apk` · [ガイド](../../docs/mobile.md#install) | 端末上で動作、オフライン対応 | プレビュー |
| **iPhone / iPad**（iOS 17+） | `.ipa`（サイドロード） · [ガイド](../../docs/mobile.md#install) | 端末上で動作、オフライン対応 | プレビュー |
| **Windows on ARM** | `.exe` · [ガイド](../../docs/install/windows.md) | CPU（x64 バックエンドをエミュレーションで実行） | 実験的 |
| **Intel Mac** | `.dmg` · [理由](../../docs/install/macos.md) | アプリ UI のみ。リモートバックエンドに接続 | 限定 |

デスクトップ版とスマートフォン版のインストーラーは[最新リリース](https://github.com/debpalash/VoiceStudio/releases/latest)から入手できます。Docker イメージは GHCR で配布しています。GPU がなくても、CPU ですべての機能を使えます（速度は落ちます）。オプトインのネイティブ GGUF エンジンは、AMD GPU を含め Vulkan も利用できます（[OmniVoice](../../docs/engines/omnivoice-gguf.md#vulkan-acceleration)、[CosyVoice](../../docs/engines/cosyvoice-gguf.md)）。エンジンとハードウェアごとの速度は[パフォーマンス](../../docs/performance.md)を参照してください。

## はじめに

**macOS / Linux**

```sh
curl -fsSL https://voicestudio.sh/install | sh
```

**Windows**（PowerShell）

```powershell
irm https://voicestudio.sh/install.ps1 | iex
```

上の表からインストーラーをダウンロードしても構いません。インストールしたら**音声クローン**を開き、声を選ぶかクリアな参照音声を追加して、テキストを入力し生成します。モデルをダウンロードする前には、必ず確認が表示されます。

> [!NOTE]
> macOS で「VoiceStudio は壊れているため開けません」と表示されるのは、Gatekeeper がアプリをブロックしているためで、ダウンロードが壊れているわけではありません。[Gatekeeper の対処法](../../docs/install/macos.md#gatekeeper-quarantine)を参照してください。

<details>
<summary><strong>その他のインストール方法</strong>：特定のバージョン、最新の main、アンインストール、ソースから、コーディングエージェントで</summary>

```sh
curl -fsSL https://voicestudio.sh/install | sh -s -- --version X.Y.Z   # 特定のリリース
curl -fsSL https://voicestudio.sh/install | sh -s -- --main            # 最新の main をビルド
curl -fsSL https://voicestudio.sh/install | sh -s -- --uninstall       # データを残してアプリを削除
```

`voicestudio.sh` にアクセスできない場合は、リポジトリから直接スクリプトを実行できます：
`curl -fsSL https://raw.githubusercontent.com/debpalash/VoiceStudio/main/scripts/install.sh | sh`。
前提条件と動作：[インストーラーガイド](../../docs/install/script.md)。

**ソースから**

```bash
git clone https://github.com/debpalash/VoiceStudio.git
cd VoiceStudio
bun run dev
```

[Electron のセットアップ](../../electron/README.md)を参照してください。

**コーディングエージェントで**（Claude Code、Codex、Cursor など）、次の内容を貼り付けます：

```text
Install the VoiceStudio app on this device and verify it works, following
https://github.com/debpalash/VoiceStudio/blob/main/docs/install/agent.md
```

0.5.3 以前（Tauri 版アプリ）からアップグレードする場合は、[新しいアプリを別途インストール](../../docs/electron-migration.md)してください。

</details>

## ドキュメント

| 目的 | 参照先 |
|---|---|
| セットアップのヘルプ | [トラブルシューティング](../../docs/install/troubleshooting.md) · [モデルのダウンロード](../../docs/downloading-models.md) |
| ガイド | [複数話者の吹き替え](../../docs/dubbing/multi-speaker-guide.md) · [表現豊かな音声](../../docs/expressive-speech.md) · [吹き替えの書き出し](../../docs/dubbing/export.md) |
| モデルと音質 | [エンジンガイド](../../docs/engines/README.md) · [whisper.cpp ASR](../../docs/engines/whisper-cpp.md) · [ベンチマーク](../../docs/benchmarks.md) |
| 連携 | [ローカル API](../../docs/speech-platform.md) · [MCP](../../docs/mcp.md) · [サンプル](../../examples/README.md) |
| スマートフォンアプリ | [iOS と Android](../../docs/mobile.md) |
| 開発 | [コントリビューション](../../.github/CONTRIBUTING.md)（初めての PR の前に [CLA への署名](../../.github/CONTRIBUTING.md#contribution-licensing)が必要です）· [変更履歴](../../CHANGELOG.md) |

エージェントスキル：`npx skills add debpalash/VoiceStudio`（音声作業には **voicestudio**、リポジトリのメンテナンスには **voicestudio-maintainer**）。

## スポンサー

VoiceStudio は無料で、背後に有料クラウドはありません。開発を続けられるのはスポンサーのおかげです。スポンサー資金はメンテナーの作業時間、テスト用ハードウェア、コード署名、リリース基盤に充てられます。

<p>
    <a href="https://supermetry.com/?utm_source=voicestudio&utm_medium=sponsor&utm_campaign=strategic-sponsor&utm_content=readme-logo"><picture><source media="(prefers-color-scheme: dark)" srcset="../../docs/sponsors/supermetry-dark.svg" /><img src="../../docs/sponsors/supermetry.svg" alt="Supermetry" height="48" /></picture></a>
</p>

**ここにあなたのロゴを。** Development・Company・Strategic スポンサー枠を月額 100 ドルから募集中です。Community スポンサー（25 ドル）は名前入りのリンクを掲載します。スポンサーシップで得られるのは謝辞の掲載であり、機能ではありません。

<a href="https://github.com/sponsors/debpalash"><img src="https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-ea4aaa?logo=githubsponsors&logoColor=white" alt="GitHub Sponsors でスポンサーになる" /></a>
[Ko-fi](https://ko-fi.com/debpalash) · [PayPal](https://paypal.me/palashCoder) · [プランと特典](../../SPONSORS.md) · [ロゴの掲載を申し込む](https://github.com/debpalash/VoiceStudio/issues/new?template=sponsor.yml)

## チーム

### コアチーム

<table>
<tr>
<td align="center" width="200"><a href="https://github.com/debpalash"><img src="https://github.com/debpalash.png?size=160" width="80" height="80" alt="Palash Debnath"></a><br><b>Palash Debnath</b><br><sub>作者・コアチーム</sub><br><sub><a href="https://palash.dev">palash.dev</a> · <a href="https://github.com/debpalash">GitHub</a> · <a href="https://x.com/idebpalash">X</a></sub></td>
<td align="center" width="200"><a href="https://github.com/velixio"><img src="https://github.com/velixio.png?size=160" width="80" height="80" alt="Shimul Debnath"></a><br><b>Shimul Debnath</b><br><sub>コアチーム</sub><br><sub><a href="https://shimul.me">shimul.me</a> · <a href="https://github.com/velixio">GitHub</a> · <a href="https://x.com/shimuldn">X</a></sub></td>
</tr>
</table>

### コントリビューター

<a href="https://github.com/kevin9327"><img src="https://github.com/kevin9327.png?size=96" width="44" height="44" alt="@kevin9327" title="@kevin9327"></a> <a href="https://github.com/jaketame"><img src="https://github.com/jaketame.png?size=96" width="44" height="44" alt="@jaketame" title="@jaketame"></a> <a href="https://github.com/psiberfunk"><img src="https://github.com/psiberfunk.png?size=96" width="44" height="44" alt="@psiberfunk" title="@psiberfunk"></a> <a href="https://github.com/rudycelekli"><img src="https://github.com/rudycelekli.png?size=96" width="44" height="44" alt="@rudycelekli" title="@rudycelekli"></a> <a href="https://github.com/paoloantinori"><img src="https://github.com/paoloantinori.png?size=96" width="44" height="44" alt="@paoloantinori" title="@paoloantinori"></a> <a href="https://github.com/Chang-Jin-Lee"><img src="https://github.com/Chang-Jin-Lee.png?size=96" width="44" height="44" alt="@Chang-Jin-Lee" title="@Chang-Jin-Lee"></a> <a href="https://github.com/swadhinbiswas"><img src="https://github.com/swadhinbiswas.png?size=96" width="44" height="44" alt="@swadhinbiswas" title="@swadhinbiswas"></a> <a href="https://github.com/BichengWang"><img src="https://github.com/BichengWang.png?size=96" width="44" height="44" alt="@BichengWang" title="@BichengWang"></a> <a href="https://github.com/nirmalchatur"><img src="https://github.com/nirmalchatur.png?size=96" width="44" height="44" alt="@nirmalchatur" title="@nirmalchatur"></a> <a href="https://github.com/Shivendra-Coherent"><img src="https://github.com/Shivendra-Coherent.png?size=96" width="44" height="44" alt="@Shivendra-Coherent" title="@Shivendra-Coherent"></a> <a href="https://github.com/marreiradigital"><img src="https://github.com/marreiradigital.png?size=96" width="44" height="44" alt="@marreiradigital" title="@marreiradigital"></a> <a href="https://github.com/nvtoan0201-swe"><img src="https://github.com/nvtoan0201-swe.png?size=96" width="44" height="44" alt="@nvtoan0201-swe" title="@nvtoan0201-swe"></a>

コード、報告、翻訳、アイデアを寄せてくださったすべての方に感謝します。[すべてのコントリビューター](https://github.com/debpalash/VoiceStudio/graphs/contributors) · [コントリビュート](../../.github/CONTRIBUTING.md)

## ライセンスと責任ある利用

アプリには [AGPL-3.0](../../LICENSE) が適用され、その条件のもとで商用利用もできます。モデルの重み、音声、生成物にはそれぞれ独自のライセンスがあり、モデルマネージャーでモデルごとに確認できます（[一覧](../../docs/licensing/model-inventory.md)）。声のクローンは、必ずその声の持ち主の許可を得てから行ってください。詳細：[LICENSE-NOTICE.md](../../LICENSE-NOTICE.md)。
