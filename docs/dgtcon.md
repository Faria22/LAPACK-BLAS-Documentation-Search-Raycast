# DGTCON

## Function Signature

```fortran
DGTCON(NORM, N, DL, D, DU, DU2, IPIV, ANORM, RCOND,
*                          WORK, IWORK, INFO)
```

## Description


 DGTCON estimates the reciprocal of the condition number of a real
 tridiagonal matrix A using the LU factorization as computed by
 DGTTRF.

 An estimate is obtained for norm(inv(A)), and the reciprocal of the
 condition number is computed as RCOND = 1 / (ANORM * norm(inv(A))).

## Parameters

### NORM (in)

NORM is CHARACTER*1 Specifies whether the 1-norm condition number or the infinity-norm condition number is required: = '1' or 'O': 1-norm; = 'I': Infinity-norm.

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### DL (in)

DL is DOUBLE PRECISION array, dimension (N-1) The (n-1) multipliers that define the matrix L from the LU factorization of A as computed by DGTTRF.

### D (in)

D is DOUBLE PRECISION array, dimension (N) The n diagonal elements of the upper triangular matrix U from the LU factorization of A.

### DU (in)

DU is DOUBLE PRECISION array, dimension (N-1) The (n-1) elements of the first superdiagonal of U.

### DU2 (in)

DU2 is DOUBLE PRECISION array, dimension (N-2) The (n-2) elements of the second superdiagonal of U.

### IPIV (in)

IPIV is INTEGER array, dimension (N) The pivot indices; for 1 <= i <= n, row i of the matrix was interchanged with row IPIV(i). IPIV(i) will always be either i or i+1; IPIV(i) = i indicates a row interchange was not required.

### ANORM (in)

ANORM is DOUBLE PRECISION If NORM = '1' or 'O', the 1-norm of the original matrix A. If NORM = 'I', the infinity-norm of the original matrix A.

### RCOND (out)

RCOND is DOUBLE PRECISION The reciprocal of the condition number of the matrix A, computed as RCOND = 1/(ANORM * AINVNM), where AINVNM is an estimate of the 1-norm of inv(A) computed in this routine.

### WORK (out)

WORK is DOUBLE PRECISION array, dimension (2*N)

### IWORK (out)

IWORK is INTEGER array, dimension (N)

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

