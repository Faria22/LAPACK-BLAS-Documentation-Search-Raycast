# ZHEGST

## Function Signature

```fortran
ZHEGST(ITYPE, UPLO, N, A, LDA, B, LDB, INFO)
```

## Description


 ZHEGST reduces a complex Hermitian-definite generalized
 eigenproblem to standard form.

 If ITYPE = 1, the problem is A*x = lambda*B*x,
 and A is overwritten by inv(U**H)*A*inv(U) or inv(L)*A*inv(L**H)

 If ITYPE = 2 or 3, the problem is A*B*x = lambda*x or
 B*A*x = lambda*x, and A is overwritten by U*A*U**H or L**H*A*L.

 B must have been previously factorized as U**H*U or L*L**H by ZPOTRF.

## Parameters

### ITYPE (in)

ITYPE is INTEGER = 1: compute inv(U**H)*A*inv(U) or inv(L)*A*inv(L**H); = 2 or 3: compute U*A*U**H or L**H*A*L.

### UPLO (in)

UPLO is CHARACTER*1 = 'U': Upper triangle of A is stored and B is factored as U**H*U; = 'L': Lower triangle of A is stored and B is factored as L*L**H.

### N (in)

N is INTEGER The order of the matrices A and B. N >= 0.

### A (in,out)

A is COMPLEX*16 array, dimension (LDA,N) On entry, the Hermitian matrix A. If UPLO = 'U', the leading N-by-N upper triangular part of A contains the upper triangular part of the matrix A, and the strictly lower triangular part of A is not referenced. If UPLO = 'L', the leading N-by-N lower triangular part of A contains the lower triangular part of the matrix A, and the strictly upper triangular part of A is not referenced. On exit, if INFO = 0, the transformed matrix, stored in the same format as A.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### B (in,out)

B is COMPLEX*16 array, dimension (LDB,N) The triangular factor from the Cholesky factorization of B, as returned by ZPOTRF. B is modified by the routine but restored on exit.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,N).

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

