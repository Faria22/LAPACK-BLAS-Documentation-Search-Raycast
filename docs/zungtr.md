# ZUNGTR

## Function Signature

```fortran
ZUNGTR(UPLO, N, A, LDA, TAU, WORK, LWORK, INFO)
```

## Description


 ZUNGTR generates a complex unitary matrix Q which is defined as the
 product of n-1 elementary reflectors of order N, as returned by
 ZHETRD:

 if UPLO = 'U', Q = H(n-1) . . . H(2) H(1),

 if UPLO = 'L', Q = H(1) H(2) . . . H(n-1).

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 = 'U': Upper triangle of A contains elementary reflectors from ZHETRD; = 'L': Lower triangle of A contains elementary reflectors from ZHETRD.

### N (in)

N is INTEGER The order of the matrix Q. N >= 0.

### A (in,out)

A is COMPLEX*16 array, dimension (LDA,N) On entry, the vectors which define the elementary reflectors, as returned by ZHETRD. On exit, the N-by-N unitary matrix Q.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= N.

### TAU (in)

TAU is COMPLEX*16 array, dimension (N-1) TAU(i) must contain the scalar factor of the elementary reflector H(i), as returned by ZHETRD.

### WORK (out)

WORK is COMPLEX*16 array, dimension (MAX(1,LWORK)) On exit, if INFO = 0, WORK(1) returns the optimal LWORK.

### LWORK (in)

LWORK is INTEGER The dimension of the array WORK. LWORK >= N-1. For optimum performance LWORK >= (N-1)*NB, where NB is the optimal blocksize. If LWORK = -1, then a workspace query is assumed; the routine only calculates the optimal size of the WORK array, returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

