# DGEMM - Double Precision General Matrix-Matrix Multiplication

## Purpose

DGEMM performs one of the matrix-matrix operations:

```
C := alpha*op(A)*op(B) + beta*C
```

where `op(X)` is one of:
- `op(X) = X` or
- `op(X) = X**T`

## Signature

```fortran
SUBROUTINE DGEMM(TRANSA, TRANSB, M, N, K, ALPHA, A, LDA, B, LDB, BETA, C, LDC)
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

**ALPHA** : *DOUBLE PRECISION*
> The scalar alpha.

**A** : *DOUBLE PRECISION array, dimension (LDA, ka)*
> Where ka is K when TRANSA = 'N' or 'n', and is M otherwise. Before entry with TRANSA = 'N' or 'n', the leading M by K part of the array A must contain the matrix A, otherwise the leading K by M part of the array A must contain the matrix A.

**LDA** : *INTEGER*
> The first dimension of A as declared in the calling program. When TRANSA = 'N' or 'n' then LDA >= max(1,M), otherwise LDA >= max(1,K).

**B** : *DOUBLE PRECISION array, dimension (LDB, kb)*
> Where kb is N when TRANSB = 'N' or 'n', and is K otherwise. Before entry with TRANSB = 'N' or 'n', the leading K by N part of the array B must contain the matrix B, otherwise the leading N by K part of the array B must contain the matrix B.

**LDB** : *INTEGER*
> The first dimension of B as declared in the calling program. When TRANSB = 'N' or 'n' then LDB >= max(1,K), otherwise LDB >= max(1,N).

**BETA** : *DOUBLE PRECISION*
> The scalar beta. When BETA is zero then C need not be set on input.

**C** : *DOUBLE PRECISION array, dimension (LDC, N)*
> Before entry, the leading M by N part of the array C must contain the matrix C, except when beta is zero, in which case C need not be set on entry. On exit, the array C is overwritten by the M by N matrix (alpha*op(A)*op(B) + beta*C).

**LDC** : *INTEGER*
> The first dimension of C as declared in the calling program. LDC >= max(1,M).

## Notes

DGEMM is a Level 3 BLAS routine. Level 3 BLAS perform O(n^3) floating point operations on O(n^2) data, making them ideal for efficient use of the memory hierarchy and cache.

## References

- BLAS (Basic Linear Algebra Subprograms)
- Netlib LAPACK Documentation
