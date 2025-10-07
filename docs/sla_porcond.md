# SLA_PORCOND

## Function Signature

```fortran
SLA_PORCOND(UPLO, N, A, LDA, AF, LDAF, CMODE, C,
*                                  INFO, WORK, IWORK)
```

## Description


    SLA_PORCOND Estimates the Skeel condition number of  op(A) * op2(C)
    where op2 is determined by CMODE as follows
    CMODE =  1    op2(C) = C
    CMODE =  0    op2(C) = I
    CMODE = -1    op2(C) = inv(C)
    The Skeel condition number  cond(A) = norminf( |inv(A)||A| )
    is computed by computing scaling factors R such that
    diag(R)*A*op2(C) is row equilibrated and computing the standard
    infinity-norm condition number.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 = 'U': Upper triangle of A is stored; = 'L': Lower triangle of A is stored.

### N (in)

N is INTEGER The number of linear equations, i.e., the order of the matrix A. N >= 0.

### A (in)

A is REAL array, dimension (LDA,N) On entry, the N-by-N matrix A.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### AF (in)

AF is REAL array, dimension (LDAF,N) The triangular factor U or L from the Cholesky factorization A = U**T*U or A = L*L**T, as computed by SPOTRF.

### LDAF (in)

LDAF is INTEGER The leading dimension of the array AF. LDAF >= max(1,N).

### CMODE (in)

CMODE is INTEGER Determines op2(C) in the formula op(A) * op2(C) as follows: CMODE = 1 op2(C) = C CMODE = 0 op2(C) = I CMODE = -1 op2(C) = inv(C)

### C (in)

C is REAL array, dimension (N) The vector C in the formula op(A) * op2(C).

### INFO (out)

INFO is INTEGER = 0: Successful exit. i > 0: The ith argument is invalid.

### WORK (out)

WORK is REAL array, dimension (3*N). Workspace.

### IWORK (out)

IWORK is INTEGER array, dimension (N). Workspace.

