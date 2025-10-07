# ZPOCON

## Function Signature

```fortran
ZPOCON(UPLO, N, A, LDA, ANORM, RCOND, WORK, RWORK,
*                          INFO)
```

## Description


 ZPOCON estimates the reciprocal of the condition number (in the
 1-norm) of a complex Hermitian positive definite matrix using the
 Cholesky factorization A = U**H*U or A = L*L**H computed by ZPOTRF.

 An estimate is obtained for norm(inv(A)), and the reciprocal of the
 condition number is computed as RCOND = 1 / (ANORM * norm(inv(A))).

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 = 'U': Upper triangle of A is stored; = 'L': Lower triangle of A is stored.

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### A (in)

A is COMPLEX*16 array, dimension (LDA,N) The triangular factor U or L from the Cholesky factorization A = U**H*U or A = L*L**H, as computed by ZPOTRF.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### ANORM (in)

ANORM is DOUBLE PRECISION The 1-norm (or infinity-norm) of the Hermitian matrix A.

### RCOND (out)

RCOND is DOUBLE PRECISION The reciprocal of the condition number of the matrix A, computed as RCOND = 1/(ANORM * AINVNM), where AINVNM is an estimate of the 1-norm of inv(A) computed in this routine.

### WORK (out)

WORK is COMPLEX*16 array, dimension (2*N)

### RWORK (out)

RWORK is DOUBLE PRECISION array, dimension (N)

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

