# ZSYTRS_AA

## Function Signature

```fortran
ZSYTRS_AA(UPLO, N, NRHS, A, LDA, IPIV, B, LDB,
*                             WORK, LWORK, INFO)
```

## Description


 ZSYTRS_AA solves a system of linear equations A*X = B with a complex
 symmetric matrix A using the factorization A = U**T*T*U or
 A = L*T*L**T computed by ZSYTRF_AA.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 Specifies whether the details of the factorization are stored as an upper or lower triangular matrix. = 'U': Upper triangular, form is A = U**T*T*U; = 'L': Lower triangular, form is A = L*T*L**T.

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### NRHS (in)

NRHS is INTEGER The number of right hand sides, i.e., the number of columns of the matrix B. NRHS >= 0.

### A (in)

A is COMPLEX*16 array, dimension (LDA,N) Details of factors computed by ZSYTRF_AA.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### IPIV (in)

IPIV is INTEGER array, dimension (N) Details of the interchanges as computed by ZSYTRF_AA.

### B (in,out)

B is COMPLEX*16 array, dimension (LDB,NRHS) On entry, the right hand side matrix B. On exit, the solution matrix X.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,N).

### WORK (out)

WORK is COMPLEX*16 array, dimension (MAX(1,LWORK))

### LWORK (in)

LWORK is INTEGER The dimension of the array WORK. LWORK >= max(1,3*N-2).

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

