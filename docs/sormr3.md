# SORMR3

## Function Signature

```fortran
SORMR3(SIDE, TRANS, M, N, K, L, A, LDA, TAU, C, LDC,
*                          WORK, INFO)
```

## Description


 SORMR3 overwrites the general real m by n matrix C with

       Q * C  if SIDE = 'L' and TRANS = 'N', or

       Q**T* C  if SIDE = 'L' and TRANS = 'C', or

       C * Q  if SIDE = 'R' and TRANS = 'N', or

       C * Q**T if SIDE = 'R' and TRANS = 'C',

 where Q is a real orthogonal matrix defined as the product of k
 elementary reflectors

       Q = H(1) H(2) . . . H(k)

 as returned by STZRZF. Q is of order m if SIDE = 'L' and of order n
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

### L (in)

L is INTEGER The number of columns of the matrix A containing the meaningful part of the Householder reflectors. If SIDE = 'L', M >= L >= 0, if SIDE = 'R', N >= L >= 0.

### A (in)

A is REAL array, dimension (LDA,M) if SIDE = 'L', (LDA,N) if SIDE = 'R' The i-th row must contain the vector which defines the elementary reflector H(i), for i = 1,2,...,k, as returned by STZRZF in the last k rows of its array argument A. A is modified by the routine but restored on exit.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,K).

### TAU (in)

TAU is REAL array, dimension (K) TAU(i) must contain the scalar factor of the elementary reflector H(i), as returned by STZRZF.

### C (in,out)

C is REAL array, dimension (LDC,N) On entry, the m-by-n matrix C. On exit, C is overwritten by Q*C or Q**T*C or C*Q**T or C*Q.

### LDC (in)

LDC is INTEGER The leading dimension of the array C. LDC >= max(1,M).

### WORK (out)

WORK is REAL array, dimension (N) if SIDE = 'L', (M) if SIDE = 'R'

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

