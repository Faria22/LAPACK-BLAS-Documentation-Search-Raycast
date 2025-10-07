# CROT

## Function Signature

```fortran
CROT(N, CX, INCX, CY, INCY, C, S)
```

## Description


 CROT applies a plane rotation, where the cos (C) is real and the
 sin (S) is complex, and the vectors CX and CY are complex.

## Parameters

### N (in)

N is INTEGER The number of elements in the vectors CX and CY.

### CX (in,out)

CX is COMPLEX array, dimension (N) On input, the vector X. On output, CX is overwritten with C*X + S*Y.

### INCX (in)

INCX is INTEGER The increment between successive values of CX. INCX <> 0.

### CY (in,out)

CY is COMPLEX array, dimension (N) On input, the vector Y. On output, CY is overwritten with -CONJG(S)*X + C*Y.

### INCY (in)

INCY is INTEGER The increment between successive values of CY. INCX <> 0.

### C (in)

C is REAL

### S (in)

S is COMPLEX C and S define a rotation [ C S ] [ -conjg(S) C ] where C*C + S*CONJG(S) = 1.0.

