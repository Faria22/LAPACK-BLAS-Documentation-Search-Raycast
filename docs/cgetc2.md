# CGETC2

## Function Signature

```fortran
CGETC2(N, A, LDA, IPIV, JPIV, INFO)
```

## Description


 CGETC2 computes an LU factorization, using complete pivoting, of the
 n-by-n matrix A. The factorization has the form A = P * L * U * Q,
 where P and Q are permutation matrices, L is lower triangular with
 unit diagonal elements and U is upper triangular.

 This is a level 1 BLAS version of the algorithm.

## Parameters

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### A (in,out)

A is COMPLEX array, dimension (LDA, N) On entry, the n-by-n matrix to be factored. On exit, the factors L and U from the factorization A = P*L*U*Q; the unit diagonal elements of L are not stored. If U(k, k) appears to be less than SMIN, U(k, k) is given the value of SMIN, giving a nonsingular perturbed system.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1, N).

### IPIV (out)

IPIV is INTEGER array, dimension (N). The pivot indices; for 1 <= i <= N, row i of the matrix has been interchanged with row IPIV(i).

### JPIV (out)

JPIV is INTEGER array, dimension (N). The pivot indices; for 1 <= j <= N, column j of the matrix has been interchanged with column JPIV(j).

### INFO (out)

INFO is INTEGER = 0: successful exit > 0: if INFO = k, U(k, k) is likely to produce overflow if one tries to solve for x in Ax = b. So U is perturbed to avoid the overflow.

