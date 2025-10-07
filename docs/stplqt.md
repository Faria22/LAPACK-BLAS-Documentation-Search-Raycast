# STPLQT

## Function Signature

```fortran
STPLQT(M, N, L, MB, A, LDA, B, LDB, T, LDT, WORK,
*                          INFO)
```

## Description


 STPLQT computes a blocked LQ factorization of a real
 "triangular-pentagonal" matrix C, which is composed of a
 triangular block A and pentagonal block B, using the compact
 WY representation for Q.

## Parameters

### M (in)

M is INTEGER The number of rows of the matrix B, and the order of the triangular matrix A. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix B. N >= 0.

### L (in)

L is INTEGER The number of rows of the lower trapezoidal part of B. MIN(M,N) >= L >= 0. See Further Details.

### MB (in)

MB is INTEGER The block size to be used in the blocked QR. M >= MB >= 1.

### A (in,out)

A is REAL array, dimension (LDA,M) On entry, the lower triangular M-by-M matrix A. On exit, the elements on and below the diagonal of the array contain the lower triangular matrix L.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,M).

### B (in,out)

B is REAL array, dimension (LDB,N) On entry, the pentagonal M-by-N matrix B. The first N-L columns are rectangular, and the last L columns are lower trapezoidal. On exit, B contains the pentagonal matrix V. See Further Details.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,M).

### T (out)

T is REAL array, dimension (LDT,N) The lower triangular block reflectors stored in compact form as a sequence of upper triangular blocks. See Further Details.

### LDT (in)

LDT is INTEGER The leading dimension of the array T. LDT >= MB.

### WORK (out)

WORK is REAL array, dimension (MB*M)

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

