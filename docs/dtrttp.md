# DTRTTP

## Function Signature

```fortran
DTRTTP(UPLO, N, A, LDA, AP, INFO)
```

## Description


 DTRTTP copies a triangular matrix A from full format (TR) to standard
 packed format (TP).

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 = 'U': A is upper triangular. = 'L': A is lower triangular.

### N (in)

N is INTEGER The order of the matrices AP and A. N >= 0.

### A (in)

A is DOUBLE PRECISION array, dimension (LDA,N) On exit, the triangular matrix A. If UPLO = 'U', the leading N-by-N upper triangular part of A contains the upper triangular part of the matrix A, and the strictly lower triangular part of A is not referenced. If UPLO = 'L', the leading N-by-N lower triangular part of A contains the lower triangular part of the matrix A, and the strictly upper triangular part of A is not referenced.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### AP (out)

AP is DOUBLE PRECISION array, dimension (N*(N+1)/2) On exit, the upper or lower triangular matrix A, packed columnwise in a linear array. The j-th column of A is stored in the array AP as follows: if UPLO = 'U', AP(i + (j-1)*j/2) = A(i,j) for 1<=i<=j; if UPLO = 'L', AP(i + (j-1)*(2n-j)/2) = A(i,j) for j<=i<=n.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

