# CLA_HERPVGRW

## Function Signature

```fortran
CLA_HERPVGRW(UPLO, N, INFO, A, LDA, AF, LDAF, IPIV,
*                                   WORK)
```

## Description



 CLA_HERPVGRW computes the reciprocal pivot growth factor
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

INFO is INTEGER The value of INFO returned from SSYTRF, .i.e., the pivot in column INFO is exactly 0.

### A (in)

A is COMPLEX array, dimension (LDA,N) On entry, the N-by-N matrix A.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### AF (in)

AF is COMPLEX array, dimension (LDAF,N) The block diagonal matrix D and the multipliers used to obtain the factor U or L as computed by CHETRF.

### LDAF (in)

LDAF is INTEGER The leading dimension of the array AF. LDAF >= max(1,N).

### IPIV (in)

IPIV is INTEGER array, dimension (N) Details of the interchanges and the block structure of D as determined by CHETRF.

### WORK (out)

WORK is REAL array, dimension (2*N)

