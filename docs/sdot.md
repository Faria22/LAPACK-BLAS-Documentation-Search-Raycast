# SDOT

## Function Signature

```fortran
SDOT(N,SX,INCX,SY,INCY)
```

## Description


    SDOT forms the dot product of two vectors.
    uses unrolled loops for increments equal to one.

## Parameters

### N (in)

N is INTEGER number of elements in input vector(s)

### SX (in)

SX is REAL array, dimension ( 1 + ( N - 1 )*abs( INCX ) )

### INCX (in)

INCX is INTEGER storage spacing between elements of SX

### SY (in)

SY is REAL array, dimension ( 1 + ( N - 1 )*abs( INCY ) )

### INCY (in)

INCY is INTEGER storage spacing between elements of SY

