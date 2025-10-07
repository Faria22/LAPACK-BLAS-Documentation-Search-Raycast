# SSWAP

## Function Signature

```fortran
SSWAP(N,SX,INCX,SY,INCY)
```

## Description


    SSWAP interchanges two vectors.
    uses unrolled loops for increments equal to 1.

## Parameters

### N (in)

N is INTEGER number of elements in input vector(s)

### SX (in,out)

SX is REAL array, dimension ( 1 + ( N - 1 )*abs( INCX ) )

### INCX (in)

INCX is INTEGER storage spacing between elements of SX

### SY (in,out)

SY is REAL array, dimension ( 1 + ( N - 1 )*abs( INCY ) )

### INCY (in)

INCY is INTEGER storage spacing between elements of SY

