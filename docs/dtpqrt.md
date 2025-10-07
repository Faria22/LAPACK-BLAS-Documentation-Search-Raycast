# DTPQRT

## Function Signature

```fortran
DTPQRT(M, N, L, NB, A, LDA, B, LDB, T, LDT, WORK,
*                          INFO)
```

## Description


 DTPQRT computes a blocked QR factorization of a real
 "triangular-pentagonal" matrix C, which is composed of a
 triangular block A and pentagonal block B, using the compact
 WY representation for Q.

## Parameters

### M (in)

M is INTEGER The number of rows of the matrix B. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix B, and the order of the triangular matrix A. N >= 0.

### L (in)

L is INTEGER The number of rows of the upper trapezoidal part of B. MIN(M,N) >= L >= 0. See Further Details.

### NB (in)

NB is INTEGER The block size to be used in the blocked QR. N >= NB >= 1.

### A (in,out)

A is DOUBLE PRECISION array, dimension (LDA,N) On entry, the upper triangular N-by-N matrix A. On exit, the elements on and above the diagonal of the array contain the upper triangular matrix R.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### B (in,out)

B is DOUBLE PRECISION array, dimension (LDB,N) On entry, the pentagonal M-by-N matrix B. The first M-L rows are rectangular, and the last L rows are upper trapezoidal. On exit, B contains the pentagonal matrix V. See Further Details.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,M).

### T (out)

T is DOUBLE PRECISION array, dimension (LDT,N) The upper triangular block reflectors stored in compact form as a sequence of upper triangular blocks. See Further Details.

### LDT (in)

LDT is INTEGER The leading dimension of the array T. LDT >= NB.

### WORK (out)

WORK is DOUBLE PRECISION array, dimension (NB*N)

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

