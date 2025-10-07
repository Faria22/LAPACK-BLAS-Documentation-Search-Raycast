# SGESV - Solve Linear Equations (Single Precision)

## Purpose

SGESV solves the system A * X = B using LU factorization.

## Signature

```fortran
SUBROUTINE SGESV(N, NRHS, A, LDA, IPIV, B, LDB, INFO)
```

## Parameters

**N** : *INTEGER*
> Order of matrix A.

**NRHS** : *INTEGER*
> Number of right-hand sides.

**A** : *REAL array, dimension (LDA, N)*
> Coefficient matrix (overwritten with LU factors).

**IPIV** : *INTEGER array*
> Pivot indices.

**B** : *REAL array, dimension (LDB, NRHS)*
> Right-hand side matrix (overwritten with solution).

**INFO** : *INTEGER*
> Success indicator.
