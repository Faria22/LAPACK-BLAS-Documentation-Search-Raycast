# CTPMQRT

## Function Signature

```fortran
CTPMQRT(SIDE, TRANS, M, N, K, L, NB, V, LDV, T, LDT,
*                           A, LDA, B, LDB, WORK, INFO)
```

## Description


 CTPMQRT applies a complex orthogonal matrix Q obtained from a
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

### NB (in)

NB is INTEGER The block size used for the storage of T. K >= NB >= 1. This must be the same value of NB used to generate T in CTPQRT.

### V (in)

V is COMPLEX array, dimension (LDV,K) The i-th column must contain the vector which defines the elementary reflector H(i), for i = 1,2,...,k, as returned by CTPQRT in B. See Further Details.

### LDV (in)

LDV is INTEGER The leading dimension of the array V. If SIDE = 'L', LDV >= max(1,M); if SIDE = 'R', LDV >= max(1,N).

### T (in)

T is COMPLEX array, dimension (LDT,K) The upper triangular factors of the block reflectors as returned by CTPQRT, stored as a NB-by-K matrix.

### LDT (in)

LDT is INTEGER The leading dimension of the array T. LDT >= NB.

### A (in,out)

A is COMPLEX array, dimension (LDA,N) if SIDE = 'L' or (LDA,K) if SIDE = 'R' On entry, the K-by-N or M-by-K matrix A. On exit, A is overwritten by the corresponding block of Q*C or Q**H*C or C*Q or C*Q**H. See Further Details.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. If SIDE = 'L', LDC >= max(1,K); If SIDE = 'R', LDC >= max(1,M).

### B (in,out)

B is COMPLEX array, dimension (LDB,N) On entry, the M-by-N matrix B. On exit, B is overwritten by the corresponding block of Q*C or Q**H*C or C*Q or C*Q**H. See Further Details.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,M).

### WORK (out)

WORK is COMPLEX array. The dimension of WORK is N*NB if SIDE = 'L', or M*NB if SIDE = 'R'.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

