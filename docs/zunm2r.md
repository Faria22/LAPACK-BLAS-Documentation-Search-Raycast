# ZUNM2R

## Function Signature

```fortran
ZUNM2R(SIDE, TRANS, M, N, K, A, LDA, TAU, C, LDC,
*                          WORK, INFO)
```

## Description


 ZUNM2R overwrites the general complex m-by-n matrix C with

       Q * C  if SIDE = 'L' and TRANS = 'N', or

       Q**H* C  if SIDE = 'L' and TRANS = 'C', or

       C * Q  if SIDE = 'R' and TRANS = 'N', or

       C * Q**H if SIDE = 'R' and TRANS = 'C',

 where Q is a complex unitary matrix defined as the product of k
 elementary reflectors

       Q = H(1) H(2) . . . H(k)

 as returned by ZGEQRF. Q is of order m if SIDE = 'L' and of order n
 if SIDE = 'R'.

## Parameters

### SIDE (in)

SIDE is CHARACTER*1 = 'L': apply Q or Q**H from the Left = 'R': apply Q or Q**H from the Right

### TRANS (in)

TRANS is CHARACTER*1 = 'N': apply Q (No transpose) = 'C': apply Q**H (Conjugate transpose)

### M (in)

M is INTEGER The number of rows of the matrix C. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix C. N >= 0.

### K (in)

K is INTEGER The number of elementary reflectors whose product defines the matrix Q. If SIDE = 'L', M >= K >= 0; if SIDE = 'R', N >= K >= 0.

### A (in)

A is COMPLEX*16 array, dimension (LDA,K) The i-th column must contain the vector which defines the elementary reflector H(i), for i = 1,2,...,k, as returned by ZGEQRF in the first k columns of its array argument A. A is modified by the routine but restored on exit.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. If SIDE = 'L', LDA >= max(1,M); if SIDE = 'R', LDA >= max(1,N).

### TAU (in)

TAU is COMPLEX*16 array, dimension (K) TAU(i) must contain the scalar factor of the elementary reflector H(i), as returned by ZGEQRF.

### C (in,out)

C is COMPLEX*16 array, dimension (LDC,N) On entry, the m-by-n matrix C. On exit, C is overwritten by Q*C or Q**H*C or C*Q**H or C*Q.

### LDC (in)

LDC is INTEGER The leading dimension of the array C. LDC >= max(1,M).

### WORK (out)

WORK is COMPLEX*16 array, dimension (N) if SIDE = 'L', (M) if SIDE = 'R'

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

