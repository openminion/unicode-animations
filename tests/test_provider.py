from __future__ import annotations

import pytest

from unicode_animations import SPINNER_NAMES, get_provider, metadata_for_spinner, spinners
from unicode_animations.provider import AnimationSpec, UnicodeAnimationProvider


def test_get_provider_returns_structural_provider_without_openminion_import() -> None:
    provider = get_provider()

    assert isinstance(provider, UnicodeAnimationProvider)
    assert provider.provider_id == "unicode"
    assert provider.names() == tuple(SPINNER_NAMES)


@pytest.mark.parametrize("name", SPINNER_NAMES)
def test_provider_specs_match_spinner_catalog(name: str) -> None:
    provider = get_provider()
    spec = provider.get(name)
    metadata = metadata_for_spinner(name)

    assert spec == AnimationSpec(
        provider_id="unicode",
        name=name,
        frames=tuple(spinners[name].frames),
        interval_ms=spinners[name].interval,
        category=metadata.category,
        tags=metadata.tags,
        frame_count=metadata.frame_count,
        frame_width=metadata.frame_width,
        motion=metadata.motion,
        description=metadata.description,
    )


def test_provider_exposes_catalog_metadata_and_search() -> None:
    provider = get_provider()
    catalog = provider.catalog()

    assert len(catalog) == len(SPINNER_NAMES)
    assert catalog[0] == metadata_for_spinner(SPINNER_NAMES[0])
    assert provider.describe("edgepulse").category == "graph"
    assert provider.names(category="graph", search="edgepulse") == ("edgepulse",)


def test_provider_rejects_unknown_spinner_name() -> None:
    with pytest.raises(KeyError):
        get_provider().get("unknown")
