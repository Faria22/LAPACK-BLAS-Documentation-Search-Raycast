# CAXPY

## Function Signature

```fortran
CAXPY(N,CA,CX,INCX,CY,INCY)
```

## Description


    CAXPY constant times a vector plus a vector.

## Parameters

### N (in)

N is INTEGER number of elements in input vector(s)

### CA (in)

CA is COMPLEX On entry, CA specifies the scalar alpha.

### CX (in)

CX is COMPLEX array, dimension ( 1 + ( N - 1 )*abs( INCX ) )

### INCX (in)

INCX is INTEGER storage spacing between elements of CX

### CY (in,out)

CY is COMPLEX array, dimension ( 1 + ( N - 1 )*abs( INCY ) )

### INCY (in)

INCY is INTEGER storage spacing between elements of CY

