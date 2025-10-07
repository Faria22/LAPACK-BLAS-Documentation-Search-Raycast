# SORGRQ

## Function Signature

```fortran
SORGRQ(M, N, K, A, LDA, TAU, WORK, LWORK, INFO)
```

## Description


 SORGRQ generates an M-by-N real matrix Q with orthonormal rows,
 which is defined as the last M rows of a product of K elementary
 reflectors of order N

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

A is REAL array, dimension (LDA,N) On entry, the (m-k+i)-th row must contain the vector which defines the elementary reflector H(i), for i = 1,2,...,k, as returned by SGERQF in the last k rows of its array argument A. On exit, the M-by-N matrix Q.

### LDA (in)

LDA is INTEGER The first dimension of the array A. LDA >= max(1,M).

### TAU (in)

TAU is REAL array, dimension (K) TAU(i) must contain the scalar factor of the elementary reflector H(i), as returned by SGERQF.

### WORK (out)

WORK is REAL array, dimension (MAX(1,LWORK)) On exit, if INFO = 0, WORK(1) returns the optimal LWORK.

### LWORK (in)

LWORK is INTEGER The dimension of the array WORK. LWORK >= max(1,M). For optimum performance LWORK >= M*NB, where NB is the optimal blocksize. If LWORK = -1, then a workspace query is assumed; the routine only calculates the optimal size of the WORK array, returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument has an illegal value

