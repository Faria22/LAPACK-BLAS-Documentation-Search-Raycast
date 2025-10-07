# ZUNGL2

## Function Signature

```fortran
ZUNGL2(M, N, K, A, LDA, TAU, WORK, INFO)
```

## Description


 ZUNGL2 generates an m-by-n complex matrix Q with orthonormal rows,
 which is defined as the first m rows of a product of k elementary
 reflectors of order n

       Q  =  H(k)**H . . . H(2)**H H(1)**H

 as returned by ZGELQF.

## Parameters

### M (in)

M is INTEGER The number of rows of the matrix Q. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix Q. N >= M.

### K (in)

K is INTEGER The number of elementary reflectors whose product defines the matrix Q. M >= K >= 0.

### A (in,out)

A is COMPLEX*16 array, dimension (LDA,N) On entry, the i-th row must contain the vector which defines the elementary reflector H(i), for i = 1,2,...,k, as returned by ZGELQF in the first k rows of its array argument A. On exit, the m by n matrix Q.

### LDA (in)

LDA is INTEGER The first dimension of the array A. LDA >= max(1,M).

### TAU (in)

TAU is COMPLEX*16 array, dimension (K) TAU(i) must contain the scalar factor of the elementary reflector H(i), as returned by ZGELQF.

### WORK (out)

WORK is COMPLEX*16 array, dimension (M)

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument has an illegal value

