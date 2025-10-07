# SLAG2D

## Function Signature

```fortran
SLAG2D(M, N, SA, LDSA, A, LDA, INFO)
```

## Description


 SLAG2D converts a SINGLE PRECISION matrix, SA, to a DOUBLE
 PRECISION matrix, A.

 Note that while it is possible to overflow while converting
 from double to single, it is not possible to overflow when
 converting from single to double.

 This is an auxiliary routine so there is no argument checking.

## Parameters

### M (in)

M is INTEGER The number of lines of the matrix A. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix A. N >= 0.

### SA (in)

SA is REAL array, dimension (LDSA,N) On entry, the M-by-N coefficient matrix SA.

### LDSA (in)

LDSA is INTEGER The leading dimension of the array SA. LDSA >= max(1,M).

### A (out)

A is DOUBLE PRECISION array, dimension (LDA,N) On exit, the M-by-N coefficient matrix A.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,M).

### INFO (out)

INFO is INTEGER = 0: successful exit

