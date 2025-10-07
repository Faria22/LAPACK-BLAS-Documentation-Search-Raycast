# SPPCON

## Function Signature

```fortran
SPPCON(UPLO, N, AP, ANORM, RCOND, WORK, IWORK, INFO)
```

## Description


 SPPCON estimates the reciprocal of the condition number (in the
 1-norm) of a real symmetric positive definite packed matrix using
 the Cholesky factorization A = U**T*U or A = L*L**T computed by
 SPPTRF.

 An estimate is obtained for norm(inv(A)), and the reciprocal of the
 condition number is computed as RCOND = 1 / (ANORM * norm(inv(A))).

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 = 'U': Upper triangle of A is stored; = 'L': Lower triangle of A is stored.

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### AP (in)

AP is REAL array, dimension (N*(N+1)/2) The triangular factor U or L from the Cholesky factorization A = U**T*U or A = L*L**T, packed columnwise in a linear array. The j-th column of U or L is stored in the array AP as follows: if UPLO = 'U', AP(i + (j-1)*j/2) = U(i,j) for 1<=i<=j; if UPLO = 'L', AP(i + (j-1)*(2n-j)/2) = L(i,j) for j<=i<=n.

### ANORM (in)

ANORM is REAL The 1-norm (or infinity-norm) of the symmetric matrix A.

### RCOND (out)

RCOND is REAL The reciprocal of the condition number of the matrix A, computed as RCOND = 1/(ANORM * AINVNM), where AINVNM is an estimate of the 1-norm of inv(A) computed in this routine.

### WORK (out)

WORK is REAL array, dimension (3*N)

### IWORK (out)

IWORK is INTEGER array, dimension (N)

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

