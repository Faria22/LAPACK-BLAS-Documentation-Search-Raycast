# CTFTTR

## Function Signature

```fortran
CTFTTR(TRANSR, UPLO, N, ARF, A, LDA, INFO)
```

## Description


 CTFTTR copies a triangular matrix A from rectangular full packed
 format (TF) to standard full format (TR).

## Parameters

### TRANSR (in)

TRANSR is CHARACTER*1 = 'N': ARF is in Normal format; = 'C': ARF is in Conjugate-transpose format;

### UPLO (in)

UPLO is CHARACTER*1 = 'U': A is upper triangular; = 'L': A is lower triangular.

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### ARF (in)

ARF is COMPLEX array, dimension ( N*(N+1)/2 ), On entry, the upper or lower triangular matrix A stored in RFP format. For a further discussion see Notes below.

### A (out)

A is COMPLEX array, dimension ( LDA, N ) On exit, the triangular matrix A. If UPLO = 'U', the leading N-by-N upper triangular part of the array A contains the upper triangular matrix, and the strictly lower triangular part of A is not referenced. If UPLO = 'L', the leading N-by-N lower triangular part of the array A contains the lower triangular matrix, and the strictly upper triangular part of A is not referenced.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

