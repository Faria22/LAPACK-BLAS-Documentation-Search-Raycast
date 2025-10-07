# DTFTTP

## Function Signature

```fortran
DTFTTP(TRANSR, UPLO, N, ARF, AP, INFO)
```

## Description


 DTFTTP copies a triangular matrix A from rectangular full packed
 format (TF) to standard packed format (TP).

## Parameters

### TRANSR (in)

TRANSR is CHARACTER*1 = 'N': ARF is in Normal format; = 'T': ARF is in Transpose format;

### UPLO (in)

UPLO is CHARACTER*1 = 'U': A is upper triangular; = 'L': A is lower triangular.

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### ARF (in)

ARF is DOUBLE PRECISION array, dimension ( N*(N+1)/2 ), On entry, the upper or lower triangular matrix A stored in RFP format. For a further discussion see Notes below.

### AP (out)

AP is DOUBLE PRECISION array, dimension ( N*(N+1)/2 ), On exit, the upper or lower triangular matrix A, packed columnwise in a linear array. The j-th column of A is stored in the array AP as follows: if UPLO = 'U', AP(i + (j-1)*j/2) = A(i,j) for 1<=i<=j; if UPLO = 'L', AP(i + (j-1)*(2n-j)/2) = A(i,j) for j<=i<=n.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

