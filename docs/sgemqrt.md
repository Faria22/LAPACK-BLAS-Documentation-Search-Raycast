# SGEMQRT

## Function Signature

```fortran
SGEMQRT(SIDE, TRANS, M, N, K, NB, V, LDV, T, LDT,
*                          C, LDC, WORK, INFO)
```

## Description


 SGEMQRT overwrites the general real M-by-N matrix C with

                 SIDE = 'L'     SIDE = 'R'
 TRANS = 'N':      Q C            C Q
 TRANS = 'T':   Q**T C            C Q**T

 where Q is a real orthogonal matrix defined as the product of K
 elementary reflectors:

       Q = H(1) H(2) . . . H(K) = I - V T V**T

 generated using the compact WY representation as returned by SGEQRT.

 Q is of order M if SIDE = 'L' and of order N  if SIDE = 'R'.

## Parameters

### SIDE (in)

SIDE is CHARACTER*1 = 'L': apply Q or Q**T from the Left; = 'R': apply Q or Q**T from the Right.

### TRANS (in)

TRANS is CHARACTER*1 = 'N': No transpose, apply Q; = 'T': Transpose, apply Q**T.

### M (in)

M is INTEGER The number of rows of the matrix C. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix C. N >= 0.

### K (in)

K is INTEGER The number of elementary reflectors whose product defines the matrix Q. If SIDE = 'L', M >= K >= 0; if SIDE = 'R', N >= K >= 0.

### NB (in)

NB is INTEGER The block size used for the storage of T. K >= NB >= 1. This must be the same value of NB used to generate T in SGEQRT.

### V (in)

V is REAL array, dimension (LDV,K) The i-th column must contain the vector which defines the elementary reflector H(i), for i = 1,2,...,k, as returned by SGEQRT in the first K columns of its array argument A.

### LDV (in)

LDV is INTEGER The leading dimension of the array V. If SIDE = 'L', LDA >= max(1,M); if SIDE = 'R', LDA >= max(1,N).

### T (in)

T is REAL array, dimension (LDT,K) The upper triangular factors of the block reflectors as returned by SGEQRT, stored as a NB-by-N matrix.

### LDT (in)

LDT is INTEGER The leading dimension of the array T. LDT >= NB.

### C (in,out)

C is REAL array, dimension (LDC,N) On entry, the M-by-N matrix C. On exit, C is overwritten by Q C, Q**T C, C Q**T or C Q.

### LDC (in)

LDC is INTEGER The leading dimension of the array C. LDC >= max(1,M).

### WORK (out)

WORK is REAL array. The dimension of WORK is N*NB if SIDE = 'L', or M*NB if SIDE = 'R'.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

