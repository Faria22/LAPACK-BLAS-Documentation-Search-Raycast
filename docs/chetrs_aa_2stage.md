# CHETRS_AA_2STAGE

## Function Signature

```fortran
CHETRS_AA_2STAGE(UPLO, N, NRHS, A, LDA, TB, LTB, IPIV, 
*                                   IPIV2, B, LDB, INFO)
```

## Description


 CHETRS_AA_2STAGE solves a system of linear equations A*X = B with a real
 hermitian matrix A using the factorization A = U**T*T*U or
 A = L*T*L**T computed by CHETRF_AA_2STAGE.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 Specifies whether the details of the factorization are stored as an upper or lower triangular matrix. = 'U': Upper triangular, form is A = U**T*T*U; = 'L': Lower triangular, form is A = L*T*L**T.

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### NRHS (in)

NRHS is INTEGER The number of right hand sides, i.e., the number of columns of the matrix B. NRHS >= 0.

### A (in)

A is COMPLEX array, dimension (LDA,N) Details of factors computed by CHETRF_AA_2STAGE.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### TB (out)

TB is COMPLEX array, dimension (LTB) Details of factors computed by CHETRF_AA_2STAGE.

### LTB (in)

LTB is INTEGER The size of the array TB. LTB >= 4*N.

### IPIV (in)

IPIV is INTEGER array, dimension (N) Details of the interchanges as computed by CHETRF_AA_2STAGE.

### IPIV2 (in)

IPIV2 is INTEGER array, dimension (N) Details of the interchanges as computed by CHETRF_AA_2STAGE.

### B (in,out)

B is COMPLEX array, dimension (LDB,NRHS) On entry, the right hand side matrix B. On exit, the solution matrix X.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,N).

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

