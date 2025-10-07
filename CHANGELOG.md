# LAPACK/BLAS Documentation Search Changelog

## [1.1.0] - {PR_MERGE_DATE}

### Added
- Scripted Netlib synchronization (`scripts/generate_inventory.py`) to backfill markdown docs and rebuild metadata.
- 200 missing routine markdown files generated directly from official documentation (e.g., `ddot`, `cdotc`, `sdsdot`).
- Expanded inventory to 2,178 LAPACK/BLAS routines with official URLs, categories, and summaries sourced from Netlib.

## [Initial Version] - 2025-01-07

### Added
- Initial implementation of LAPACK/BLAS Documentation Search extension
- Local-first architecture with no web dependencies
- 30 commonly used LAPACK/BLAS routines with detailed documentation
- Instant search through function names, descriptions, and categories
- Markdown-based documentation system
- Support for both double and single precision routines
- Categories include:
  - BLAS Level 1, 2, and 3 operations
  - LAPACK linear systems solvers
  - LAPACK factorizations (LU, QR, Cholesky)
  - LAPACK eigenvalue and SVD solvers
- Quick actions:
  - View full documentation
  - Open official documentation in browser
  - Copy routine name and URLs
