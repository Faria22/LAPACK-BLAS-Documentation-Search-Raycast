# SGEQRT3

## Function Signature

```fortran
SGEQRT3(M, N, A, LDA, T, LDT, INFO)
```

## Description


 SGEQRT3 recursively computes a QR factorization of a real M-by-N
 matrix A, using the compact WY representation of Q.

 Based on the algorithm of Elmroth and Gustavson,
 IBM J. Res. Develop. Vol 44 No. 4 July 2000.

## Parameters

### M (in)

M is INTEGER The number of rows of the matrix A. M >= N.

### N (in)

N is INTEGER The number of columns of the matrix A. N >= 0.

### A (in,out)

A is REAL array, dimension (LDA,N) On entry, the real M-by-N matrix A. On exit, the elements on and above the diagonal contain the N-by-N upper triangular matrix R; the elements below the diagonal are the columns of V. See below for further details.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,M).

### T (out)

T is REAL array, dimension (LDT,N) The N-by-N upper triangular factor of the block reflector. The elements on and above the diagonal contain the block reflector T; the elements below the diagonal are not used. See below for further details.

### LDT (in)

LDT is INTEGER The leading dimension of the array T. LDT >= max(1,N).

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

