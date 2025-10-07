# SASUM

## Function Signature

```fortran
SASUM(N,SX,INCX)
```

## Description


    SASUM takes the sum of the absolute values.
    uses unrolled loops for increment equal to one.

## Parameters

### N (in)

N is INTEGER number of elements in input vector(s)

### SX (in)

SX is REAL array, dimension ( 1 + ( N - 1 )*abs( INCX ) )

### INCX (in)

INCX is INTEGER storage spacing between elements of SX

