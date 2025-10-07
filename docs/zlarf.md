# ZLARF

## Function Signature

```fortran
ZLARF(SIDE, M, N, V, INCV, TAU, C, LDC, WORK)
```

## Description


 ZLARF applies a complex elementary reflector H to a complex M-by-N
 matrix C, from either the left or the right. H is represented in the
 form

       H = I - tau * v * v**H

 where tau is a complex scalar and v is a complex vector.

 If tau = 0, then H is taken to be the unit matrix.

 To apply H**H, supply conjg(tau) instead
 tau.

## Parameters

### SIDE (in)

SIDE is CHARACTER*1 = 'L': form H * C = 'R': form C * H

### M (in)

M is INTEGER The number of rows of the matrix C.

### N (in)

N is INTEGER The number of columns of the matrix C.

### V (in)

V is COMPLEX*16 array, dimension (1 + (M-1)*abs(INCV)) if SIDE = 'L' or (1 + (N-1)*abs(INCV)) if SIDE = 'R' The vector v in the representation of H. V is not used if TAU = 0.

### INCV (in)

INCV is INTEGER The increment between elements of v. INCV <> 0.

### TAU (in)

TAU is COMPLEX*16 The value tau in the representation of H.

### C (in,out)

C is COMPLEX*16 array, dimension (LDC,N) On entry, the M-by-N matrix C. On exit, C is overwritten by the matrix H * C if SIDE = 'L', or C * H if SIDE = 'R'.

### LDC (in)

LDC is INTEGER The leading dimension of the array C. LDC >= max(1,M).

### WORK (out)

WORK is COMPLEX*16 array, dimension (N) if SIDE = 'L' or (M) if SIDE = 'R'

