# SLARZ

## Function Signature

```fortran
SLARZ(SIDE, M, N, L, V, INCV, TAU, C, LDC, WORK)
```

## Description


 SLARZ applies a real elementary reflector H to a real M-by-N
 matrix C, from either the left or the right. H is represented in the
 form

       H = I - tau * v * v**T

 where tau is a real scalar and v is a real vector.

 If tau = 0, then H is taken to be the unit matrix.


 H is a product of k elementary reflectors as returned by STZRZF.

## Parameters

### SIDE (in)

SIDE is CHARACTER*1 = 'L': form H * C = 'R': form C * H

### M (in)

M is INTEGER The number of rows of the matrix C.

### N (in)

N is INTEGER The number of columns of the matrix C.

### L (in)

L is INTEGER The number of entries of the vector V containing the meaningful part of the Householder vectors. If SIDE = 'L', M >= L >= 0, if SIDE = 'R', N >= L >= 0.

### V (in)

V is REAL array, dimension (1+(L-1)*abs(INCV)) The vector v in the representation of H as returned by STZRZF. V is not used if TAU = 0.

### INCV (in)

INCV is INTEGER The increment between elements of v. INCV <> 0.

### TAU (in)

TAU is REAL The value tau in the representation of H.

### C (in,out)

C is REAL array, dimension (LDC,N) On entry, the M-by-N matrix C. On exit, C is overwritten by the matrix H * C if SIDE = 'L', or C * H if SIDE = 'R'.

### LDC (in)

LDC is INTEGER The leading dimension of the array C. LDC >= max(1,M).

### WORK (out)

WORK is REAL array, dimension (N) if SIDE = 'L' or (M) if SIDE = 'R'

