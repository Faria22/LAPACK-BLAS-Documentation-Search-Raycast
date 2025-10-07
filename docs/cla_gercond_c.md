# CLA_GERCOND_C

## Function Signature

```fortran
CLA_GERCOND_C(TRANS, N, A, LDA, AF, LDAF, IPIV, C,
*                                    CAPPLY, INFO, WORK, RWORK)
```

## Description



    CLA_GERCOND_C computes the infinity norm condition number of
    op(A) * inv(diag(C)) where C is a REAL vector.

## Parameters

### TRANS (in)

TRANS is CHARACTER*1 Specifies the form of the system of equations: = 'N': A * X = B (No transpose) = 'T': A**T * X = B (Transpose) = 'C': A**H * X = B (Conjugate Transpose = Transpose)

### N (in)

N is INTEGER The number of linear equations, i.e., the order of the matrix A. N >= 0.

### A (in)

A is COMPLEX array, dimension (LDA,N) On entry, the N-by-N matrix A

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### AF (in)

AF is COMPLEX array, dimension (LDAF,N) The factors L and U from the factorization A = P*L*U as computed by CGETRF.

### LDAF (in)

LDAF is INTEGER The leading dimension of the array AF. LDAF >= max(1,N).

### IPIV (in)

IPIV is INTEGER array, dimension (N) The pivot indices from the factorization A = P*L*U as computed by CGETRF; row i of the matrix was interchanged with row IPIV(i).

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

