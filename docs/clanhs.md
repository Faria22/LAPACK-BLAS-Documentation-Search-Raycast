# CLANHS

## Function Signature

```fortran
CLANHS(NORM, N, A, LDA, WORK)
```

## Description


 CLANHS  returns the value of the one norm,  or the Frobenius norm, or
 the  infinity norm,  or the  element of  largest absolute value  of a
 Hessenberg matrix A.

## Parameters

### NORM (in)

NORM is CHARACTER*1 Specifies the value to be returned in CLANHS as described above.

### N (in)

N is INTEGER The order of the matrix A. N >= 0. When N = 0, CLANHS is set to zero.

### A (in)

A is COMPLEX array, dimension (LDA,N) The n by n upper Hessenberg matrix A; the part of A below the first sub-diagonal is not referenced.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(N,1).

### WORK (out)

WORK is REAL array, dimension (MAX(1,LWORK)), where LWORK >= N when NORM = 'I'; otherwise, WORK is not referenced.

