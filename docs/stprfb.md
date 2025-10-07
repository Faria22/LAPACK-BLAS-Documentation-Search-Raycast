# STPRFB

## Function Signature

```fortran
STPRFB(SIDE, TRANS, DIRECT, STOREV, M, N, K, L,
*                          V, LDV, T, LDT, A, LDA, B, LDB, WORK, LDWORK)
```

## Description


 STPRFB applies a real "triangular-pentagonal" block reflector H or its
 transpose H**T to a real matrix C, which is composed of two
 blocks A and B, either from the left or right.


## Parameters

### SIDE (in)

SIDE is CHARACTER*1 = 'L': apply H or H**T from the Left = 'R': apply H or H**T from the Right

### TRANS (in)

TRANS is CHARACTER*1 = 'N': apply H (No transpose) = 'T': apply H**T (Transpose)

### DIRECT (in)

DIRECT is CHARACTER*1 Indicates how H is formed from a product of elementary reflectors = 'F': H = H(1) H(2) . . . H(k) (Forward) = 'B': H = H(k) . . . H(2) H(1) (Backward)

### STOREV (in)

STOREV is CHARACTER*1 Indicates how the vectors which define the elementary reflectors are stored: = 'C': Columns = 'R': Rows

### M (in)

M is INTEGER The number of rows of the matrix B. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix B. N >= 0.

### K (in)

K is INTEGER The order of the matrix T, i.e. the number of elementary reflectors whose product defines the block reflector. K >= 0.

### L (in)

L is INTEGER The order of the trapezoidal part of V. K >= L >= 0. See Further Details.

### V (in)

V is REAL array, dimension (LDV,K) if STOREV = 'C' (LDV,M) if STOREV = 'R' and SIDE = 'L' (LDV,N) if STOREV = 'R' and SIDE = 'R' The pentagonal matrix V, which contains the elementary reflectors H(1), H(2), ..., H(K). See Further Details.

### LDV (in)

LDV is INTEGER The leading dimension of the array V. If STOREV = 'C' and SIDE = 'L', LDV >= max(1,M); if STOREV = 'C' and SIDE = 'R', LDV >= max(1,N); if STOREV = 'R', LDV >= K.

### T (in)

T is REAL array, dimension (LDT,K) The triangular K-by-K matrix T in the representation of the block reflector.

### LDT (in)

LDT is INTEGER The leading dimension of the array T. LDT >= K.

### A (in,out)

A is REAL array, dimension (LDA,N) if SIDE = 'L' or (LDA,K) if SIDE = 'R' On entry, the K-by-N or M-by-K matrix A. On exit, A is overwritten by the corresponding block of H*C or H**T*C or C*H or C*H**T. See Further Details.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. If SIDE = 'L', LDA >= max(1,K); If SIDE = 'R', LDA >= max(1,M).

### B (in,out)

B is REAL array, dimension (LDB,N) On entry, the M-by-N matrix B. On exit, B is overwritten by the corresponding block of H*C or H**T*C or C*H or C*H**T. See Further Details.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,M).

### WORK (out)

WORK is REAL array, dimension (LDWORK,N) if SIDE = 'L', (LDWORK,K) if SIDE = 'R'.

### LDWORK (in)

LDWORK is INTEGER The leading dimension of the array WORK. If SIDE = 'L', LDWORK >= K; if SIDE = 'R', LDWORK >= M.

