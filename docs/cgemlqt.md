# CGEMLQT

## Function Signature

```fortran
CGEMLQT(SIDE, TRANS, M, N, K, MB, V, LDV, T, LDT,
*                          C, LDC, WORK, INFO)
```

## Description


 CGEMLQT overwrites the general complex M-by-N matrix C with

                 SIDE = 'L'     SIDE = 'R'
 TRANS = 'N':      Q C            C Q
 TRANS = 'C':   Q**H C            C Q**H

 where Q is a complex unitary matrix defined as the product of K
 elementary reflectors:

       Q = H(1) H(2) . . . H(K) = I - V T V**H

 generated using the compact WY representation as returned by CGELQT.

 Q is of order M if SIDE = 'L' and of order N  if SIDE = 'R'.

## Parameters

### SIDE (in)

SIDE is CHARACTER*1 = 'L': apply Q or Q**H from the Left; = 'R': apply Q or Q**H from the Right.

### TRANS (in)

TRANS is CHARACTER*1 = 'N': No transpose, apply Q; = 'C': Conjugate transpose, apply Q**H.

### M (in)

M is INTEGER The number of rows of the matrix C. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix C. N >= 0.

### K (in)

K is INTEGER The number of elementary reflectors whose product defines the matrix Q. If SIDE = 'L', M >= K >= 0; if SIDE = 'R', N >= K >= 0.

### MB (in)

MB is INTEGER The block size used for the storage of T. K >= MB >= 1. This must be the same value of MB used to generate T in CGELQT.

### V (in)

V is COMPLEX array, dimension (LDV,M) if SIDE = 'L', (LDV,N) if SIDE = 'R' The i-th row must contain the vector which defines the elementary reflector H(i), for i = 1,2,...,k, as returned by CGELQT in the first K rows of its array argument A.

### LDV (in)

LDV is INTEGER The leading dimension of the array V. LDV >= max(1,K).

### T (in)

T is COMPLEX array, dimension (LDT,K) The upper triangular factors of the block reflectors as returned by CGELQT, stored as a MB-by-K matrix.

### LDT (in)

LDT is INTEGER The leading dimension of the array T. LDT >= MB.

### C (in,out)

C is COMPLEX array, dimension (LDC,N) On entry, the M-by-N matrix C. On exit, C is overwritten by Q C, Q**H C, C Q**H or C Q.

### LDC (in)

LDC is INTEGER The leading dimension of the array C. LDC >= max(1,M).

### WORK (out)

WORK is COMPLEX array. The dimension of WORK is N*MB if SIDE = 'L', or M*MB if SIDE = 'R'.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

