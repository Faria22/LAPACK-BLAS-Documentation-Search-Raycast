# CGEQL2

## Function Signature

```fortran
CGEQL2(M, N, A, LDA, TAU, WORK, INFO)
```

## Description


 CGEQL2 computes a QL factorization of a complex m by n matrix A:
 A = Q * L.

## Parameters

### M (in)

M is INTEGER The number of rows of the matrix A. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix A. N >= 0.

### A (in,out)

A is COMPLEX array, dimension (LDA,N) On entry, the m by n matrix A. On exit, if m >= n, the lower triangle of the subarray A(m-n+1:m,1:n) contains the n by n lower triangular matrix L; if m <= n, the elements on and below the (n-m)-th superdiagonal contain the m by n lower trapezoidal matrix L; the remaining elements, with the array TAU, represent the unitary matrix Q as a product of elementary reflectors (see Further Details).

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,M).

### TAU (out)

TAU is COMPLEX array, dimension (min(M,N)) The scalar factors of the elementary reflectors (see Further Details).

### WORK (out)

WORK is COMPLEX array, dimension (N)

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

