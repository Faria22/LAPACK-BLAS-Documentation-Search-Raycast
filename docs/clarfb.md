# CLARFB

## Function Signature

```fortran
CLARFB(SIDE, TRANS, DIRECT, STOREV, M, N, K, V, LDV,
*                          T, LDT, C, LDC, WORK, LDWORK)
```

## Description


 CLARFB applies a complex block reflector H or its transpose H**H to a
 complex M-by-N matrix C, from either the left or the right.

## Parameters

### SIDE (in)

SIDE is CHARACTER*1 = 'L': apply H or H**H from the Left = 'R': apply H or H**H from the Right

### TRANS (in)

TRANS is CHARACTER*1 = 'N': apply H (No transpose) = 'C': apply H**H (Conjugate transpose)

### DIRECT (in)

DIRECT is CHARACTER*1 Indicates how H is formed from a product of elementary reflectors = 'F': H = H(1) H(2) . . . H(k) (Forward) = 'B': H = H(k) . . . H(2) H(1) (Backward)

### STOREV (in)

STOREV is CHARACTER*1 Indicates how the vectors which define the elementary reflectors are stored: = 'C': Columnwise = 'R': Rowwise

### M (in)

M is INTEGER The number of rows of the matrix C.

### N (in)

N is INTEGER The number of columns of the matrix C.

### K (in)

K is INTEGER The order of the matrix T (= the number of elementary reflectors whose product defines the block reflector). If SIDE = 'L', M >= K >= 0; if SIDE = 'R', N >= K >= 0.

### V (in)

V is COMPLEX array, dimension (LDV,K) if STOREV = 'C' (LDV,M) if STOREV = 'R' and SIDE = 'L' (LDV,N) if STOREV = 'R' and SIDE = 'R' The matrix V. See Further Details.

### LDV (in)

LDV is INTEGER The leading dimension of the array V. If STOREV = 'C' and SIDE = 'L', LDV >= max(1,M); if STOREV = 'C' and SIDE = 'R', LDV >= max(1,N); if STOREV = 'R', LDV >= K.

### T (in)

T is COMPLEX array, dimension (LDT,K) The triangular K-by-K matrix T in the representation of the block reflector.

### LDT (in)

LDT is INTEGER The leading dimension of the array T. LDT >= K.

### C (in,out)

C is COMPLEX array, dimension (LDC,N) On entry, the M-by-N matrix C. On exit, C is overwritten by H*C or H**H*C or C*H or C*H**H.

### LDC (in)

LDC is INTEGER The leading dimension of the array C. LDC >= max(1,M).

### WORK (out)

WORK is COMPLEX array, dimension (LDWORK,K)

### LDWORK (in)

LDWORK is INTEGER The leading dimension of the array WORK. If SIDE = 'L', LDWORK >= max(1,N); if SIDE = 'R', LDWORK >= max(1,M).

