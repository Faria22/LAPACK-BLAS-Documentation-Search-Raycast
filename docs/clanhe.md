# CLANHE

## Function Signature

```fortran
CLANHE(NORM, UPLO, N, A, LDA, WORK)
```

## Description


 CLANHE  returns the value of the one norm,  or the Frobenius norm, or
 the  infinity norm,  or the  element of  largest absolute value  of a
 complex hermitian matrix A.

## Parameters

### NORM (in)

NORM is CHARACTER*1 Specifies the value to be returned in CLANHE as described above.

### UPLO (in)

UPLO is CHARACTER*1 Specifies whether the upper or lower triangular part of the hermitian matrix A is to be referenced. = 'U': Upper triangular part of A is referenced = 'L': Lower triangular part of A is referenced

### N (in)

N is INTEGER The order of the matrix A. N >= 0. When N = 0, CLANHE is set to zero.

### A (in)

A is COMPLEX array, dimension (LDA,N) The hermitian matrix A. If UPLO = 'U', the leading n by n upper triangular part of A contains the upper triangular part of the matrix A, and the strictly lower triangular part of A is not referenced. If UPLO = 'L', the leading n by n lower triangular part of A contains the lower triangular part of the matrix A, and the strictly upper triangular part of A is not referenced. Note that the imaginary parts of the diagonal elements need not be set and are assumed to be zero.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(N,1).

### WORK (out)

WORK is REAL array, dimension (MAX(1,LWORK)), where LWORK >= N when NORM = 'I' or '1' or 'O'; otherwise, WORK is not referenced.

