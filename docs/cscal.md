# CSCAL

## Function Signature

```fortran
CSCAL(N,CA,CX,INCX)
```

## Description


    CSCAL scales a vector by a constant.

## Parameters

### N (in)

N is INTEGER number of elements in input vector(s)

### CA (in)

CA is COMPLEX On entry, CA specifies the scalar alpha.

### CX (in,out)

CX is COMPLEX array, dimension ( 1 + ( N - 1 )*abs( INCX ) )

### INCX (in)

INCX is INTEGER storage spacing between elements of CX

