# DSCAL

## Function Signature

```fortran
DSCAL(N,DA,DX,INCX)
```

## Description


    DSCAL scales a vector by a constant.
    uses unrolled loops for increment equal to 1.

## Parameters

### N (in)

N is INTEGER number of elements in input vector(s)

### DA (in)

DA is DOUBLE PRECISION On entry, DA specifies the scalar alpha.

### DX (in,out)

DX is DOUBLE PRECISION array, dimension ( 1 + ( N - 1 )*abs( INCX ) )

### INCX (in)

INCX is INTEGER storage spacing between elements of DX

