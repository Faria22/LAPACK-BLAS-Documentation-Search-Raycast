# ZPOTRI

## Function Signature

```fortran
ZPOTRI(UPLO, N, A, LDA, INFO)
```

## Description


 ZPOTRI computes the inverse of a complex Hermitian positive definite
 matrix A using the Cholesky factorization A = U**H*U or A = L*L**H
 computed by ZPOTRF.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 = 'U': Upper triangle of A is stored; = 'L': Lower triangle of A is stored.

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### A (in,out)

A is COMPLEX*16 array, dimension (LDA,N) On entry, the triangular factor U or L from the Cholesky factorization A = U**H*U or A = L*L**H, as computed by ZPOTRF. On exit, the upper or lower triangle of the (Hermitian) inverse of A, overwriting the input factor U or L.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value > 0: if INFO = i, the (i,i) element of the factor U or L is zero, and the inverse could not be computed.

