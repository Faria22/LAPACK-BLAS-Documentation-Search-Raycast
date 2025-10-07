# DTRTTF

## Function Signature

```fortran
DTRTTF(TRANSR, UPLO, N, A, LDA, ARF, INFO)
```

## Description


 DTRTTF copies a triangular matrix A from standard full format (TR)
 to rectangular full packed format (TF) .

## Parameters

### TRANSR (in)

TRANSR is CHARACTER*1 = 'N': ARF in Normal form is wanted; = 'T': ARF in Transpose form is wanted.

### UPLO (in)

UPLO is CHARACTER*1 = 'U': Upper triangle of A is stored; = 'L': Lower triangle of A is stored.

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### A (in)

A is DOUBLE PRECISION array, dimension (LDA,N). On entry, the triangular matrix A. If UPLO = 'U', the leading N-by-N upper triangular part of the array A contains the upper triangular matrix, and the strictly lower triangular part of A is not referenced. If UPLO = 'L', the leading N-by-N lower triangular part of the array A contains the lower triangular matrix, and the strictly upper triangular part of A is not referenced.

### LDA (in)

LDA is INTEGER The leading dimension of the matrix A. LDA >= max(1,N).

### ARF (out)

ARF is DOUBLE PRECISION array, dimension (NT). NT=N*(N+1)/2. On exit, the triangular matrix A in RFP format.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

