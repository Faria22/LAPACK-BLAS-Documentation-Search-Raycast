# DGEMV - Double Precision General Matrix-Vector Multiplication

## Purpose

DGEMV performs one of the matrix-vector operations:

```
y := alpha*A*x + beta*y   or   y := alpha*A^T*x + beta*y
```

## Signature

```fortran
SUBROUTINE DGEMV(TRANS, M, N, ALPHA, A, LDA, X, INCX, BETA, Y, INCY)
```

## Parameters

**TRANS** : *CHARACTER*
> Specifies the operation: 'N' for A*x, 'T' for A^T*x.

**M** : *INTEGER*
> The number of rows of matrix A.

**N** : *INTEGER*
> The number of columns of matrix A.

**ALPHA** : *DOUBLE PRECISION*
> The scalar alpha.

**A** : *DOUBLE PRECISION array, dimension (LDA, N)*
> The matrix A.

**LDA** : *INTEGER*
> The leading dimension of A. LDA >= max(1,M).

**X** : *DOUBLE PRECISION array*
> The input vector X.

**INCX** : *INTEGER*
> The increment for X.

**BETA** : *DOUBLE PRECISION*
> The scalar beta.

**Y** : *DOUBLE PRECISION array*
> On entry, the input vector Y. On exit, the result.

**INCY** : *INTEGER*
> The increment for Y.

## Notes

DGEMV is a Level 2 BLAS routine.
