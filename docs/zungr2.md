# ZUNGR2

## Function Signature

```fortran
ZUNGR2(M, N, K, A, LDA, TAU, WORK, INFO)
```

## Description


 ZUNGR2 generates an m by n complex matrix Q with orthonormal rows,
 which is defined as the last m rows of a product of k elementary
 reflectors of order n

       Q  =  H(1)**H H(2)**H . . . H(k)**H

 as returned by ZGERQF.

## Parameters

### M (in)

M is INTEGER The number of rows of the matrix Q. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix Q. N >= M.

### K (in)

K is INTEGER The number of elementary reflectors whose product defines the matrix Q. M >= K >= 0.

### A (in,out)

A is COMPLEX*16 array, dimension (LDA,N) On entry, the (m-k+i)-th row must contain the vector which defines the elementary reflector H(i), for i = 1,2,...,k, as returned by ZGERQF in the last k rows of its array argument A. On exit, the m-by-n matrix Q.

### LDA (in)

LDA is INTEGER The first dimension of the array A. LDA >= max(1,M).

### TAU (in)

TAU is COMPLEX*16 array, dimension (K) TAU(i) must contain the scalar factor of the elementary reflector H(i), as returned by ZGERQF.

### WORK (out)

WORK is COMPLEX*16 array, dimension (M)

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument has an illegal value

