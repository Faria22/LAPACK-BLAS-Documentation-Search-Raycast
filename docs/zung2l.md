# ZUNG2L

## Function Signature

```fortran
ZUNG2L(M, N, K, A, LDA, TAU, WORK, INFO)
```

## Description


 ZUNG2L generates an m by n complex matrix Q with orthonormal columns,
 which is defined as the last n columns of a product of k elementary
 reflectors of order m

       Q  =  H(k) . . . H(2) H(1)

 as returned by ZGEQLF.

## Parameters

### M (in)

M is INTEGER The number of rows of the matrix Q. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix Q. M >= N >= 0.

### K (in)

K is INTEGER The number of elementary reflectors whose product defines the matrix Q. N >= K >= 0.

### A (in,out)

A is COMPLEX*16 array, dimension (LDA,N) On entry, the (n-k+i)-th column must contain the vector which defines the elementary reflector H(i), for i = 1,2,...,k, as returned by ZGEQLF in the last k columns of its array argument A. On exit, the m-by-n matrix Q.

### LDA (in)

LDA is INTEGER The first dimension of the array A. LDA >= max(1,M).

### TAU (in)

TAU is COMPLEX*16 array, dimension (K) TAU(i) must contain the scalar factor of the elementary reflector H(i), as returned by ZGEQLF.

### WORK (out)

WORK is COMPLEX*16 array, dimension (N)

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument has an illegal value

