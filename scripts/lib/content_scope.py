from __future__ import annotations

from pathlib import Path
from typing import Union

SCANNED_SECTIONS: frozenset[str] = frozenset(
    {
        "platform",
        "best-practices",
        "operations",
        "troubleshooting",
    }
)

EXCLUDED_SUBPATHS: tuple[str, ...] = ()

NAVIGATION_INDEXES: frozenset[str] = frozenset(
    {
        "platform/index.md",
        "best-practices/index.md",
        "operations/index.md",
        "troubleshooting/index.md",
        "troubleshooting/first-10-minutes/index.md",
        "troubleshooting/playbooks/index.md",
    }
)

TAUTOLOGICAL_CLAIM_MARKER: str = "primary source basis"


def is_in_scope(rel_path: Union[Path, str]) -> bool:
    rel = Path(rel_path)
    parts = rel.parts
    if not parts or parts[0] not in SCANNED_SECTIONS:
        return False

    posix = rel.as_posix()
    if any(posix.startswith(prefix) for prefix in EXCLUDED_SUBPATHS):
        return False

    if posix in NAVIGATION_INDEXES:
        return False

    return True


def is_tautological_text(text: object) -> bool:
    if not isinstance(text, str):
        return False
    return TAUTOLOGICAL_CLAIM_MARKER.casefold() in text.casefold()


__all__ = [
    "SCANNED_SECTIONS",
    "EXCLUDED_SUBPATHS",
    "NAVIGATION_INDEXES",
    "TAUTOLOGICAL_CLAIM_MARKER",
    "is_in_scope",
    "is_tautological_text",
]
