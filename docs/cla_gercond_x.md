# CLA_GERCOND_X

## Function Signature

```fortran
CLA_GERCOND_X(TRANS, N, A, LDA, AF, LDAF, IPIV, X,
*                                    INFO, WORK, RWORK)
```

## Description



    CLA_GERCOND_X computes the infinity norm condition number of
    op(A) * diag(X) where X is a COMPLEX vector.

## Parameters

### TRANS (in)

TRANS is CHARACTER*1 Specifies the form of the system of equations: = 'N': A * X = B (No transpose) = 'T': A**T * X = B (Transpose) = 'C': A**H * X = B (Conjugate Transpose = Transpose)

### N (in)

N is INTEGER The number of linear equations, i.e., the order of the matrix A. N >= 0.

### A (in)

A is COMPLEX array, dimension (LDA,N) On entry, the N-by-N matrix A.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### AF (in)

AF is COMPLEX array, dimension (LDAF,N) The factors L and U from the factorization A = P*L*U as computed by CGETRF.

### LDAF (in)

LDAF is INTEGER The leading dimension of the array AF. LDAF >= max(1,N).

### IPIV (in)

IPIV is INTEGER array, dimension (N) The pivot indices from the factorization A = P*L*U as computed by CGETRF; row i of the matrix was interchanged with row IPIV(i).

### X (in)

X is COMPLEX array, dimension (N) The vector X in the formula op(A) * diag(X).

### INFO (out)

INFO is INTEGER = 0: Successful exit. i > 0: The ith argument is invalid.

### WORK (out)

WORK is COMPLEX array, dimension (2*N). Workspace.

### RWORK (out)

RWORK is REAL array, dimension (N). Workspace.

