# CHETRS_AA

## Function Signature

```fortran
CHETRS_AA(UPLO, N, NRHS, A, LDA, IPIV, B, LDB,
*                             WORK, LWORK, INFO)
```

## Description


 CHETRS_AA solves a system of linear equations A*X = B with a complex
 hermitian matrix A using the factorization A = U**H*T*U or
 A = L*T*L**H computed by CHETRF_AA.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 Specifies whether the details of the factorization are stored as an upper or lower triangular matrix. = 'U': Upper triangular, form is A = U**H*T*U; = 'L': Lower triangular, form is A = L*T*L**H.

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### NRHS (in)

NRHS is INTEGER The number of right hand sides, i.e., the number of columns of the matrix B. NRHS >= 0.

### A (in)

A is COMPLEX array, dimension (LDA,N) Details of factors computed by CHETRF_AA.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### IPIV (in)

IPIV is INTEGER array, dimension (N) Details of the interchanges as computed by CHETRF_AA.

### B (in,out)

B is COMPLEX array, dimension (LDB,NRHS) On entry, the right hand side matrix B. On exit, the solution matrix X.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,N).

### WORK (out)

WORK is COMPLEX array, dimension (MAX(1,LWORK))

### LWORK (in)

LWORK is INTEGER The dimension of the array WORK. If MIN(N,NRHS) = 0, LWORK >= 1, else LWORK >= 3*N-2. If LWORK = -1, then a workspace query is assumed; the routine only calculates the minimal size of the WORK array, returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

