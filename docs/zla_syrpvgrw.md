# ZLA_SYRPVGRW

## Function Signature

```fortran
ZLA_SYRPVGRW(UPLO, N, INFO, A, LDA, AF,
*                                               LDAF, IPIV, WORK)
```

## Description



 ZLA_SYRPVGRW computes the reciprocal pivot growth factor
 norm(A)/norm(U). The "max absolute element" norm is used. If this is
 much less than 1, the stability of the LU factorization of the
 (equilibrated) matrix A could be poor. This also means that the
 solution X, estimated condition numbers, and error bounds could be
 unreliable.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 = 'U': Upper triangle of A is stored; = 'L': Lower triangle of A is stored.

### N (in)

N is INTEGER The number of linear equations, i.e., the order of the matrix A. N >= 0.

### INFO (in)

INFO is INTEGER The value of INFO returned from ZSYTRF, .i.e., the pivot in column INFO is exactly 0.

### A (in)

A is COMPLEX*16 array, dimension (LDA,N) On entry, the N-by-N matrix A.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### AF (in)

AF is COMPLEX*16 array, dimension (LDAF,N) The block diagonal matrix D and the multipliers used to obtain the factor U or L as computed by ZSYTRF.

### LDAF (in)

LDAF is INTEGER The leading dimension of the array AF. LDAF >= max(1,N).

### IPIV (in)

IPIV is INTEGER array, dimension (N) Details of the interchanges and the block structure of D as determined by ZSYTRF.

### WORK (out)

WORK is DOUBLE PRECISION array, dimension (2*N)

