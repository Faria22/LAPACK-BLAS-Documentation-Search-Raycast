# ZSWAP

## Function Signature

```fortran
ZSWAP(N,ZX,INCX,ZY,INCY)
```

## Description


    ZSWAP interchanges two vectors.

## Parameters

### N (in)

N is INTEGER number of elements in input vector(s)

### ZX (in,out)

ZX is COMPLEX*16 array, dimension ( 1 + ( N - 1 )*abs( INCX ) )

### INCX (in)

INCX is INTEGER storage spacing between elements of ZX

### ZY (in,out)

ZY is COMPLEX*16 array, dimension ( 1 + ( N - 1 )*abs( INCY ) )

### INCY (in)

INCY is INTEGER storage spacing between elements of ZY

