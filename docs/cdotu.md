# CDOTU

## Function Signature

```fortran
CDOTU(N,CX,INCX,CY,INCY)
```

## Description


 CDOTU forms the dot product of two complex vectors
      CDOTU = X^T * Y


## Parameters

### N (in)

N is INTEGER number of elements in input vector(s)

### CX (in)

CX is COMPLEX array, dimension ( 1 + ( N - 1 )*abs( INCX ) )

### INCX (in)

INCX is INTEGER storage spacing between elements of CX

### CY (in)

CY is COMPLEX array, dimension ( 1 + ( N - 1 )*abs( INCY ) )

### INCY (in)

INCY is INTEGER storage spacing between elements of CY

