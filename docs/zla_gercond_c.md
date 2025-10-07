# ZLA_GERCOND_C

## Function Signature

```fortran
ZLA_GERCOND_C(TRANS, N, A, LDA, AF,
*                                                LDAF, IPIV, C, CAPPLY,
*                                                INFO, WORK, RWORK)
```

## Description


    ZLA_GERCOND_C computes the infinity norm condition number of
    op(A) * inv(diag(C)) where C is a DOUBLE PRECISION vector.

## Parameters

### TRANS (in)

TRANS is CHARACTER*1 Specifies the form of the system of equations: = 'N': A * X = B (No transpose) = 'T': A**T * X = B (Transpose) = 'C': A**H * X = B (Conjugate Transpose = Transpose)

### N (in)

N is INTEGER The number of linear equations, i.e., the order of the matrix A. N >= 0.

### A (in)

A is COMPLEX*16 array, dimension (LDA,N) On entry, the N-by-N matrix A

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### AF (in)

AF is COMPLEX*16 array, dimension (LDAF,N) The factors L and U from the factorization A = P*L*U as computed by ZGETRF.

### LDAF (in)

LDAF is INTEGER The leading dimension of the array AF. LDAF >= max(1,N).

### IPIV (in)

IPIV is INTEGER array, dimension (N) The pivot indices from the factorization A = P*L*U as computed by ZGETRF; row i of the matrix was interchanged with row IPIV(i).

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

