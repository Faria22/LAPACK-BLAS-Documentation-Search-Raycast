# ZTRCON

## Function Signature

```fortran
ZTRCON(NORM, UPLO, DIAG, N, A, LDA, RCOND, WORK,
*                          RWORK, INFO)
```

## Description


 ZTRCON estimates the reciprocal of the condition number of a
 triangular matrix A, in either the 1-norm or the infinity-norm.

 The norm of A is computed and an estimate is obtained for
 norm(inv(A)), then the reciprocal of the condition number is
 computed as
    RCOND = 1 / ( norm(A) * norm(inv(A)) ).

## Parameters

### NORM (in)

NORM is CHARACTER*1 Specifies whether the 1-norm condition number or the infinity-norm condition number is required: = '1' or 'O': 1-norm; = 'I': Infinity-norm.

### UPLO (in)

UPLO is CHARACTER*1 = 'U': A is upper triangular; = 'L': A is lower triangular.

### DIAG (in)

DIAG is CHARACTER*1 = 'N': A is non-unit triangular; = 'U': A is unit triangular.

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### A (in)

A is COMPLEX*16 array, dimension (LDA,N) The triangular matrix A. If UPLO = 'U', the leading N-by-N upper triangular part of the array A contains the upper triangular matrix, and the strictly lower triangular part of A is not referenced. If UPLO = 'L', the leading N-by-N lower triangular part of the array A contains the lower triangular matrix, and the strictly upper triangular part of A is not referenced. If DIAG = 'U', the diagonal elements of A are also not referenced and are assumed to be 1.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### RCOND (out)

RCOND is DOUBLE PRECISION The reciprocal of the condition number of the matrix A, computed as RCOND = 1/(norm(A) * norm(inv(A))).

### WORK (out)

WORK is COMPLEX*16 array, dimension (2*N)

### RWORK (out)

RWORK is DOUBLE PRECISION array, dimension (N)

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

