# CCOPY

## Function Signature

```fortran
CCOPY(N,CX,INCX,CY,INCY)
```

## Description


    CCOPY copies a vector x to a vector y.

## Parameters

### N (in)

N is INTEGER number of elements in input vector(s)

### CX (in)

CX is COMPLEX array, dimension ( 1 + ( N - 1 )*abs( INCX ) )

### INCX (in)

INCX is INTEGER storage spacing between elements of CX

### CY (out)

CY is COMPLEX array, dimension ( 1 + ( N - 1 )*abs( INCY ) )

### INCY (in)

INCY is INTEGER storage spacing between elements of CY

