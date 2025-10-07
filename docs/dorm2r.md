# DORM2R

## Function Signature

```fortran
DORM2R(SIDE, TRANS, M, N, K, A, LDA, TAU, C, LDC,
*                          WORK, INFO)
```

## Description


 DORM2R overwrites the general real m by n matrix C with

       Q * C  if SIDE = 'L' and TRANS = 'N', or

       Q**T* C  if SIDE = 'L' and TRANS = 'T', or

       C * Q  if SIDE = 'R' and TRANS = 'N', or

       C * Q**T if SIDE = 'R' and TRANS = 'T',

 where Q is a real orthogonal matrix defined as the product of k
 elementary reflectors

       Q = H(1) H(2) . . . H(k)

 as returned by DGEQRF. Q is of order m if SIDE = 'L' and of order n
 if SIDE = 'R'.

## Parameters

### SIDE (in)

SIDE is CHARACTER*1 = 'L': apply Q or Q**T from the Left = 'R': apply Q or Q**T from the Right

### TRANS (in)

TRANS is CHARACTER*1 = 'N': apply Q (No transpose) = 'T': apply Q**T (Transpose)

### M (in)

M is INTEGER The number of rows of the matrix C. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix C. N >= 0.

### K (in)

K is INTEGER The number of elementary reflectors whose product defines the matrix Q. If SIDE = 'L', M >= K >= 0; if SIDE = 'R', N >= K >= 0.

### A (in)

A is DOUBLE PRECISION array, dimension (LDA,K) The i-th column must contain the vector which defines the elementary reflector H(i), for i = 1,2,...,k, as returned by DGEQRF in the first k columns of its array argument A.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. If SIDE = 'L', LDA >= max(1,M); if SIDE = 'R', LDA >= max(1,N).

### TAU (in)

TAU is DOUBLE PRECISION array, dimension (K) TAU(i) must contain the scalar factor of the elementary reflector H(i), as returned by DGEQRF.

### C (in,out)

C is DOUBLE PRECISION array, dimension (LDC,N) On entry, the m by n matrix C. On exit, C is overwritten by Q*C or Q**T*C or C*Q**T or C*Q.

### LDC (in)

LDC is INTEGER The leading dimension of the array C. LDC >= max(1,M).

### WORK (out)

WORK is DOUBLE PRECISION array, dimension (N) if SIDE = 'L', (M) if SIDE = 'R'

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

