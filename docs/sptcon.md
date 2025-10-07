# SPTCON

## Function Signature

```fortran
SPTCON(N, D, E, ANORM, RCOND, WORK, INFO)
```

## Description


 SPTCON computes the reciprocal of the condition number (in the
 1-norm) of a real symmetric positive definite tridiagonal matrix
 using the factorization A = L*D*L**T or A = U**T*D*U computed by
 SPTTRF.

 Norm(inv(A)) is computed by a direct method, and the reciprocal of
 the condition number is computed as
              RCOND = 1 / (ANORM * norm(inv(A))).

## Parameters

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### D (in)

D is REAL array, dimension (N) The n diagonal elements of the diagonal matrix D from the factorization of A, as computed by SPTTRF.

### E (in)

E is REAL array, dimension (N-1) The (n-1) off-diagonal elements of the unit bidiagonal factor U or L from the factorization of A, as computed by SPTTRF.

### ANORM (in)

ANORM is REAL The 1-norm of the original matrix A.

### RCOND (out)

RCOND is REAL The reciprocal of the condition number of the matrix A, computed as RCOND = 1/(ANORM * AINVNM), where AINVNM is the 1-norm of inv(A) computed in this routine.

### WORK (out)

WORK is REAL array, dimension (N)

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

