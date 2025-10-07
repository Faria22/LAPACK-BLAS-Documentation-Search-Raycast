# ZTPLQT2

## Function Signature

```fortran
ZTPLQT2(M, N, L, A, LDA, B, LDB, T, LDT, INFO)
```

## Description


 ZTPLQT2 computes a LQ a factorization of a complex "triangular-pentagonal"
 matrix C, which is composed of a triangular block A and pentagonal block B,
 using the compact WY representation for Q.

## Parameters

### M (in)

M is INTEGER The total number of rows of the matrix B. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix B, and the order of the triangular matrix A. N >= 0.

### L (in)

L is INTEGER The number of rows of the lower trapezoidal part of B. MIN(M,N) >= L >= 0. See Further Details.

### A (in,out)

A is COMPLEX*16 array, dimension (LDA,M) On entry, the lower triangular M-by-M matrix A. On exit, the elements on and below the diagonal of the array contain the lower triangular matrix L.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,M).

### B (in,out)

B is COMPLEX*16 array, dimension (LDB,N) On entry, the pentagonal M-by-N matrix B. The first N-L columns are rectangular, and the last L columns are lower trapezoidal. On exit, B contains the pentagonal matrix V. See Further Details.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,M).

### T (out)

T is COMPLEX*16 array, dimension (LDT,M) The N-by-N upper triangular factor T of the block reflector. See Further Details.

### LDT (in)

LDT is INTEGER The leading dimension of the array T. LDT >= max(1,M)

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

