# DDOT

## Function Signature

```fortran
DDOT(N,DX,INCX,DY,INCY)
```

## Description


    DDOT forms the dot product of two vectors.
    uses unrolled loops for increments equal to one.

## Parameters

### N (in)

N is INTEGER number of elements in input vector(s)

### DX (in)

DX is DOUBLE PRECISION array, dimension ( 1 + ( N - 1 )*abs( INCX ) )

### INCX (in)

INCX is INTEGER storage spacing between elements of DX

### DY (in)

DY is DOUBLE PRECISION array, dimension ( 1 + ( N - 1 )*abs( INCY ) )

### INCY (in)

INCY is INTEGER storage spacing between elements of DY

