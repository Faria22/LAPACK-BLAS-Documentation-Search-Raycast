# ZPTCON

## Function Signature

```fortran
ZPTCON(N, D, E, ANORM, RCOND, RWORK, INFO)
```

## Description


 ZPTCON computes the reciprocal of the condition number (in the
 1-norm) of a complex Hermitian positive definite tridiagonal matrix
 using the factorization A = L*D*L**H or A = U**H*D*U computed by
 ZPTTRF.

 Norm(inv(A)) is computed by a direct method, and the reciprocal of
 the condition number is computed as
                  RCOND = 1 / (ANORM * norm(inv(A))).

## Parameters

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### D (in)

D is DOUBLE PRECISION array, dimension (N) The n diagonal elements of the diagonal matrix D from the factorization of A, as computed by ZPTTRF.

### E (in)

E is COMPLEX*16 array, dimension (N-1) The (n-1) off-diagonal elements of the unit bidiagonal factor U or L from the factorization of A, as computed by ZPTTRF.

### ANORM (in)

ANORM is DOUBLE PRECISION The 1-norm of the original matrix A.

### RCOND (out)

RCOND is DOUBLE PRECISION The reciprocal of the condition number of the matrix A, computed as RCOND = 1/(ANORM * AINVNM), where AINVNM is the 1-norm of inv(A) computed in this routine.

### RWORK (out)

RWORK is DOUBLE PRECISION array, dimension (N)

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

