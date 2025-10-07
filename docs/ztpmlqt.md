# ZTPMLQT

## Function Signature

```fortran
ZTPMLQT(SIDE, TRANS, M, N, K, L, MB, V, LDV, T, LDT,
*                           A, LDA, B, LDB, WORK, INFO)
```

## Description


 ZTPMLQT applies a complex unitary matrix Q obtained from a
 "triangular-pentagonal" complex block reflector H to a general
 complex matrix C, which consists of two blocks A and B.

## Parameters

### SIDE (in)

SIDE is CHARACTER*1 = 'L': apply Q or Q**H from the Left; = 'R': apply Q or Q**H from the Right.

### TRANS (in)

TRANS is CHARACTER*1 = 'N': No transpose, apply Q; = 'C': Conjugate transpose, apply Q**H.

### M (in)

M is INTEGER The number of rows of the matrix B. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix B. N >= 0.

### K (in)

K is INTEGER The number of elementary reflectors whose product defines the matrix Q.

### L (in)

L is INTEGER The order of the trapezoidal part of V. K >= L >= 0. See Further Details.

### MB (in)

MB is INTEGER The block size used for the storage of T. K >= MB >= 1. This must be the same value of MB used to generate T in ZTPLQT.

### V (in)

V is COMPLEX*16 array, dimension (LDV,K) The i-th row must contain the vector which defines the elementary reflector H(i), for i = 1,2,...,k, as returned by ZTPLQT in B. See Further Details.

### LDV (in)

LDV is INTEGER The leading dimension of the array V. LDV >= K.

### T (in)

T is COMPLEX*16 array, dimension (LDT,K) The upper triangular factors of the block reflectors as returned by ZTPLQT, stored as a MB-by-K matrix.

### LDT (in)

LDT is INTEGER The leading dimension of the array T. LDT >= MB.

### A (in,out)

A is COMPLEX*16 array, dimension (LDA,N) if SIDE = 'L' or (LDA,K) if SIDE = 'R' On entry, the K-by-N or M-by-K matrix A. On exit, A is overwritten by the corresponding block of Q*C or Q**H*C or C*Q or C*Q**H. See Further Details.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. If SIDE = 'L', LDA >= max(1,K); If SIDE = 'R', LDA >= max(1,M).

### B (in,out)

B is COMPLEX*16 array, dimension (LDB,N) On entry, the M-by-N matrix B. On exit, B is overwritten by the corresponding block of Q*C or Q**H*C or C*Q or C*Q**H. See Further Details.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,M).

### WORK (out)

WORK is COMPLEX*16 array. The dimension of WORK is N*MB if SIDE = 'L', or M*MB if SIDE = 'R'.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

