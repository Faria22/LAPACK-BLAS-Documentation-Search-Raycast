# DTFTTR

## Function Signature

```fortran
DTFTTR(TRANSR, UPLO, N, ARF, A, LDA, INFO)
```

## Description


 DTFTTR copies a triangular matrix A from rectangular full packed
 format (TF) to standard full format (TR).

## Parameters

### TRANSR (in)

TRANSR is CHARACTER*1 = 'N': ARF is in Normal format; = 'T': ARF is in Transpose format.

### UPLO (in)

UPLO is CHARACTER*1 = 'U': A is upper triangular; = 'L': A is lower triangular.

### N (in)

N is INTEGER The order of the matrices ARF and A. N >= 0.

### ARF (in)

ARF is DOUBLE PRECISION array, dimension (N*(N+1)/2). On entry, the upper (if UPLO = 'U') or lower (if UPLO = 'L') matrix A in RFP format. See the "Notes" below for more details.

### A (out)

A is DOUBLE PRECISION array, dimension (LDA,N) On exit, the triangular matrix A. If UPLO = 'U', the leading N-by-N upper triangular part of the array A contains the upper triangular matrix, and the strictly lower triangular part of A is not referenced. If UPLO = 'L', the leading N-by-N lower triangular part of the array A contains the lower triangular matrix, and the strictly upper triangular part of A is not referenced.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

