# CLA_PORCOND_C

## Function Signature

```fortran
CLA_PORCOND_C(UPLO, N, A, LDA, AF, LDAF, C, CAPPLY,
*                                    INFO, WORK, RWORK)
```

## Description


    CLA_PORCOND_C Computes the infinity norm condition number of
    op(A) * inv(diag(C)) where C is a REAL vector

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 = 'U': Upper triangle of A is stored; = 'L': Lower triangle of A is stored.

### N (in)

N is INTEGER The number of linear equations, i.e., the order of the matrix A. N >= 0.

### A (in)

A is COMPLEX array, dimension (LDA,N) On entry, the N-by-N matrix A

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### AF (in)

AF is COMPLEX array, dimension (LDAF,N) The triangular factor U or L from the Cholesky factorization A = U**H*U or A = L*L**H, as computed by CPOTRF.

### LDAF (in)

LDAF is INTEGER The leading dimension of the array AF. LDAF >= max(1,N).

### C (in)

C is REAL array, dimension (N) The vector C in the formula op(A) * inv(diag(C)).

### CAPPLY (in)

CAPPLY is LOGICAL If .TRUE. then access the vector C in the formula above.

### INFO (out)

INFO is INTEGER = 0: Successful exit. i > 0: The ith argument is invalid.

### WORK (out)

WORK is COMPLEX array, dimension (2*N). Workspace.

### RWORK (out)

RWORK is REAL array, dimension (N). Workspace.

