# DZASUM

## Function Signature

```fortran
DZASUM(N,ZX,INCX)
```

## Description


    DZASUM takes the sum of the (|Re(.)| + |Im(.)|)'s of a complex vector and
    returns a double precision result.

## Parameters

### N (in)

N is INTEGER number of elements in input vector(s)

### ZX (in,out)

ZX is COMPLEX*16 array, dimension ( 1 + ( N - 1 )*abs( INCX ) )

### INCX (in)

INCX is INTEGER storage spacing between elements of ZX

