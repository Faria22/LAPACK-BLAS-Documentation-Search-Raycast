# SSCAL

## Function Signature

```fortran
SSCAL(N,SA,SX,INCX)
```

## Description


    SSCAL scales a vector by a constant.
    uses unrolled loops for increment equal to 1.

## Parameters

### N (in)

N is INTEGER number of elements in input vector(s)

### SA (in)

SA is REAL On entry, SA specifies the scalar alpha.

### SX (in,out)

SX is REAL array, dimension ( 1 + ( N - 1 )*abs( INCX ) )

### INCX (in)

INCX is INTEGER storage spacing between elements of SX

