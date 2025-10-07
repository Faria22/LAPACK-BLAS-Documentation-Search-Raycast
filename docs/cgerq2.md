# CGERQ2

## Function Signature

```fortran
CGERQ2(M, N, A, LDA, TAU, WORK, INFO)
```

## Description


 CGERQ2 computes an RQ factorization of a complex m by n matrix A:
 A = R * Q.

## Parameters

### M (in)

M is INTEGER The number of rows of the matrix A. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix A. N >= 0.

### A (in,out)

A is COMPLEX array, dimension (LDA,N) On entry, the m by n matrix A. On exit, if m <= n, the upper triangle of the subarray A(1:m,n-m+1:n) contains the m by m upper triangular matrix R; if m >= n, the elements on and above the (m-n)-th subdiagonal contain the m by n upper trapezoidal matrix R; the remaining elements, with the array TAU, represent the unitary matrix Q as a product of elementary reflectors (see Further Details).

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,M).

### TAU (out)

TAU is COMPLEX array, dimension (min(M,N)) The scalar factors of the elementary reflectors (see Further Details).

### WORK (out)

WORK is COMPLEX array, dimension (M)

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

