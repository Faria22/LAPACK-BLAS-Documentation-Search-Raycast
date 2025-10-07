# CSYCON

## Function Signature

```fortran
CSYCON(UPLO, N, A, LDA, IPIV, ANORM, RCOND, WORK,
*                          INFO)
```

## Description


 CSYCON estimates the reciprocal of the condition number (in the
 1-norm) of a complex symmetric matrix A using the factorization
 A = U*D*U**T or A = L*D*L**T computed by CSYTRF.

 An estimate is obtained for norm(inv(A)), and the reciprocal of the
 condition number is computed as RCOND = 1 / (ANORM * norm(inv(A))).

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 Specifies whether the details of the factorization are stored as an upper or lower triangular matrix. = 'U': Upper triangular, form is A = U*D*U**T; = 'L': Lower triangular, form is A = L*D*L**T.

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### A (in)

A is COMPLEX array, dimension (LDA,N) The block diagonal matrix D and the multipliers used to obtain the factor U or L as computed by CSYTRF.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### IPIV (in)

IPIV is INTEGER array, dimension (N) Details of the interchanges and the block structure of D as determined by CSYTRF.

### ANORM (in)

ANORM is REAL The 1-norm of the original matrix A.

### RCOND (out)

RCOND is REAL The reciprocal of the condition number of the matrix A, computed as RCOND = 1/(ANORM * AINVNM), where AINVNM is an estimate of the 1-norm of inv(A) computed in this routine.

### WORK (out)

WORK is COMPLEX array, dimension (2*N)

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

