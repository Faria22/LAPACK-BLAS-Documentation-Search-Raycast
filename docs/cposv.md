# CPOSV

CPOSV computes the solution to system of linear equations A * X = B for PO matrices

## Function Signature

```fortran
CPOSV(UPLO, N, NRHS, A, LDA, B, LDB, INFO)
```

## Description


 CPOSV computes the solution to a complex system of linear equations
    A * X = B,
 where A is an N-by-N Hermitian positive definite matrix and X and B
 are N-by-NRHS matrices.

 The Cholesky decomposition is used to factor A as
    A = U**H* U,  if UPLO = 'U', or
    A = L * L**H,  if UPLO = 'L',
 where U is an upper triangular matrix and  L is a lower triangular
 matrix.  The factored form of A is then used to solve the system of
 equations A * X = B.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 = 'U': Upper triangle of A is stored; = 'L': Lower triangle of A is stored.

### N (in)

N is INTEGER The number of linear equations, i.e., the order of the matrix A. N >= 0.

### NRHS (in)

NRHS is INTEGER The number of right hand sides, i.e., the number of columns of the matrix B. NRHS >= 0.

### A (in,out)

A is COMPLEX array, dimension (LDA,N) On entry, the Hermitian matrix A. If UPLO = 'U', the leading N-by-N upper triangular part of A contains the upper triangular part of the matrix A, and the strictly lower triangular part of A is not referenced. If UPLO = 'L', the leading N-by-N lower triangular part of A contains the lower triangular part of the matrix A, and the strictly upper triangular part of A is not referenced. On exit, if INFO = 0, the factor U or L from the Cholesky factorization A = U**H*U or A = L*L**H.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### B (in,out)

B is COMPLEX array, dimension (LDB,NRHS) On entry, the N-by-NRHS right hand side matrix B. On exit, if INFO = 0, the N-by-NRHS solution matrix X.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,N).

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value > 0: if INFO = i, the leading principal minor of order i of A is not positive, so the factorization could not be completed, and the solution has not been computed.

