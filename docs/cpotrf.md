# CPOTRF

## Function Signature

```fortran
CPOTRF(UPLO, N, A, LDA, INFO)
```

## Description


 CPOTRF computes the Cholesky factorization of a complex Hermitian
 positive definite matrix A.

 The factorization has the form
    A = U**H * U,  if UPLO = 'U', or
    A = L  * L**H,  if UPLO = 'L',
 where U is an upper triangular matrix and L is lower triangular.

 This is the block version of the algorithm, calling Level 3 BLAS.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 = 'U': Upper triangle of A is stored; = 'L': Lower triangle of A is stored.

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### A (in,out)

A is COMPLEX array, dimension (LDA,N) On entry, the Hermitian matrix A. If UPLO = 'U', the leading N-by-N upper triangular part of A contains the upper triangular part of the matrix A, and the strictly lower triangular part of A is not referenced. If UPLO = 'L', the leading N-by-N lower triangular part of A contains the lower triangular part of the matrix A, and the strictly upper triangular part of A is not referenced. On exit, if INFO = 0, the factor U or L from the Cholesky factorization A = U**H*U or A = L*L**H.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value > 0: if INFO = i, the leading principal minor of order i is not positive, and the factorization could not be completed.

