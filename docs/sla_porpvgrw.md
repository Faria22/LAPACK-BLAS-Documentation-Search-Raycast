# SLA_PORPVGRW

## Function Signature

```fortran
SLA_PORPVGRW(UPLO, NCOLS, A, LDA, AF, LDAF, WORK)
```

## Description



 SLA_PORPVGRW computes the reciprocal pivot growth factor
 norm(A)/norm(U). The "max absolute element" norm is used. If this is
 much less than 1, the stability of the LU factorization of the
 (equilibrated) matrix A could be poor. This also means that the
 solution X, estimated condition numbers, and error bounds could be
 unreliable.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 = 'U': Upper triangle of A is stored; = 'L': Lower triangle of A is stored.

### NCOLS (in)

NCOLS is INTEGER The number of columns of the matrix A. NCOLS >= 0.

### A (in)

A is REAL array, dimension (LDA,N) On entry, the N-by-N matrix A.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### AF (in)

AF is REAL array, dimension (LDAF,N) The triangular factor U or L from the Cholesky factorization A = U**T*U or A = L*L**T, as computed by SPOTRF.

### LDAF (in)

LDAF is INTEGER The leading dimension of the array AF. LDAF >= max(1,N).

### WORK (out)

WORK is REAL array, dimension (2*N)

