# DLANSY

## Function Signature

```fortran
DLANSY(NORM, UPLO, N, A, LDA, WORK)
```

## Description


 DLANSY  returns the value of the one norm,  or the Frobenius norm, or
 the  infinity norm,  or the  element of  largest absolute value  of a
 real symmetric matrix A.

## Parameters

### NORM (in)

NORM is CHARACTER*1 Specifies the value to be returned in DLANSY as described above.

### UPLO (in)

UPLO is CHARACTER*1 Specifies whether the upper or lower triangular part of the symmetric matrix A is to be referenced. = 'U': Upper triangular part of A is referenced = 'L': Lower triangular part of A is referenced

### N (in)

N is INTEGER The order of the matrix A. N >= 0. When N = 0, DLANSY is set to zero.

### A (in)

A is DOUBLE PRECISION array, dimension (LDA,N) The symmetric matrix A. If UPLO = 'U', the leading n by n upper triangular part of A contains the upper triangular part of the matrix A, and the strictly lower triangular part of A is not referenced. If UPLO = 'L', the leading n by n lower triangular part of A contains the lower triangular part of the matrix A, and the strictly upper triangular part of A is not referenced.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(N,1).

### WORK (out)

WORK is DOUBLE PRECISION array, dimension (MAX(1,LWORK)), where LWORK >= N when NORM = 'I' or '1' or 'O'; otherwise, WORK is not referenced.

