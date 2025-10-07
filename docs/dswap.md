# DSWAP

## Function Signature

```fortran
DSWAP(N,DX,INCX,DY,INCY)
```

## Description


    DSWAP interchanges two vectors.
    uses unrolled loops for increments equal to 1.

## Parameters

### N (in)

N is INTEGER number of elements in input vector(s)

### DX (in,out)

DX is DOUBLE PRECISION array, dimension ( 1 + ( N - 1 )*abs( INCX ) )

### INCX (in)

INCX is INTEGER storage spacing between elements of DX

### DY (in,out)

DY is DOUBLE PRECISION array, dimension ( 1 + ( N - 1 )*abs( INCY ) )

### INCY (in)

INCY is INTEGER storage spacing between elements of DY

