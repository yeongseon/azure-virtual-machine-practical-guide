#!/usr/bin/env python3
"""Generate content validation status dashboard from frontmatter metadata."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib.content_scope import (  # noqa: E402
    EXCLUDED_SUBPATHS,
    NAVIGATION_INDEXES,
    SCANNED_SECTIONS,
    TAUTOLOGICAL_CLAIM_MARKER,
    is_in_scope,
    is_tautological_text,
)

ICON_VERIFIED = "✅ Verified"
ICON_PENDING = "⚠️ Pending Review"
ICON_UNVERIFIED = "➖ Unverified"
ICON_NO_META = "❓ No Metadata"


def parse_frontmatter(filepath: Path) -> dict[str, Any] | None:
    text = filepath.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return None
    try:
        return yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return None


def scan_documents(docs_dir: Path) -> list[dict[str, Any]]:
    documents = []
    for section in sorted(SCANNED_SECTIONS):
        section_dir = docs_dir / section
        if not section_dir.exists():
            continue
        for md_file in section_dir.rglob("*.md"):
            rel_path = md_file.relative_to(docs_dir)
            if not is_in_scope(rel_path):
                continue
            frontmatter = parse_frontmatter(md_file)
            doc_info = {
                "filepath": md_file,
                "rel_path": str(rel_path),
                "section": rel_path.parts[0],
                "filename": md_file.stem,
                "title": md_file.stem.replace("-", " ").title(),
                "has_content_sources": False,
                "has_content_validation": False,
                "validation_status": "no_metadata",
                "core_claims_count": 0,
                "verified_claims_count": 0,
                "tautological_claims_count": 0,
                "last_reviewed": None,
            }
            if frontmatter and isinstance(frontmatter, dict):
                if "content_sources" in frontmatter:
                    doc_info["has_content_sources"] = True
                cv = frontmatter.get("content_validation", {})
                if cv and isinstance(cv, dict):
                    doc_info["has_content_validation"] = True
                    doc_info["validation_status"] = cv.get("status", "unverified")
                    doc_info["last_reviewed"] = cv.get("last_reviewed")
                    claims = cv.get("core_claims", [])
                    if isinstance(claims, list):
                        doc_info["core_claims_count"] = len(claims)
                        doc_info["verified_claims_count"] = sum(
                            1
                            for c in claims
                            if isinstance(c, dict) and c.get("verified", False)
                        )
                        doc_info["tautological_claims_count"] = sum(
                            1
                            for c in claims
                            if isinstance(c, dict)
                            and is_tautological_text(c.get("claim"))
                        )
            documents.append(doc_info)
    return documents


def get_status_icon(status: str) -> str:
    return {
        "verified": ICON_VERIFIED,
        "pending_review": ICON_PENDING,
        "unverified": ICON_UNVERIFIED,
        "no_metadata": ICON_NO_META,
    }.get(status, ICON_NO_META)


def _scope_summary_lines() -> list[str]:
    sections = ", ".join(f"`docs/{s}/`" for s in sorted(SCANNED_SECTIONS))
    excluded = ", ".join(f"`docs/{p}`" for p in EXCLUDED_SUBPATHS) or "none"
    nav_examples = ", ".join(f"`docs/{p}`" for p in sorted(NAVIGATION_INDEXES))
    return [
        "This page tracks `content_validation` metadata for **in-scope factual-claim documents** under "
        f"{sections}. Pages outside this scope — tutorials, start-here, reference, contributing, "
        f"excluded subpaths ({excluded}), and navigation indexes ({nav_examples}) — are not counted here. "
        "See `scripts/lib/content_scope.py` for the executable scope definition.",
    ]


def generate_dashboard(documents: list[dict[str, Any]], today: date) -> str:
    total = len(documents)
    verified = sum(1 for d in documents if d["validation_status"] == "verified")
    pending = sum(1 for d in documents if d["validation_status"] == "pending_review")
    unverified = sum(1 for d in documents if d["validation_status"] == "unverified")
    no_meta = sum(1 for d in documents if d["validation_status"] == "no_metadata")

    lines: list[str] = []
    lines.append("---")
    lines.append(
        "description: In-scope content_validation coverage for the Azure Virtual Machines practical guide, generated from page frontmatter metadata."
    )
    lines.append("content_sources:")
    lines.append("  diagrams:")
    lines.append("    - id: content-validation-status-pie")
    lines.append("      type: pie")
    lines.append("      source: self-generated")
    lines.append(
        "      description: Summary of content_validation status across in-scope Azure VM documentation pages."
    )
    lines.append("      based_on:")
    lines.append(
        "        - https://learn.microsoft.com/en-us/azure/virtual-machines/overview"
    )
    lines.append(
        "        - https://learn.microsoft.com/en-us/azure/virtual-machines/availability"
    )
    lines.append(
        "        - https://learn.microsoft.com/en-us/azure/virtual-machines/disks-types"
    )
    lines.append(
        "        - https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/overview"
    )
    lines.append(
        "      justification: Auto-generated dashboard summarizing declared content_validation metadata."
    )
    lines.append("---")
    lines.append("")
    lines.append("# Content Validation Status")
    lines.append("")
    lines.extend(_scope_summary_lines())
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"*Generated: {today.isoformat()}*")
    lines.append("")
    lines.append("| Metric | Count |")
    lines.append("|---|---:|")
    lines.append(f"| In-scope factual-claim documents | {total} |")
    lines.append(f"| ✅ Verified | {verified} |")
    lines.append(f"| ⚠️ Pending review | {pending} |")
    lines.append(f"| ➖ Unverified | {unverified} |")
    lines.append(f"| ❓ No metadata | {no_meta} |")
    lines.append("")
    lines.append("<!-- diagram-id: content-validation-status-pie -->")
    lines.append("```mermaid")
    lines.append("pie title In-Scope Document Validation Status")
    if verified > 0:
        lines.append(f'    "Verified" : {verified}')
    if pending > 0:
        lines.append(f'    "Pending Review" : {pending}')
    if unverified > 0:
        lines.append(f'    "Unverified" : {unverified}')
    if no_meta > 0:
        lines.append(f'    "No Metadata" : {no_meta}')
    lines.append("```")
    lines.append("")

    by_section: dict[str, list[dict[str, Any]]] = {}
    for d in documents:
        by_section.setdefault(d["section"], []).append(d)

    lines.append("## By Section")
    lines.append("")
    for section in ["platform", "best-practices", "operations", "troubleshooting"]:
        section_docs = by_section.get(section)
        if not section_docs:
            continue
        lines.append(f"### {section.replace('-', ' ').title()}")
        lines.append("")
        lines.append("| Document | Has Sources | Status | Claims | Last Reviewed |")
        lines.append("|---|---|---|---|---|")
        for d in sorted(section_docs, key=lambda item: item["rel_path"]):
            claims = "—"
            if d["core_claims_count"] > 0:
                claims = f"{d['verified_claims_count']}/{d['core_claims_count']}"
            last_reviewed = d["last_reviewed"] or "—"
            lines.append(
                f"| [{d['title']}](../{d['rel_path']}) | {'✅' if d['has_content_sources'] else '❌'} | {get_status_icon(d['validation_status'])} | {claims} | {last_reviewed} |"
            )
        lines.append("")

    lines.append("## Validation Status")
    lines.append("")
    lines.append("| Status | Description |")
    lines.append("|---|---|")
    lines.append(
        "| `verified` | All listed core claims were checked against Microsoft Learn sources. |"
    )
    lines.append(
        "| `pending_review` | The page has metadata, but one or more claims still need verification. |"
    )
    lines.append(
        "| `unverified` | The page carries metadata, but no claims have been verified yet. |"
    )
    lines.append("")
    lines.append("## How to Add Validation")
    lines.append("")
    lines.append(
        "Add a `content_validation` block only to in-scope factual-claim pages."
    )
    lines.append("")
    lines.append("```yaml")
    lines.append("---")
    lines.append("content_validation:")
    lines.append("  status: verified")
    lines.append(f"  last_reviewed: {today.isoformat()}")
    lines.append("  reviewer: agent")
    lines.append("  core_claims:")
    lines.append(
        '    - claim: "Azure Virtual Machines supports multiple size families optimized for different workload classes."'
    )
    lines.append(
        "      source: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes"
    )
    lines.append("      verified: true")
    lines.append("```")
    lines.append("")
    lines.append(
        "Claims containing the marker "
        f"`{TAUTOLOGICAL_CLAIM_MARKER}` are rejected because they are metadata about the page rather than factual Azure behavior."
    )
    lines.append("")
    lines.append("## See Also")
    lines.append("")
    lines.append("- [Tutorial Validation Status](validation-status.md)")
    lines.append("- [VM Size Families](vm-size-families.md)")
    lines.append("- [Availability Options](availability-options.md)")
    lines.append("")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate content validation status dashboard"
    )
    parser.add_argument("--docs-dir", type=Path, default=Path("docs"))
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("docs/reference/content-validation-status.md"),
    )
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent.parent
    docs_dir = project_root / args.docs_dir
    output_path = project_root / args.output
    if not docs_dir.exists():
        print(f"Error: docs directory not found: {docs_dir}")
        raise SystemExit(1)

    documents = scan_documents(docs_dir)
    tautological_docs = [d for d in documents if d["tautological_claims_count"] > 0]
    if tautological_docs:
        print(
            f"ERROR: {len(tautological_docs)} in-scope document(s) contain tautological placeholder claims (text containing '{TAUTOLOGICAL_CLAIM_MARKER}').",
            file=sys.stderr,
        )
        for d in tautological_docs:
            print(f"  - {d['rel_path']}", file=sys.stderr)
        raise SystemExit(1)

    today = date.today()
    dashboard = generate_dashboard(documents, today)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(dashboard, encoding="utf-8")

    verified = sum(1 for d in documents if d["validation_status"] == "verified")
    print(
        f"Scanned {len(documents)} in-scope documents, {verified} verified, generated {output_path}"
    )


if __name__ == "__main__":
    main()
