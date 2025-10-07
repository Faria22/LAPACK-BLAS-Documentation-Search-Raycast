# SLANTR

## Function Signature

```fortran
SLANTR(NORM, UPLO, DIAG, M, N, A, LDA,
*                        WORK)
```

## Description


 SLANTR  returns the value of the one norm,  or the Frobenius norm, or
 the  infinity norm,  or the  element of  largest absolute value  of a
 trapezoidal or triangular matrix A.

## Parameters

### NORM (in)

NORM is CHARACTER*1 Specifies the value to be returned in SLANTR as described above.

### UPLO (in)

UPLO is CHARACTER*1 Specifies whether the matrix A is upper or lower trapezoidal. = 'U': Upper trapezoidal = 'L': Lower trapezoidal Note that A is triangular instead of trapezoidal if M = N.

### DIAG (in)

DIAG is CHARACTER*1 Specifies whether or not the matrix A has unit diagonal. = 'N': Non-unit diagonal = 'U': Unit diagonal

### M (in)

M is INTEGER The number of rows of the matrix A. M >= 0, and if UPLO = 'U', M <= N. When M = 0, SLANTR is set to zero.

### N (in)

N is INTEGER The number of columns of the matrix A. N >= 0, and if UPLO = 'L', N <= M. When N = 0, SLANTR is set to zero.

### A (in)

A is REAL array, dimension (LDA,N) The trapezoidal matrix A (A is triangular if M = N). If UPLO = 'U', the leading m by n upper trapezoidal part of the array A contains the upper trapezoidal matrix, and the strictly lower triangular part of A is not referenced. If UPLO = 'L', the leading m by n lower trapezoidal part of the array A contains the lower trapezoidal matrix, and the strictly upper triangular part of A is not referenced. Note that when DIAG = 'U', the diagonal elements of A are not referenced and are assumed to be one.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(M,1).

### WORK (out)

WORK is REAL array, dimension (MAX(1,LWORK)), where LWORK >= M when NORM = 'I'; otherwise, WORK is not referenced.

