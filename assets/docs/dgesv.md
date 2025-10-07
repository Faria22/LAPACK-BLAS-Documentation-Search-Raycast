# DGESV - Solve a System of Linear Equations (Double Precision)

## Purpose

DGESV computes the solution to a real system of linear equations:

```
A * X = B
```

where A is an N-by-N matrix and X and B are N-by-NRHS matrices.

The LU decomposition with partial pivoting and row interchanges is used to factor A as:

```
A = P * L * U
```

where P is a permutation matrix, L is unit lower triangular, and U is upper triangular. The factored form of A is then used to solve the system.

## Signature

```fortran
SUBROUTINE DGESV(N, NRHS, A, LDA, IPIV, B, LDB, INFO)
```

## Parameters

**N** : *INTEGER*
> The number of linear equations, i.e., the order of the matrix A. N >= 0.

**NRHS** : *INTEGER*
> The number of right hand sides, i.e., the number of columns of the matrix B. NRHS >= 0.

**A** : *DOUBLE PRECISION array, dimension (LDA, N)*
> On entry, the N-by-N coefficient matrix A. On exit, the factors L and U from the factorization A = P*L*U; the unit diagonal elements of L are not stored.

**LDA** : *INTEGER*
> The leading dimension of the array A. LDA >= max(1,N).

**IPIV** : *INTEGER array, dimension (N)*
> The pivot indices that define the permutation matrix P; row i of the matrix was interchanged with row IPIV(i).

**B** : *DOUBLE PRECISION array, dimension (LDB, NRHS)*
> On entry, the N-by-NRHS matrix of right hand side matrix B. On exit, if INFO = 0, the N-by-NRHS solution matrix X.

**LDB** : *INTEGER*
> The leading dimension of the array B. LDB >= max(1,N).

**INFO** : *INTEGER*
> = 0: successful exit
> < 0: if INFO = -i, the i-th argument had an illegal value
> > 0: if INFO = i, U(i,i) is exactly zero. The factorization has been completed, but the factor U is exactly singular, so the solution could not be computed.

## Notes

DGESV is a driver routine that combines factorization and solving in one call. For repeated solutions with the same coefficient matrix A, consider using DGETRF and DGETRS separately.

## References

- LAPACK Working Note 41
- Netlib LAPACK Documentation
