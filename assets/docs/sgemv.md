# SGEMV - Single Precision General Matrix-Vector Multiplication

## Purpose

SGEMV performs matrix-vector multiplication (single precision).

## Signature

```fortran
SUBROUTINE SGEMV(TRANS, M, N, ALPHA, A, LDA, X, INCX, BETA, Y, INCY)
```

## Parameters

**TRANS** : *CHARACTER*
> Operation: 'N' for A*x, 'T' for A^T*x.

**M, N** : *INTEGER*
> Dimensions of matrix A.

**ALPHA, BETA** : *REAL*
> Scalar multipliers.

**A** : *REAL array, dimension (LDA, N)*
> The matrix A.

**X, Y** : *REAL arrays*
> Input and output vectors.

## Notes

Level 2 BLAS routine.
