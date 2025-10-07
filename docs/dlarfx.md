# DLARFX

## Function Signature

```fortran
DLARFX(SIDE, M, N, V, TAU, C, LDC, WORK)
```

## Description


 DLARFX applies a real elementary reflector H to a real m by n
 matrix C, from either the left or the right. H is represented in the
 form

       H = I - tau * v * v**T

 where tau is a real scalar and v is a real vector.

 If tau = 0, then H is taken to be the unit matrix

 This version uses inline code if H has order < 11.

## Parameters

### SIDE (in)

SIDE is CHARACTER*1 = 'L': form H * C = 'R': form C * H

### M (in)

M is INTEGER The number of rows of the matrix C.

### N (in)

N is INTEGER The number of columns of the matrix C.

### V (in)

V is DOUBLE PRECISION array, dimension (M) if SIDE = 'L' or (N) if SIDE = 'R' The vector v in the representation of H.

### TAU (in)

TAU is DOUBLE PRECISION The value tau in the representation of H.

### C (in,out)

C is DOUBLE PRECISION array, dimension (LDC,N) On entry, the m by n matrix C. On exit, C is overwritten by the matrix H * C if SIDE = 'L', or C * H if SIDE = 'R'.

### LDC (in)

LDC is INTEGER The leading dimension of the array C. LDC >= (1,M).

### WORK (out)

WORK is DOUBLE PRECISION array, dimension (N) if SIDE = 'L' or (M) if SIDE = 'R' WORK is not referenced if H has order < 11.

