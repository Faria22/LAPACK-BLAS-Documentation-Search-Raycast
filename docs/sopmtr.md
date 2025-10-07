# SOPMTR

## Function Signature

```fortran
SOPMTR(SIDE, UPLO, TRANS, M, N, AP, TAU, C, LDC, WORK,
*                          INFO)
```

## Description


 SOPMTR overwrites the general real M-by-N matrix C with

                 SIDE = 'L'     SIDE = 'R'
 TRANS = 'N':      Q * C          C * Q
 TRANS = 'T':      Q**T * C       C * Q**T

 where Q is a real orthogonal matrix of order nq, with nq = m if
 SIDE = 'L' and nq = n if SIDE = 'R'. Q is defined as the product of
 nq-1 elementary reflectors, as returned by SSPTRD using packed
 storage:

 if UPLO = 'U', Q = H(nq-1) . . . H(2) H(1);

 if UPLO = 'L', Q = H(1) H(2) . . . H(nq-1).

## Parameters

### SIDE (in)

SIDE is CHARACTER*1 = 'L': apply Q or Q**T from the Left; = 'R': apply Q or Q**T from the Right.

### UPLO (in)

UPLO is CHARACTER*1 = 'U': Upper triangular packed storage used in previous call to SSPTRD; = 'L': Lower triangular packed storage used in previous call to SSPTRD.

### TRANS (in)

TRANS is CHARACTER*1 = 'N': No transpose, apply Q; = 'T': Transpose, apply Q**T.

### M (in)

M is INTEGER The number of rows of the matrix C. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix C. N >= 0.

### AP (in)

AP is REAL array, dimension (M*(M+1)/2) if SIDE = 'L' (N*(N+1)/2) if SIDE = 'R' The vectors which define the elementary reflectors, as returned by SSPTRD. AP is modified by the routine but restored on exit.

### TAU (in)

TAU is REAL array, dimension (M-1) if SIDE = 'L' or (N-1) if SIDE = 'R' TAU(i) must contain the scalar factor of the elementary reflector H(i), as returned by SSPTRD.

### C (in,out)

C is REAL array, dimension (LDC,N) On entry, the M-by-N matrix C. On exit, C is overwritten by Q*C or Q**T*C or C*Q**T or C*Q.

### LDC (in)

LDC is INTEGER The leading dimension of the array C. LDC >= max(1,M).

### WORK (out)

WORK is REAL array, dimension (N) if SIDE = 'L' (M) if SIDE = 'R'

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

