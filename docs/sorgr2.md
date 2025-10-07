# SORGR2

## Function Signature

```fortran
SORGR2(M, N, K, A, LDA, TAU, WORK, INFO)
```

## Description


 SORGR2 generates an m by n real matrix Q with orthonormal rows,
 which is defined as the last m rows of a product of k elementary
 reflectors of order n

       Q  =  H(1) H(2) . . . H(k)

 as returned by SGERQF.

## Parameters

### M (in)

M is INTEGER The number of rows of the matrix Q. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix Q. N >= M.

### K (in)

K is INTEGER The number of elementary reflectors whose product defines the matrix Q. M >= K >= 0.

### A (in,out)

A is REAL array, dimension (LDA,N) On entry, the (m-k+i)-th row must contain the vector which defines the elementary reflector H(i), for i = 1,2,...,k, as returned by SGERQF in the last k rows of its array argument A. On exit, the m by n matrix Q.

### LDA (in)

LDA is INTEGER The first dimension of the array A. LDA >= max(1,M).

### TAU (in)

TAU is REAL array, dimension (K) TAU(i) must contain the scalar factor of the elementary reflector H(i), as returned by SGERQF.

### WORK (out)

WORK is REAL array, dimension (M)

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument has an illegal value

