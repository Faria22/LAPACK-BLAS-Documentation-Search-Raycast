# CUNGQR

## Function Signature

```fortran
CUNGQR(M, N, K, A, LDA, TAU, WORK, LWORK, INFO)
```

## Description


 CUNGQR generates an M-by-N complex matrix Q with orthonormal columns,
 which is defined as the first N columns of a product of K elementary
 reflectors of order M

       Q  =  H(1) H(2) . . . H(k)

 as returned by CGEQRF.

## Parameters

### M (in)

M is INTEGER The number of rows of the matrix Q. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix Q. M >= N >= 0.

### K (in)

K is INTEGER The number of elementary reflectors whose product defines the matrix Q. N >= K >= 0.

### A (in,out)

A is COMPLEX array, dimension (LDA,N) On entry, the i-th column must contain the vector which defines the elementary reflector H(i), for i = 1,2,...,k, as returned by CGEQRF in the first k columns of its array argument A. On exit, the M-by-N matrix Q.

### LDA (in)

LDA is INTEGER The first dimension of the array A. LDA >= max(1,M).

### TAU (in)

TAU is COMPLEX array, dimension (K) TAU(i) must contain the scalar factor of the elementary reflector H(i), as returned by CGEQRF.

### WORK (out)

WORK is COMPLEX array, dimension (MAX(1,LWORK)) On exit, if INFO = 0, WORK(1) returns the optimal LWORK.

### LWORK (in)

LWORK is INTEGER The dimension of the array WORK. LWORK >= max(1,N). For optimum performance LWORK >= N*NB, where NB is the optimal blocksize. If LWORK = -1, then a workspace query is assumed; the routine only calculates the optimal size of the WORK array, returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument has an illegal value

