# SPOCON

## Function Signature

```fortran
SPOCON(UPLO, N, A, LDA, ANORM, RCOND, WORK, IWORK,
*                          INFO)
```

## Description


 SPOCON estimates the reciprocal of the condition number (in the
 1-norm) of a real symmetric positive definite matrix using the
 Cholesky factorization A = U**T*U or A = L*L**T computed by SPOTRF.

 An estimate is obtained for norm(inv(A)), and the reciprocal of the
 condition number is computed as RCOND = 1 / (ANORM * norm(inv(A))).

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 = 'U': Upper triangle of A is stored; = 'L': Lower triangle of A is stored.

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### A (in)

A is REAL array, dimension (LDA,N) The triangular factor U or L from the Cholesky factorization A = U**T*U or A = L*L**T, as computed by SPOTRF.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

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

