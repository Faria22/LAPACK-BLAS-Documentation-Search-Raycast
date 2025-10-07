# ZAXPBY

## Function Signature

```fortran
ZAXPBY(N,ZA,ZX,INCX,ZB,ZY,INCY)
```

## Description


    ZAXPBY constant times a vector plus constant times a vector.

    Y = ALPHA * X + BETA * Y


## Parameters

### N (in)

N is INTEGER number of elements in input vector(s)

### ZA (in)

ZA is COMPLEX*16 On entry, ZA specifies the scalar alpha.

### ZX (in)

ZX is COMPLEX*16 array, dimension ( 1 + ( N - 1 )*abs( INCX ) )

### INCX (in)

INCX is INTEGER storage spacing between elements of ZX

### ZB (in)

ZB is COMPLEX*16 On entry, ZB specifies the scalar beta.

### ZY (in,out)

ZY is COMPLEX*16 array, dimension ( 1 + ( N - 1 )*abs( INCY ) )

### INCY (in)

INCY is INTEGER storage spacing between elements of ZY

