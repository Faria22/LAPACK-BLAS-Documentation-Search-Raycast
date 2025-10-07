# DSYTRS

## Function Signature

```fortran
DSYTRS(UPLO, N, NRHS, A, LDA, IPIV, B, LDB, INFO)
```

## Description


 DSYTRS solves a system of linear equations A*X = B with a real
 symmetric matrix A using the factorization A = U*D*U**T or
 A = L*D*L**T computed by DSYTRF.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 Specifies whether the details of the factorization are stored as an upper or lower triangular matrix. = 'U': Upper triangular, form is A = U*D*U**T; = 'L': Lower triangular, form is A = L*D*L**T.

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### NRHS (in)

NRHS is INTEGER The number of right hand sides, i.e., the number of columns of the matrix B. NRHS >= 0.

### A (in)

A is DOUBLE PRECISION array, dimension (LDA,N) The block diagonal matrix D and the multipliers used to obtain the factor U or L as computed by DSYTRF.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### IPIV (in)

IPIV is INTEGER array, dimension (N) Details of the interchanges and the block structure of D as determined by DSYTRF.

### B (in,out)

B is DOUBLE PRECISION array, dimension (LDB,NRHS) On entry, the right hand side matrix B. On exit, the solution matrix X.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,N).

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

