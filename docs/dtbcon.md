# DTBCON

## Function Signature

```fortran
DTBCON(NORM, UPLO, DIAG, N, KD, AB, LDAB, RCOND, WORK,
*                          IWORK, INFO)
```

## Description


 DTBCON estimates the reciprocal of the condition number of a
 triangular band matrix A, in either the 1-norm or the infinity-norm.

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

### KD (in)

KD is INTEGER The number of superdiagonals or subdiagonals of the triangular band matrix A. KD >= 0.

### AB (in)

AB is DOUBLE PRECISION array, dimension (LDAB,N) The upper or lower triangular band matrix A, stored in the first kd+1 rows of the array. The j-th column of A is stored in the j-th column of the array AB as follows: if UPLO = 'U', AB(kd+1+i-j,j) = A(i,j) for max(1,j-kd)<=i<=j; if UPLO = 'L', AB(1+i-j,j) = A(i,j) for j<=i<=min(n,j+kd). If DIAG = 'U', the diagonal elements of A are not referenced and are assumed to be 1.

### LDAB (in)

LDAB is INTEGER The leading dimension of the array AB. LDAB >= KD+1.

### RCOND (out)

RCOND is DOUBLE PRECISION The reciprocal of the condition number of the matrix A, computed as RCOND = 1/(norm(A) * norm(inv(A))).

### WORK (out)

WORK is DOUBLE PRECISION array, dimension (3*N)

### IWORK (out)

IWORK is INTEGER array, dimension (N)

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

