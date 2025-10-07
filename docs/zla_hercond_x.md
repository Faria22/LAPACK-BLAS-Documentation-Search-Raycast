# ZLA_HERCOND_X

## Function Signature

```fortran
ZLA_HERCOND_X(UPLO, N, A, LDA, AF,
*                                                LDAF, IPIV, X, INFO,
*                                                WORK, RWORK)
```

## Description


    ZLA_HERCOND_X computes the infinity norm condition number of
    op(A) * diag(X) where X is a COMPLEX*16 vector.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 = 'U': Upper triangle of A is stored; = 'L': Lower triangle of A is stored.

### N (in)

N is INTEGER The number of linear equations, i.e., the order of the matrix A. N >= 0.

### A (in)

A is COMPLEX*16 array, dimension (LDA,N) On entry, the N-by-N matrix A.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### AF (in)

AF is COMPLEX*16 array, dimension (LDAF,N) The block diagonal matrix D and the multipliers used to obtain the factor U or L as computed by ZHETRF.

### LDAF (in)

LDAF is INTEGER The leading dimension of the array AF. LDAF >= max(1,N).

### IPIV (in)

IPIV is INTEGER array, dimension (N) Details of the interchanges and the block structure of D as determined by CHETRF.

### X (in)

X is COMPLEX*16 array, dimension (N) The vector X in the formula op(A) * diag(X).

### INFO (out)

INFO is INTEGER = 0: Successful exit. i > 0: The ith argument is invalid.

### WORK (out)

WORK is COMPLEX*16 array, dimension (2*N). Workspace.

### RWORK (out)

RWORK is DOUBLE PRECISION array, dimension (N). Workspace.

