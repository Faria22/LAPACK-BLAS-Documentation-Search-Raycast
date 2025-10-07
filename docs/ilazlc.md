# ILAZLC

## Function Signature

```fortran
ILAZLC(M, N, A, LDA)
```

## Description


 ILAZLC scans A for its last non-zero column.

## Parameters

### M (in)

M is INTEGER The number of rows of the matrix A.

### N (in)

N is INTEGER The number of columns of the matrix A.

### A (in)

A is COMPLEX*16 array, dimension (LDA,N) The m by n matrix A.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,M).

