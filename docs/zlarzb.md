# ZLARZB

## Function Signature

```fortran
ZLARZB(SIDE, TRANS, DIRECT, STOREV, M, N, K, L, V,
*                          LDV, T, LDT, C, LDC, WORK, LDWORK)
```

## Description


 ZLARZB applies a complex block reflector H or its transpose H**H
 to a complex distributed M-by-N  C from the left or the right.

 Currently, only STOREV = 'R' and DIRECT = 'B' are supported.

## Parameters

### SIDE (in)

SIDE is CHARACTER*1 = 'L': apply H or H**H from the Left = 'R': apply H or H**H from the Right

### TRANS (in)

TRANS is CHARACTER*1 = 'N': apply H (No transpose) = 'C': apply H**H (Conjugate transpose)

### DIRECT (in)

DIRECT is CHARACTER*1 Indicates how H is formed from a product of elementary reflectors = 'F': H = H(1) H(2) . . . H(k) (Forward, not supported yet) = 'B': H = H(k) . . . H(2) H(1) (Backward)

### STOREV (in)

STOREV is CHARACTER*1 Indicates how the vectors which define the elementary reflectors are stored: = 'C': Columnwise (not supported yet) = 'R': Rowwise

### M (in)

M is INTEGER The number of rows of the matrix C.

### N (in)

N is INTEGER The number of columns of the matrix C.

### K (in)

K is INTEGER The order of the matrix T (= the number of elementary reflectors whose product defines the block reflector).

### L (in)

L is INTEGER The number of columns of the matrix V containing the meaningful part of the Householder reflectors. If SIDE = 'L', M >= L >= 0, if SIDE = 'R', N >= L >= 0.

### V (in)

V is COMPLEX*16 array, dimension (LDV,NV). If STOREV = 'C', NV = K; if STOREV = 'R', NV = L.

### LDV (in)

LDV is INTEGER The leading dimension of the array V. If STOREV = 'C', LDV >= L; if STOREV = 'R', LDV >= K.

### T (in)

T is COMPLEX*16 array, dimension (LDT,K) The triangular K-by-K matrix T in the representation of the block reflector.

### LDT (in)

LDT is INTEGER The leading dimension of the array T. LDT >= K.

### C (in,out)

C is COMPLEX*16 array, dimension (LDC,N) On entry, the M-by-N matrix C. On exit, C is overwritten by H*C or H**H*C or C*H or C*H**H.

### LDC (in)

LDC is INTEGER The leading dimension of the array C. LDC >= max(1,M).

### WORK (out)

WORK is COMPLEX*16 array, dimension (LDWORK,K)

### LDWORK (in)

LDWORK is INTEGER The leading dimension of the array WORK. If SIDE = 'L', LDWORK >= max(1,N); if SIDE = 'R', LDWORK >= max(1,M).

