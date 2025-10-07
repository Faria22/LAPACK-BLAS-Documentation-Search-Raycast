# SCOPY

## Function Signature

```fortran
SCOPY(N,SX,INCX,SY,INCY)
```

## Description


    SCOPY copies a vector, x, to a vector, y.
    uses unrolled loops for increments equal to 1.

## Parameters

### N (in)

N is INTEGER number of elements in input vector(s)

### SX (in)

SX is REAL array, dimension ( 1 + ( N - 1 )*abs( INCX ) )

### INCX (in)

INCX is INTEGER storage spacing between elements of SX

### SY (out)

SY is REAL array, dimension ( 1 + ( N - 1 )*abs( INCY ) )

### INCY (in)

INCY is INTEGER storage spacing between elements of SY

