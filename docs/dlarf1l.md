# DLARF1L

## Function Signature

```fortran
DLARF1L(SIDE, M, N, V, INCV, TAU, C, LDC, WORK)
```

## Description


 DLARF1L applies a real elementary reflector H to a real m by n matrix
 C, from either the left or the right. H is represented in the form

       H = I - tau * v * v**T

 where tau is a real scalar and v is a real vector.

 If tau = 0, then H is taken to be the unit matrix.

## Parameters

### SIDE (in)

SIDE is CHARACTER*1 = 'L': form H * C = 'R': form C * H

### M (in)

M is INTEGER The number of rows of the matrix C.

### N (in)

N is INTEGER The number of columns of the matrix C.

### V (in)

V is DOUBLE PRECISION array, dimension (1 + (M-1)*abs(INCV)) if SIDE = 'L' or (1 + (N-1)*abs(INCV)) if SIDE = 'R' The vector v in the representation of H. V is not used if TAU = 0.

### INCV (in)

INCV is INTEGER The increment between elements of v. INCV <> 0.

### TAU (in)

TAU is DOUBLE PRECISION The value tau in the representation of H.

### C (in,out)

C is DOUBLE PRECISION array, dimension (LDC,N) On entry, the m by n matrix C. On exit, C is overwritten by the matrix H * C if SIDE = 'L', or C * H if SIDE = 'R'.

### LDC (in)

LDC is INTEGER The leading dimension of the array C. LDC >= max(1,M).

### WORK (out)

WORK is DOUBLE PRECISION array, dimension (N) if SIDE = 'L' or (M) if SIDE = 'R'

