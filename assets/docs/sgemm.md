# SGEMM - Single Precision General Matrix-Matrix Multiplication

## Purpose

SGEMM performs one of the matrix-matrix operations:

```
C := alpha*op(A)*op(B) + beta*C
```

where `op(X)` is one of:
- `op(X) = X` or
- `op(X) = X**T`

## Signature

```fortran
SUBROUTINE SGEMM(TRANSA, TRANSB, M, N, K, ALPHA, A, LDA, B, LDB, BETA, C, LDC)
```

## Parameters

**TRANSA** : *CHARACTER*
> Specifies the form of op(A) to be used in the matrix multiplication:
> - 'N' or 'n': op(A) = A
> - 'T' or 't': op(A) = A**T
> - 'C' or 'c': op(A) = A**T

**TRANSB** : *CHARACTER*
> Specifies the form of op(B) to be used in the matrix multiplication:
> - 'N' or 'n': op(B) = B
> - 'T' or 't': op(B) = B**T
> - 'C' or 'c': op(B) = B**T

**M** : *INTEGER*
> The number of rows of the matrix op(A) and of the matrix C. M >= 0.

**N** : *INTEGER*
> The number of columns of the matrix op(B) and the matrix C. N >= 0.

**K** : *INTEGER*
> The number of columns of the matrix op(A) and the number of rows of the matrix op(B). K >= 0.

**ALPHA** : *REAL*
> The scalar alpha.

**A** : *REAL array, dimension (LDA, ka)*
> Where ka is K when TRANSA = 'N' or 'n', and is M otherwise.

**LDA** : *INTEGER*
> The first dimension of A. When TRANSA = 'N' or 'n' then LDA >= max(1,M), otherwise LDA >= max(1,K).

**B** : *REAL array, dimension (LDB, kb)*
> Where kb is N when TRANSB = 'N' or 'n', and is K otherwise.

**LDB** : *INTEGER*
> The first dimension of B. When TRANSB = 'N' or 'n' then LDB >= max(1,K), otherwise LDB >= max(1,N).

**BETA** : *REAL*
> The scalar beta. When BETA is zero then C need not be set on input.

**C** : *REAL array, dimension (LDC, N)*
> On entry, the leading M by N part contains the matrix C. On exit, overwritten by (alpha*op(A)*op(B) + beta*C).

**LDC** : *INTEGER*
> The first dimension of C. LDC >= max(1,M).

## Notes

SGEMM is a Level 3 BLAS routine optimized for single precision operations.
