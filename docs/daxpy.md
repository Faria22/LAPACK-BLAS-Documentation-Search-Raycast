# DAXPY

## Function Signature

```fortran
DAXPY(N,DA,DX,INCX,DY,INCY)
```

## Description


    DAXPY constant times a vector plus a vector.
    uses unrolled loops for increments equal to one.

## Parameters

### N (in)

N is INTEGER number of elements in input vector(s)

### DA (in)

DA is DOUBLE PRECISION On entry, DA specifies the scalar alpha.

### DX (in)

DX is DOUBLE PRECISION array, dimension ( 1 + ( N - 1 )*abs( INCX ) )

### INCX (in)

INCX is INTEGER storage spacing between elements of DX

### DY (in,out)

DY is DOUBLE PRECISION array, dimension ( 1 + ( N - 1 )*abs( INCY ) )

### INCY (in)

INCY is INTEGER storage spacing between elements of DY

