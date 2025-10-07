# CSSCAL

## Function Signature

```fortran
CSSCAL(N,SA,CX,INCX)
```

## Description


    CSSCAL scales a complex vector by a real constant.

## Parameters

### N (in)

N is INTEGER number of elements in input vector(s)

### SA (in)

SA is REAL On entry, SA specifies the scalar alpha.

### CX (in,out)

CX is COMPLEX array, dimension ( 1 + ( N - 1 )*abs( INCX ) )

### INCX (in)

INCX is INTEGER storage spacing between elements of CX

