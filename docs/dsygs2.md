# DSYGS2

## Function Signature

```fortran
DSYGS2(ITYPE, UPLO, N, A, LDA, B, LDB, INFO)
```

## Description


 DSYGS2 reduces a real symmetric-definite generalized eigenproblem
 to standard form.

 If ITYPE = 1, the problem is A*x = lambda*B*x,
 and A is overwritten by inv(U**T)*A*inv(U) or inv(L)*A*inv(L**T)

 If ITYPE = 2 or 3, the problem is A*B*x = lambda*x or
 B*A*x = lambda*x, and A is overwritten by U*A*U**T or L**T *A*L.

 B must have been previously factorized as U**T *U or L*L**T by DPOTRF.

## Parameters

### ITYPE (in)

ITYPE is INTEGER = 1: compute inv(U**T)*A*inv(U) or inv(L)*A*inv(L**T); = 2 or 3: compute U*A*U**T or L**T *A*L.

### UPLO (in)

UPLO is CHARACTER*1 Specifies whether the upper or lower triangular part of the symmetric matrix A is stored, and how B has been factorized. = 'U': Upper triangular = 'L': Lower triangular

### N (in)

N is INTEGER The order of the matrices A and B. N >= 0.

### A (in,out)

A is DOUBLE PRECISION array, dimension (LDA,N) On entry, the symmetric matrix A. If UPLO = 'U', the leading n by n upper triangular part of A contains the upper triangular part of the matrix A, and the strictly lower triangular part of A is not referenced. If UPLO = 'L', the leading n by n lower triangular part of A contains the lower triangular part of the matrix A, and the strictly upper triangular part of A is not referenced. On exit, if INFO = 0, the transformed matrix, stored in the same format as A.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### B (in)

B is DOUBLE PRECISION array, dimension (LDB,N) The triangular factor from the Cholesky factorization of B, as returned by DPOTRF.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,N).

### INFO (out)

INFO is INTEGER = 0: successful exit. < 0: if INFO = -i, the i-th argument had an illegal value.

