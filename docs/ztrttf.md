# ZTRTTF

## Function Signature

```fortran
ZTRTTF(TRANSR, UPLO, N, A, LDA, ARF, INFO)
```

## Description


 ZTRTTF copies a triangular matrix A from standard full format (TR)
 to rectangular full packed format (TF) .

## Parameters

### TRANSR (in)

TRANSR is CHARACTER*1 = 'N': ARF in Normal mode is wanted; = 'C': ARF in Conjugate Transpose mode is wanted;

### UPLO (in)

UPLO is CHARACTER*1 = 'U': A is upper triangular; = 'L': A is lower triangular.

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### A (in)

A is COMPLEX*16 array, dimension ( LDA, N ) On entry, the triangular matrix A. If UPLO = 'U', the leading N-by-N upper triangular part of the array A contains the upper triangular matrix, and the strictly lower triangular part of A is not referenced. If UPLO = 'L', the leading N-by-N lower triangular part of the array A contains the lower triangular matrix, and the strictly upper triangular part of A is not referenced.

### LDA (in)

LDA is INTEGER The leading dimension of the matrix A. LDA >= max(1,N).

### ARF (out)

ARF is COMPLEX*16 array, dimension ( N*(N+1)/2 ), On exit, the upper or lower triangular matrix A stored in RFP format. For a further discussion see Notes below.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

