<div align="center">
  <img src="../../docs/logo.png" alt="VoiceStudio" width="88" />
  <h1>VoiceStudio</h1>
  <p>
    <a href="https://trendshift.io/repositories/28176?utm_source=repository-badge&amp;utm_medium=badge&amp;utm_campaign=badge-repository-28176" target="_blank" rel="noopener noreferrer"><img src="https://trendshift.io/api/badge/repositories/28176" alt="Значок рейтинга популярности VoiceStudio на Trendshift" width="220" height="48" /></a>
  </p>
  <p><strong>Локальная голосовая студия: клонирование и создание голосов, дубляж, диктовка, расшифровка и озвучка на 646 языках.</strong><br />
  Работает на вашем компьютере и телефоне. Без аккаунтов и API-ключей; без вашего согласия ничего не покидает устройство.</p>
  <p>
    <a href="https://voicestudio.sh/?utm_source=github&utm_medium=readme&utm_campaign=project">Сайт</a> ·
    <a href="https://github.com/debpalash/VoiceStudio/releases/latest">Скачать</a> ·
    <a href="#быстрый-старт">Начало работы</a> ·
    <a href="#справка">Документация</a> ·
    <a href="https://discord.gg/bzQavDfVV9">Discord</a> ·
    <a href="../../README.md">English</a> ·
    <a href="README_CN.md">简体中文</a> ·
    <a href="README_JA.md">日本語</a> ·
    <a href="README_KO.md">한국어</a>
  </p>
  <p>
    <a href="https://github.com/debpalash/VoiceStudio/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/debpalash/VoiceStudio/ci.yml?branch=main" alt="Статус CI" /></a>
    <a href="https://github.com/debpalash/VoiceStudio/releases/latest"><img src="https://img.shields.io/github/v/release/debpalash/VoiceStudio" alt="Последний релиз" /></a>
    <a href="../../LICENSE"><img src="https://img.shields.io/badge/license-AGPL--3.0-blue" alt="Лицензия AGPL-3.0" /></a>
    <a href="https://supermetry.com"><img src="https://app.supermetry.com/px/zfjiv7psp4ed.svg?c=VoiceStudio&style=stats" alt="Число просмотров" /></a>
  </p>
  <p>
    <sub>Стратегический спонсор</sub><br />
    <a href="https://supermetry.com/?utm_source=voicestudio&utm_medium=sponsor&utm_campaign=strategic-sponsor&utm_content=readme-logo"><picture><source media="(prefers-color-scheme: dark)" srcset="../../docs/sponsors/supermetry-dark.svg" /><img src="../../docs/sponsors/supermetry.svg" alt="Supermetry" height="48" /></picture></a>
  </p>
</div>

![Обзор приложения: клонирование голоса, создание голоса, дубляж и управление моделями](../../docs/media/electron/voicestudio.gif)

## Возможности

| Творите | Публикуйте | Интегрируйте |
| :--- | :--- | :--- |
| Копия любого голоса или голос по описанию | Перевод и озвучка роликов с точной синхронизацией | API и MCP-сервер для ИИ-агентов прямо на вашей машине |
| Голосовой ввод из компактного окна поверх приложений | Рассказы, аудиокниги и обработка файлов пачками | Сохранённые сценарии и автообработка новых файлов в папке |

Из коробки работает **VoiceStudio** — штатный движок, построенный на k2-fsa/OmniVoice; ещё несколько десятков альтернатив ставятся из менеджера моделей. Полный список — в [каталоге функций и движков](../../docs/feature-catalog.md).

<details>
<summary><strong>Скриншоты</strong></summary>

<table>
  <tr>
    <td><img src="../../docs/media/electron/voice-cloning.png" alt="Рабочее пространство клонирования голоса со встроенным демонстрационным голосом" width="100%" /></td>
    <td><img src="../../docs/media/electron/dubbing.png" alt="Экран дубляжа в приложении Electron" width="100%" /></td>
  </tr>
  <tr><td align="center">Клонирование голоса</td><td align="center">Дубляж</td></tr>
  <tr>
    <td><img src="../../docs/media/electron/voice-design.png" alt="Голос задаётся текстовым описанием на экране голосового дизайна" width="100%" /></td>
    <td><img src="../../docs/media/electron/models.png" alt="Скачивание, обновление и удаление речевых моделей на компьютере" width="100%" /></td>
  </tr>
  <tr><td align="center">Голосовой дизайн</td><td align="center">Модели</td></tr>
</table>

</details>

## Платформы

| Платформа | Файл | Аппаратное ускорение | Статус |
| :--- | :--- | :--- | :--- |
| **macOS** (Apple Silicon) | `.dmg` · [руководство](../../docs/install/macos.md) | Metal (MPS) | Стабильная |
| **Windows 10/11** (x64) | `.exe` · [руководство](../../docs/install/windows.md) | NVIDIA CUDA · [AMD ROCm (по желанию)](../../docs/install/windows-rocm.md) · CPU | Стабильная |
| **Linux** (x64) | `.AppImage` · `.deb` · `snap` · [Nix](../../docs/install/nix.md) · [руководство](../../docs/install/linux.md) | NVIDIA CUDA · CPU | Стабильная |
| **Docker** | [`ghcr.io/debpalash/voicestudio`](../../docs/install/docker.md) | NVIDIA CUDA · AMD ROCm | Стабильная |
| **Android** 10+ | `.apk` · [руководство](../../docs/mobile.md#install) | На устройстве, офлайн | Предварительная |
| **iPhone / iPad** (iOS 17+) | `.ipa` (sideload) · [руководство](../../docs/mobile.md#install) | На устройстве, офлайн | Предварительная |
| **Windows ARM64** | `.exe` · [руководство](../../docs/install/windows.md) | CPU (x64-бэкенд работает через эмуляцию) | Экспериментальная |
| **Intel Mac** | `.dmg` · [причины](../../docs/install/macos.md) | Только интерфейс, подключение к удалённому бэкенду | Ограниченная |

Установщики для компьютера и телефона лежат в [последнем релизе](https://github.com/debpalash/VoiceStudio/releases/latest), а образы Docker публикуются в GHCR. Нет видеокарты? Приложение полностью работает на процессоре, просто медленнее. Необязательные нативные GGUF-движки могут использовать Vulkan, в том числе на видеокартах AMD ([OmniVoice](../../docs/engines/omnivoice-gguf.md#vulkan-acceleration), [CosyVoice](../../docs/engines/cosyvoice-gguf.md)). Сколько занимает генерация на разных движках и железе, показано в [обзоре быстродействия](../../docs/performance.md).

## Быстрый старт

**macOS / Linux**

```sh
curl -fsSL https://voicestudio.sh/install | sh
```

**Windows** (PowerShell)

```powershell
irm https://voicestudio.sh/install.ps1 | iex
```

Или скачайте установщик из таблицы выше. Затем откройте **Клонирование голоса**, выберите голос или добавьте чистую эталонную запись, введите текст и запустите генерацию. Перед загрузкой любой модели приложение спросит разрешения.

> [!NOTE]
> Сообщение macOS «Программа VoiceStudio повреждена, и её не удаётся открыть» означает, что приложение заблокировал Gatekeeper, а не что загрузка повреждена. [Как снять блокировку](../../docs/install/macos.md#gatekeeper-quarantine).

<details>
<summary><strong>Другие способы установки</strong>: конкретная версия, текущий main, удаление, из исходного кода, с помощью агента</summary>

```sh
curl -fsSL https://voicestudio.sh/install | sh -s -- --version X.Y.Z   # конкретный релиз
curl -fsSL https://voicestudio.sh/install | sh -s -- --main            # собрать текущий main
curl -fsSL https://voicestudio.sh/install | sh -s -- --uninstall       # удалить приложение, сохранив данные
```

Если `voicestudio.sh` недоступен, запустите скрипт прямо из репозитория:
`curl -fsSL https://raw.githubusercontent.com/debpalash/VoiceStudio/main/scripts/install.sh | sh`.
Требования и поведение: [руководство по установщику](../../docs/install/script.md).

**Из исходного кода**

```bash
git clone https://github.com/debpalash/VoiceStudio.git
cd VoiceStudio
bun run dev
```

Зависимости и настройка бэкенда описаны в [инструкции к Electron](../../electron/README.md).

**Через ИИ-агента** (например, Claude Code, Codex или Cursor) — передайте ему такой запрос:

```text
Install the VoiceStudio app on this device and verify it works, following
https://github.com/debpalash/VoiceStudio/blob/main/docs/install/agent.md
```

Обновляетесь с версии 0.5.3 или более ранней (приложение на Tauri)? [Установите новое приложение отдельно](../../docs/electron-migration.md).

</details>

## Справка

| Задача | Куда смотреть |
|---|---|
| Проблемы при установке | [Решение проблем](../../docs/install/troubleshooting.md) · [Скачивание моделей](../../docs/downloading-models.md) |
| Пошаговые инструкции | [Дубляж с несколькими дикторами](../../docs/dubbing/multi-speaker-guide.md) · [Выразительная речь](../../docs/expressive-speech.md) · [Экспорт дубляжа](../../docs/dubbing/export.md) |
| Движки и качество | [Обзор движков](../../docs/engines/README.md) · [whisper.cpp ASR](../../docs/engines/whisper-cpp.md) · [Бенчмарки](../../docs/benchmarks.md) |
| Связка с другими инструментами | [API речевой платформы](../../docs/speech-platform.md) · [MCP](../../docs/mcp.md) · [Образцы кода](../../examples/README.md) |
| Мобильные приложения | [Android и iOS](../../docs/mobile.md) |
| Для разработчиков | [Правила для контрибьюторов](../../.github/CONTRIBUTING.md) ([подпишите CLA](../../.github/CONTRIBUTING.md#contribution-licensing) перед первым PR) · [История версий](../../CHANGELOG.md) |

Скиллы для ИИ-агентов ставятся командой `npx skills add debpalash/VoiceStudio`: **voicestudio** — для аудиозадач, **voicestudio-maintainer** — для поддержки самого репозитория.

## Поддержка проекта

VoiceStudio бесплатен, и за ним нет платного облака. Новые версии выходят благодаря спонсорам: они оплачивают время мейнтейнера, оборудование для тестов, подпись кода и инфраструктуру релизов.

<p>
    <a href="https://supermetry.com/?utm_source=voicestudio&utm_medium=sponsor&utm_campaign=strategic-sponsor&utm_content=readme-logo"><picture><source media="(prefers-color-scheme: dark)" srcset="../../docs/sponsors/supermetry-dark.svg" /><img src="../../docs/sponsors/supermetry.svg" alt="Supermetry" height="48" /></picture></a>
</p>

**Здесь может быть ваш логотип.** Места спонсоров уровней Development, Company и Strategic открыты — от 100 $ в месяц; спонсоры уровня Community (25 $) получают именную ссылку. Спонсорство даёт признание, а не функции.

<a href="https://github.com/sponsors/debpalash"><img src="https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-ea4aaa?logo=githubsponsors&logoColor=white" alt="Поддержать через GitHub Sponsors" /></a>
[Ko-fi](https://ko-fi.com/debpalash) · [PayPal](https://paypal.me/palashCoder) · [Уровни и привилегии](../../SPONSORS.md) · [Разместить логотип](https://github.com/debpalash/VoiceStudio/issues/new?template=sponsor.yml)

## Команда проекта

### Основная команда

<table>
<tr>
<td align="center" width="200"><a href="https://github.com/debpalash"><img src="https://github.com/debpalash.png?size=160" width="80" height="80" alt="Palash Debnath"></a><br><b>Palash Debnath</b><br><sub>Автор проекта, основная команда</sub><br><sub><a href="https://palash.dev">palash.dev</a> · <a href="https://github.com/debpalash">GitHub</a> · <a href="https://x.com/idebpalash">X</a></sub></td>
<td align="center" width="200"><a href="https://github.com/velixio"><img src="https://github.com/velixio.png?size=160" width="80" height="80" alt="Shimul Debnath"></a><br><b>Shimul Debnath</b><br><sub>Основная команда</sub><br><sub><a href="https://shimul.me">shimul.me</a> · <a href="https://github.com/velixio">GitHub</a> · <a href="https://x.com/shimuldn">X</a></sub></td>
</tr>
</table>

### Участники

<a href="https://github.com/kevin9327"><img src="https://github.com/kevin9327.png?size=96" width="44" height="44" alt="@kevin9327" title="@kevin9327"></a> <a href="https://github.com/jaketame"><img src="https://github.com/jaketame.png?size=96" width="44" height="44" alt="@jaketame" title="@jaketame"></a> <a href="https://github.com/psiberfunk"><img src="https://github.com/psiberfunk.png?size=96" width="44" height="44" alt="@psiberfunk" title="@psiberfunk"></a> <a href="https://github.com/rudycelekli"><img src="https://github.com/rudycelekli.png?size=96" width="44" height="44" alt="@rudycelekli" title="@rudycelekli"></a> <a href="https://github.com/paoloantinori"><img src="https://github.com/paoloantinori.png?size=96" width="44" height="44" alt="@paoloantinori" title="@paoloantinori"></a> <a href="https://github.com/Chang-Jin-Lee"><img src="https://github.com/Chang-Jin-Lee.png?size=96" width="44" height="44" alt="@Chang-Jin-Lee" title="@Chang-Jin-Lee"></a> <a href="https://github.com/swadhinbiswas"><img src="https://github.com/swadhinbiswas.png?size=96" width="44" height="44" alt="@swadhinbiswas" title="@swadhinbiswas"></a> <a href="https://github.com/BichengWang"><img src="https://github.com/BichengWang.png?size=96" width="44" height="44" alt="@BichengWang" title="@BichengWang"></a> <a href="https://github.com/nirmalchatur"><img src="https://github.com/nirmalchatur.png?size=96" width="44" height="44" alt="@nirmalchatur" title="@nirmalchatur"></a> <a href="https://github.com/Shivendra-Coherent"><img src="https://github.com/Shivendra-Coherent.png?size=96" width="44" height="44" alt="@Shivendra-Coherent" title="@Shivendra-Coherent"></a> <a href="https://github.com/marreiradigital"><img src="https://github.com/marreiradigital.png?size=96" width="44" height="44" alt="@marreiradigital" title="@marreiradigital"></a> <a href="https://github.com/nvtoan0201-swe"><img src="https://github.com/nvtoan0201-swe.png?size=96" width="44" height="44" alt="@nvtoan0201-swe" title="@nvtoan0201-swe"></a>

Спасибо всем, кто присылает код, сообщения об ошибках, переводы и идеи. [Все участники](https://github.com/debpalash/VoiceStudio/graphs/contributors) · [Как помочь проекту](../../.github/CONTRIBUTING.md)

## Лицензия и этичное использование

На приложение распространяется лицензия [AGPL-3.0](../../LICENSE), в том числе на коммерческое использование на её условиях. У весов моделей, голосов и сгенерированного результата свои лицензии; менеджер моделей показывает их для каждой модели ([полный перечень](../../docs/licensing/model-inventory.md)). Клонируйте голос только с разрешения его владельца. Подробности: [LICENSE-NOTICE.md](../../LICENSE-NOTICE.md).
