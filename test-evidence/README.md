# Copilot docs validation summary

The original implementation and follow-ups were validated on Windows with Python
3.14.3, PyYAML 6.0.3 and python-liquid 2.3.6. Final product candidate:
`5083bc0aca277475e22a6662426d94a07ed6f473`. Upstream documentation remains pinned to
`github/docs@7c3387d3b513ed43ea26c9b2e4c0e1b12234c010`.

## Completed product validation

- 55 permanent tests passed with no failures, errors or skips.
- 22 pipeline assertions passed: pinned rebuild/repeat byte equivalence, fresh
  cold fetch/build and refresh, failure preservation, shell entry point, manifest
  validation, corpus scope and staging cleanup.
- All 568 generated frontmatters matched the independent source-value oracle.
- Compared with original PR candidate `875c75b`, 531 pages were byte-identical;
  35 had metadata-only repairs and two had intended code/API-placeholder repairs.
  No Markdown pages were added or removed. The upstream license was unchanged.
- Final routing qualifications for hooks, GHES and billing were source-checked;
  all 568 pages, LICENSE and provenance were unchanged by that prose follow-up.
- Existing missing-version and plugin-listing-icon warnings were nonblocking.

These are historical results for the stated candidates, not an assertion that
future changes pass. Model scenario evaluations are separate from these technical
checks; this summary does not claim perfect answers or live-product verification.

## Cleanup validation (2026-11-11)

The relocated full validation runner passed **60 permanent tests** with no
failures, errors or skips and **23 pipeline assertions**, including the new
artifact guard. The relocated scalar regression runner passed all six assertions.
The five new hygiene tests cover force-added logs, allowed input fixtures,
ignored output placement, preservation of existing runs and invalid labels.
All product references, build generators and recipes remain unchanged from
`5083bc0`. Local Markdown links and the staged whitespace check also passed.

## Evidence handling and reproduction

Reusable validation scripts now live in [`build/validation/`](../build/validation/).
Raw per-run logs and JSON inventories are not maintained as source. The scripts
write into ignored `.build-cache/validation-results/<unique-label>/` and preserve
existing runs. See the [README workflow](../README.md#keep-generated-validation-output-out-of-git).

The cleanup removes 70 historical reports/output files and relocates the two
Python validation scripts. Original raw evidence remains in earlier commits and
in the original local test checkout; this cleanup does not erase history.

## Limits

Validation does not establish live GitHub product behavior or a cross-platform
matrix. A real child-process termination before publication was tested, but a
kill during the two-rename publication gap or power loss was not. Cross-filesystem
rejection used an injected device mismatch, not a physical multi-volume test.
The resolver supports the pinned GitHub Docs dialect, not the full site renderer.

The artifact guard detects known generated-file locations and extensions. It is
not a credential scanner and does not replace reviewing staged diffs or access
controls. A scan of the 72 original evidence files found local-machine paths in
21 files and no matches for the credential patterns checked; that is not proof
that the files contain no sensitive information.
