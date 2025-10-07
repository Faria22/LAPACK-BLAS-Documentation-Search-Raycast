# ZAXPY

## Function Signature

```fortran
ZAXPY(N,ZA,ZX,INCX,ZY,INCY)
```

## Description


    ZAXPY constant times a vector plus a vector.

## Parameters

### N (in)

N is INTEGER number of elements in input vector(s)

### ZA (in)

ZA is COMPLEX*16 On entry, ZA specifies the scalar alpha.

### ZX (in)

ZX is COMPLEX*16 array, dimension ( 1 + ( N - 1 )*abs( INCX ) )

### INCX (in)

INCX is INTEGER storage spacing between elements of ZX

### ZY (in,out)

ZY is COMPLEX*16 array, dimension ( 1 + ( N - 1 )*abs( INCY ) )

### INCY (in)

INCY is INTEGER storage spacing between elements of ZY

