# ZLACPY

## Function Signature

```fortran
ZLACPY(UPLO, M, N, A, LDA, B, LDB)
```

## Description


 ZLACPY copies all or part of a two-dimensional matrix A to another
 matrix B.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 Specifies the part of the matrix A to be copied to B. = 'U': Upper triangular part = 'L': Lower triangular part Otherwise: All of the matrix A

### M (in)

M is INTEGER The number of rows of the matrix A. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix A. N >= 0.

### A (in)

A is COMPLEX*16 array, dimension (LDA,N) The m by n matrix A. If UPLO = 'U', only the upper trapezium is accessed; if UPLO = 'L', only the lower trapezium is accessed.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,M).

### B (out)

B is COMPLEX*16 array, dimension (LDB,N) On exit, B = A in the locations specified by UPLO.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,M).

