# DLAG2S

## Function Signature

```fortran
DLAG2S(M, N, A, LDA, SA, LDSA, INFO)
```

## Description


 DLAG2S converts a DOUBLE PRECISION matrix, A, to a SINGLE
 PRECISION matrix, SA.

 RMAX is the overflow for the SINGLE PRECISION arithmetic
 DLAG2S checks that all the entries of A are between -RMAX and
 RMAX. If not the conversion is aborted and a flag is raised.

 This is an auxiliary routine so there is no argument checking.

## Parameters

### M (in)

M is INTEGER The number of lines of the matrix A. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix A. N >= 0.

### A (in)

A is DOUBLE PRECISION array, dimension (LDA,N) On entry, the M-by-N coefficient matrix A.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,M).

### SA (out)

SA is REAL array, dimension (LDSA,N) On exit, if INFO=0, the M-by-N coefficient matrix SA; if INFO>0, the content of SA is unspecified.

### LDSA (in)

LDSA is INTEGER The leading dimension of the array SA. LDSA >= max(1,M).

### INFO (out)

INFO is INTEGER = 0: successful exit. = 1: an entry of the matrix A is greater than the SINGLE PRECISION overflow threshold, in this case, the content of SA in exit is unspecified.

