# CGETF2

## Function Signature

```fortran
CGETF2(M, N, A, LDA, IPIV, INFO)
```

## Description


 CGETF2 computes an LU factorization of a general m-by-n matrix A
 using partial pivoting with row interchanges.

 The factorization has the form
    A = P * L * U
 where P is a permutation matrix, L is lower triangular with unit
 diagonal elements (lower trapezoidal if m > n), and U is upper
 triangular (upper trapezoidal if m < n).

 This is the right-looking Level 2 BLAS version of the algorithm.

## Parameters

### M (in)

M is INTEGER The number of rows of the matrix A. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix A. N >= 0.

### A (in,out)

A is COMPLEX array, dimension (LDA,N) On entry, the m by n matrix to be factored. On exit, the factors L and U from the factorization A = P*L*U; the unit diagonal elements of L are not stored.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,M).

### IPIV (out)

IPIV is INTEGER array, dimension (min(M,N)) The pivot indices; for 1 <= i <= min(M,N), row i of the matrix was interchanged with row IPIV(i).

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -k, the k-th argument had an illegal value > 0: if INFO = k, U(k,k) is exactly zero. The factorization has been completed, but the factor U is exactly singular, and division by zero will occur if it is used to solve a system of equations.

