<p align="center">
  <img src="https://www.openminion.com/brand/openminion-logo.png" alt="Unicode Animatio logo" width="128" />
</p>

<h1 align="center">Unicode Animatio</h1>

<p align="center">
  <strong>Lightweight Unicode and ASCII terminal animation data for Python.</strong>
</p>

<p align="center">
  <a href="https://github.com/openminion/unicode-animatio">GitHub</a>
  · <a href="https://pypi.org/project/unicode-animatio/">PyPI</a>
  · <a href="https://www.openminion.com">Website</a>
  · <a href="docs/README.md">Docs</a>
  · <a href="https://x.com/OpenMinion">X</a>
</p>

<p align="center">
  <a href="https://pypi.org/project/unicode-animatio/"><img alt="PyPI" src="https://img.shields.io/pypi/v/unicode-animatio?cacheSeconds=300"></a>
  <a href="https://pypi.org/project/unicode-animatio/"><img alt="Python" src="https://img.shields.io/pypi/pyversions/unicode-animatio?cacheSeconds=300"></a>
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/license-MIT-blue"></a>
  <img alt="Status" src="https://img.shields.io/badge/status-beta-5B8DEF">
</p>

Unicode Animatio `v0.0.3` packages deterministic animation frames and timing
for terminals and other text renderers. It has no runtime dependencies and
does not take ownership of colors, labels, layout, progress, or task state.

The distribution and CLI name is `unicode-animatio`. The Python import root is
`unicode_animations`.

## Read This First

1. Read [At a Glance](#at-a-glance) for the package naming and renderer
   boundary.
2. Follow [Install](#install) and [Quick Start](#quick-start) to read animation
   frames from Python.
3. Use [Choosing a Preset](#choosing-a-preset) to select a category.
4. Use the terminal or browser preview commands before integrating a renderer.
5. Read [Development](#development) before changing the package.

## Trust and Brand Safety

- Official GitHub: <https://github.com/openminion/unicode-animatio>
- Official website: <https://www.openminion.com>
- Official X account: <https://x.com/OpenMinion>

Unicode Animatio has no official token, coin, NFT, airdrop, staking program,
treasury product, or investment offering. Any claim otherwise is unauthorized
and should be treated as a scam.

## At a Glance

| | |
| --- | --- |
| Distribution | `unicode-animatio` |
| Import root | `unicode_animations` |
| Current line | `v0.0.3` beta |
| Python | 3.9+ |
| Catalog | 58 animations across 10 categories |
| Runtime dependencies | None |
| Not the claim | Progress tracking, task orchestration, or framework rendering |

## Common Commands

```bash
python3 -m pip install unicode-animatio
unicode-animatio --list
unicode-animatio --categories
unicode-animatio helix
unicode-animatio-web --port 8765
```

## Install

Install from PyPI:

```bash
python3 -m pip install unicode-animatio
```

For a source checkout:

```bash
python3 -m pip install -e ".[dev]"
```

## Quick Start

Read raw frames and timing:

```python
from unicode_animations import spinners

spinner = spinners["braille"]
print(spinner.frames)
print(spinner.interval)
```

Use the provider boundary when the consumer should not depend on the catalog
implementation:

```python
from unicode_animations import get_provider

provider = get_provider()
animation = provider.get("helix")

print(provider.provider_id)
print(animation.frames)
print(animation.interval_ms)
```

Preview the catalog in a terminal:

```bash
unicode-animatio --list --category graph
unicode-animatio edgepulse
```

Preview it in a local browser:

```bash
unicode-animatio --web
```

## What Unicode Animatio Provides

- immutable animation frame data and millisecond timing
- canonical animation names, categories, and category lookup
- braille-grid helpers: `make_grid` and `grid_to_braille`
- compatibility aliases: `makeGrid` and `gridToBraille`
- a structural provider entry point for host applications
- a terminal preview CLI: `unicode-animatio`
- a local browser preview CLI: `unicode-animatio-web`
- a PEP 561 type marker and typed public API

## What Unicode Animatio Does Not Provide

- terminal UI or async rendering frameworks
- progress bars, task orchestration, or job-state tracking
- renderer colors, backgrounds, labels, or layout
- automatic reduced-motion or accessibility policy
- hosted demos or remote APIs
- framework-specific Rich, Textual, or Typer adapters

The host renderer owns presentation and accessibility. The package returns raw
frames and timing only.

## Available animations

The catalog currently contains 58 deterministic animations:

| Category | Presets |
| --- | --- |
| `subtle` | `braille`, `pulse`, `orbit`, `breathe`, `softdot`, `slowbreath`, `quietorbit`, `dimwave` |
| `scan` | `scan`, `scanline`, `snake`, `diagswipe`, `hscan`, `vscan`, `radar`, `focusbeam` |
| `build` | `blocks`, `stack`, `assemble`, `brickline` |
| `thinking` | `ellipsis`, `mindwave`, `synapse`, `neuron` |
| `tool` | `terminalblink`, `gearspin`, `wrench`, `sparkplug` |
| `data` | `braillewave`, `dna`, `rain`, `cascade`, `columns`, `waverows`, `helix`, `bitstream`, `packetflow`, `matrixrain`, `columns2` |
| `graph` | `nodes`, `edgepulse`, `cluster`, `orbitnodes` |
| `progress` | `fillsweep`, `meter`, `ladder`, `risingblocks`, `fillbar2` |
| `alert` | `sparkle`, `warningpulse`, `heartbeat`, `ping`, `flashdot` |
| `dense` | `checkerboard`, `plasma`, `noise`, `moire`, `shimmergrid` |

## Choosing a Preset

| Category | Good fit |
| --- | --- |
| `subtle` | Calm background activity |
| `scan` | Indexing, searching, or retrieval |
| `build` | Assembly and compilation |
| `thinking` | Model or reasoning activity |
| `tool` | Command and tool execution |
| `data` | Streaming and data movement |
| `graph` | Relation traversal and knowledge graphs |
| `progress` | Steady forward motion |
| `alert` | Short attention states |
| `dense` | High-energy or diagnostic displays |

Inspect exact names and timing rather than selecting from memory:

```bash
unicode-animatio --categories
unicode-animatio --list --category data
unicode-animatio packetflow
```

## Development

```bash
make dev-install
make hooks-install
make check
```

Use `make release-check` before publishing or changing the documented public
surface.

## Docs and Release

- [`docs/README.md`](docs/README.md): package documentation map
- [`docs/getting-started.md`](docs/getting-started.md): package usage and
  contributor bootstrap
- [`docs/source-tree-owner-map.md`](docs/source-tree-owner-map.md): code owners
  and package layout
- [`API_COMPATIBILITY.md`](API_COMPATIBILITY.md): public names and provider
  contract
- [`RELEASING.md`](RELEASING.md): release and publish flow

Questions and bug reports belong in
[GitHub Issues](https://github.com/openminion/unicode-animatio/issues).

## License and Brand-use Boundary

- Source code license: MIT
- Brand/trademark grant: none

The license grants rights to use, modify, and redistribute the code. It does
not grant rights to present a fork, clone, token, website, or social account as
the official Unicode Animatio or OpenMinion project or imply affiliation or
endorsement.
