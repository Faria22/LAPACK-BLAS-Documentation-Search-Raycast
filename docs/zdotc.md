# ZDOTC

## Function Signature

```fortran
ZDOTC(N,ZX,INCX,ZY,INCY)
```

## Description


 ZDOTC forms the dot product of two complex vectors
      ZDOTC = X^H * Y


## Parameters

### N (in)

N is INTEGER number of elements in input vector(s)

### ZX (in)

ZX is COMPLEX*16 array, dimension ( 1 + ( N - 1 )*abs( INCX ) )

### INCX (in)

INCX is INTEGER storage spacing between elements of ZX

### ZY (in)

ZY is COMPLEX*16 array, dimension ( 1 + ( N - 1 )*abs( INCY ) )

### INCY (in)

INCY is INTEGER storage spacing between elements of ZY

