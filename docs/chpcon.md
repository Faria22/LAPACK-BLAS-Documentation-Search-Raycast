# CHPCON

## Function Signature

```fortran
CHPCON(UPLO, N, AP, IPIV, ANORM, RCOND, WORK, INFO)
```

## Description


 CHPCON estimates the reciprocal of the condition number of a complex
 Hermitian packed matrix A using the factorization A = U*D*U**H or
 A = L*D*L**H computed by CHPTRF.

 An estimate is obtained for norm(inv(A)), and the reciprocal of the
 condition number is computed as RCOND = 1 / (ANORM * norm(inv(A))).

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 Specifies whether the details of the factorization are stored as an upper or lower triangular matrix. = 'U': Upper triangular, form is A = U*D*U**H; = 'L': Lower triangular, form is A = L*D*L**H.

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### AP (in)

AP is COMPLEX array, dimension (N*(N+1)/2) The block diagonal matrix D and the multipliers used to obtain the factor U or L as computed by CHPTRF, stored as a packed triangular matrix.

### IPIV (in)

IPIV is INTEGER array, dimension (N) Details of the interchanges and the block structure of D as determined by CHPTRF.

### ANORM (in)

ANORM is REAL The 1-norm of the original matrix A.

### RCOND (out)

RCOND is REAL The reciprocal of the condition number of the matrix A, computed as RCOND = 1/(ANORM * AINVNM), where AINVNM is an estimate of the 1-norm of inv(A) computed in this routine.

### WORK (out)

WORK is COMPLEX array, dimension (2*N)

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

