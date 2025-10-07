# ZLAT2C

## Function Signature

```fortran
ZLAT2C(UPLO, N, A, LDA, SA, LDSA, INFO)
```

## Description


 ZLAT2C converts a COMPLEX*16 triangular matrix, SA, to a COMPLEX
 triangular matrix, A.

 RMAX is the overflow for the SINGLE PRECISION arithmetic
 ZLAT2C checks that all the entries of A are between -RMAX and
 RMAX. If not the conversion is aborted and a flag is raised.

 This is an auxiliary routine so there is no argument checking.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 = 'U': A is upper triangular; = 'L': A is lower triangular.

### N (in)

N is INTEGER The number of rows and columns of the matrix A. N >= 0.

### A (in)

A is COMPLEX*16 array, dimension (LDA,N) On entry, the N-by-N triangular coefficient matrix A.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### SA (out)

SA is COMPLEX array, dimension (LDSA,N) Only the UPLO part of SA is referenced. On exit, if INFO=0, the N-by-N coefficient matrix SA; if INFO>0, the content of the UPLO part of SA is unspecified.

### LDSA (in)

LDSA is INTEGER The leading dimension of the array SA. LDSA >= max(1,M).

### INFO (out)

INFO is INTEGER = 0: successful exit. = 1: an entry of the matrix A is greater than the SINGLE PRECISION overflow threshold, in this case, the content of the UPLO part of SA in exit is unspecified.

