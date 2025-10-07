# CLARFX

## Function Signature

```fortran
CLARFX(SIDE, M, N, V, TAU, C, LDC, WORK)
```

## Description


 CLARFX applies a complex elementary reflector H to a complex m by n
 matrix C, from either the left or the right. H is represented in the
 form

       H = I - tau * v * v**H

 where tau is a complex scalar and v is a complex vector.

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

V is COMPLEX array, dimension (M) if SIDE = 'L' or (N) if SIDE = 'R' The vector v in the representation of H.

### TAU (in)

TAU is COMPLEX The value tau in the representation of H.

### C (in,out)

C is COMPLEX array, dimension (LDC,N) On entry, the m by n matrix C. On exit, C is overwritten by the matrix H * C if SIDE = 'L', or C * H if SIDE = 'R'.

### LDC (in)

LDC is INTEGER The leading dimension of the array C. LDC >= max(1,M).

### WORK (out)

WORK is COMPLEX array, dimension (N) if SIDE = 'L' or (M) if SIDE = 'R' WORK is not referenced if H has order < 11.

