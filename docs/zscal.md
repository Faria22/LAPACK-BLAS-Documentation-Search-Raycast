# ZSCAL

## Function Signature

```fortran
ZSCAL(N,ZA,ZX,INCX)
```

## Description


    ZSCAL scales a vector by a constant.

## Parameters

### N (in)

N is INTEGER number of elements in input vector(s)

### ZA (in)

ZA is COMPLEX*16 On entry, ZA specifies the scalar alpha.

### ZX (in,out)

ZX is COMPLEX*16 array, dimension ( 1 + ( N - 1 )*abs( INCX ) )

### INCX (in)

INCX is INTEGER storage spacing between elements of ZX

