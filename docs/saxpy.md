# SAXPY

## Function Signature

```fortran
SAXPY(N,SA,SX,INCX,SY,INCY)
```

## Description


    SAXPY constant times a vector plus a vector.
    uses unrolled loops for increments equal to one.

## Parameters

### N (in)

N is INTEGER number of elements in input vector(s)

### SA (in)

SA is REAL On entry, SA specifies the scalar alpha.

### SX (in)

SX is REAL array, dimension ( 1 + ( N - 1 )*abs( INCX ) )

### INCX (in)

INCX is INTEGER storage spacing between elements of SX

### SY (in,out)

SY is REAL array, dimension ( 1 + ( N - 1 )*abs( INCY ) )

### INCY (in)

INCY is INTEGER storage spacing between elements of SY

