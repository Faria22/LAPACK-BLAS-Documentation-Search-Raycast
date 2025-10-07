# ZLACRM

## Function Signature

```fortran
ZLACRM(M, N, A, LDA, B, LDB, C, LDC, RWORK)
```

## Description


 ZLACRM performs a very simple matrix-matrix multiplication:
          C := A * B,
 where A is M by N and complex; B is N by N and real;
 C is M by N and complex.

## Parameters

### M (in)

M is INTEGER The number of rows of the matrix A and of the matrix C. M >= 0.

### N (in)

N is INTEGER The number of columns and rows of the matrix B and the number of columns of the matrix C. N >= 0.

### A (in)

A is COMPLEX*16 array, dimension (LDA, N) On entry, A contains the M by N matrix A.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >=max(1,M).

### B (in)

B is DOUBLE PRECISION array, dimension (LDB, N) On entry, B contains the N by N matrix B.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >=max(1,N).

### C (out)

C is COMPLEX*16 array, dimension (LDC, N) On exit, C contains the M by N matrix C.

### LDC (in)

LDC is INTEGER The leading dimension of the array C. LDC >=max(1,N).

### RWORK (out)

RWORK is DOUBLE PRECISION array, dimension (2*M*N)

