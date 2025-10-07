# ZCOPY

## Function Signature

```fortran
ZCOPY(N,ZX,INCX,ZY,INCY)
```

## Description


    ZCOPY copies a vector, x, to a vector, y.

## Parameters

### N (in)

N is INTEGER number of elements in input vector(s)

### ZX (in)

ZX is COMPLEX*16 array, dimension ( 1 + ( N - 1 )*abs( INCX ) )

### INCX (in)

INCX is INTEGER storage spacing between elements of ZX

### ZY (out)

ZY is COMPLEX*16 array, dimension ( 1 + ( N - 1 )*abs( INCY ) )

### INCY (in)

INCY is INTEGER storage spacing between elements of ZY

