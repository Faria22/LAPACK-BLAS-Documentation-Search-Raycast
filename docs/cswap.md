# CSWAP

## Function Signature

```fortran
CSWAP(N,CX,INCX,CY,INCY)
```

## Description


   CSWAP interchanges two vectors.

## Parameters

### N (in)

N is INTEGER number of elements in input vector(s)

### CX (in,out)

CX is COMPLEX array, dimension ( 1 + ( N - 1 )*abs( INCX ) )

### INCX (in)

INCX is INTEGER storage spacing between elements of CX

### CY (in,out)

CY is COMPLEX array, dimension ( 1 + ( N - 1 )*abs( INCY ) )

### INCY (in)

INCY is INTEGER storage spacing between elements of CY

