# DLA_GERCOND

## Function Signature

```fortran
DLA_GERCOND(TRANS, N, A, LDA, AF,
*                                              LDAF, IPIV, CMODE, C,
*                                              INFO, WORK, IWORK)
```

## Description


    DLA_GERCOND estimates the Skeel condition number of op(A) * op2(C)
    where op2 is determined by CMODE as follows
    CMODE =  1    op2(C) = C
    CMODE =  0    op2(C) = I
    CMODE = -1    op2(C) = inv(C)
    The Skeel condition number cond(A) = norminf( |inv(A)||A| )
    is computed by computing scaling factors R such that
    diag(R)*A*op2(C) is row equilibrated and computing the standard
    infinity-norm condition number.

## Parameters

### TRANS (in)

TRANS is CHARACTER*1 Specifies the form of the system of equations: = 'N': A * X = B (No transpose) = 'T': A**T * X = B (Transpose) = 'C': A**H * X = B (Conjugate Transpose = Transpose)

### N (in)

N is INTEGER The number of linear equations, i.e., the order of the matrix A. N >= 0.

### A (in)

A is DOUBLE PRECISION array, dimension (LDA,N) On entry, the N-by-N matrix A.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### AF (in)

AF is DOUBLE PRECISION array, dimension (LDAF,N) The factors L and U from the factorization A = P*L*U as computed by DGETRF.

### LDAF (in)

LDAF is INTEGER The leading dimension of the array AF. LDAF >= max(1,N).

### IPIV (in)

IPIV is INTEGER array, dimension (N) The pivot indices from the factorization A = P*L*U as computed by DGETRF; row i of the matrix was interchanged with row IPIV(i).

### CMODE (in)

CMODE is INTEGER Determines op2(C) in the formula op(A) * op2(C) as follows: CMODE = 1 op2(C) = C CMODE = 0 op2(C) = I CMODE = -1 op2(C) = inv(C)

### C (in)

C is DOUBLE PRECISION array, dimension (N) The vector C in the formula op(A) * op2(C).

### INFO (out)

INFO is INTEGER = 0: Successful exit. i > 0: The ith argument is invalid.

### WORK (out)

WORK is DOUBLE PRECISION array, dimension (3*N). Workspace.

### IWORK (out)

IWORK is INTEGER array, dimension (N). Workspace.

