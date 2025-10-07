# ZLA_HERCOND_C

## Function Signature

```fortran
ZLA_HERCOND_C(UPLO, N, A, LDA, AF,
*                                                LDAF, IPIV, C, CAPPLY,
*                                                INFO, WORK, RWORK)
```

## Description


    ZLA_HERCOND_C computes the infinity norm condition number of
    op(A) * inv(diag(C)) where C is a DOUBLE PRECISION vector.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 = 'U': Upper triangle of A is stored; = 'L': Lower triangle of A is stored.

### N (in)

N is INTEGER The number of linear equations, i.e., the order of the matrix A. N >= 0.

### A (in)

A is COMPLEX*16 array, dimension (LDA,N) On entry, the N-by-N matrix A

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### AF (in)

AF is COMPLEX*16 array, dimension (LDAF,N) The block diagonal matrix D and the multipliers used to obtain the factor U or L as computed by ZHETRF.

### LDAF (in)

LDAF is INTEGER The leading dimension of the array AF. LDAF >= max(1,N).

### IPIV (in)

IPIV is INTEGER array, dimension (N) Details of the interchanges and the block structure of D as determined by CHETRF.

### C (in)

C is DOUBLE PRECISION array, dimension (N) The vector C in the formula op(A) * inv(diag(C)).

### CAPPLY (in)

CAPPLY is LOGICAL If .TRUE. then access the vector C in the formula above.

### INFO (out)

INFO is INTEGER = 0: Successful exit. i > 0: The ith argument is invalid.

### WORK (out)

WORK is COMPLEX*16 array, dimension (2*N). Workspace.

### RWORK (out)

RWORK is DOUBLE PRECISION array, dimension (N). Workspace.

