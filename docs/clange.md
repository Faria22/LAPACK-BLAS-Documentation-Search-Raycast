# CLANGE

## Function Signature

```fortran
CLANGE(NORM, M, N, A, LDA, WORK)
```

## Description


 CLANGE  returns the value of the one norm,  or the Frobenius norm, or
 the  infinity norm,  or the  element of  largest absolute value  of a
 complex matrix A.

## Parameters

### NORM (in)

NORM is CHARACTER*1 Specifies the value to be returned in CLANGE as described above.

### M (in)

M is INTEGER The number of rows of the matrix A. M >= 0. When M = 0, CLANGE is set to zero.

### N (in)

N is INTEGER The number of columns of the matrix A. N >= 0. When N = 0, CLANGE is set to zero.

### A (in)

A is COMPLEX array, dimension (LDA,N) The m by n matrix A.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(M,1).

### WORK (out)

WORK is REAL array, dimension (MAX(1,LWORK)), where LWORK >= M when NORM = 'I'; otherwise, WORK is not referenced.

