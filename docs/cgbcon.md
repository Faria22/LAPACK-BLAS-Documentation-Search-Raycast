# CGBCON

## Function Signature

```fortran
CGBCON(NORM, N, KL, KU, AB, LDAB, IPIV, ANORM, RCOND,
*                          WORK, RWORK, INFO)
```

## Description


 CGBCON estimates the reciprocal of the condition number of a complex
 general band matrix A, in either the 1-norm or the infinity-norm,
 using the LU factorization computed by CGBTRF.

 An estimate is obtained for norm(inv(A)), and the reciprocal of the
 condition number is computed as
    RCOND = 1 / ( norm(A) * norm(inv(A)) ).

## Parameters

### NORM (in)

NORM is CHARACTER*1 Specifies whether the 1-norm condition number or the infinity-norm condition number is required: = '1' or 'O': 1-norm; = 'I': Infinity-norm.

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### KL (in)

KL is INTEGER The number of subdiagonals within the band of A. KL >= 0.

### KU (in)

KU is INTEGER The number of superdiagonals within the band of A. KU >= 0.

### AB (in)

AB is COMPLEX array, dimension (LDAB,N) Details of the LU factorization of the band matrix A, as computed by CGBTRF. U is stored as an upper triangular band matrix with KL+KU superdiagonals in rows 1 to KL+KU+1, and the multipliers used during the factorization are stored in rows KL+KU+2 to 2*KL+KU+1.

### LDAB (in)

LDAB is INTEGER The leading dimension of the array AB. LDAB >= 2*KL+KU+1.

### IPIV (in)

IPIV is INTEGER array, dimension (N) The pivot indices; for 1 <= i <= N, row i of the matrix was interchanged with row IPIV(i).

### ANORM (in)

ANORM is REAL If NORM = '1' or 'O', the 1-norm of the original matrix A. If NORM = 'I', the infinity-norm of the original matrix A.

### RCOND (out)

RCOND is REAL The reciprocal of the condition number of the matrix A, computed as RCOND = 1/(norm(A) * norm(inv(A))).

### WORK (out)

WORK is COMPLEX array, dimension (2*N)

### RWORK (out)

RWORK is REAL array, dimension (N)

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

