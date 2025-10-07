# CAXPBY

## Function Signature

```fortran
CAXPBY(N,CA,CX,INCX,CB,CY,INCY)
```

## Description


    CAXPBY constant times a vector plus constant times a vector.

    Y = ALPHA * X + BETA * Y


## Parameters

### N (in)

N is INTEGER number of elements in input vector(s)

### CA (in)

CA is COMPLEX On entry, CA specifies the scalar alpha.

### CX (in)

CX is COMPLEX array, dimension ( 1 + ( N - 1 )*abs( INCX ) )

### INCX (in)

INCX is INTEGER storage spacing between elements of CX

### CB (in)

CB is COMPLEX On entry, CB specifies the scalar beta.

### CY (in,out)

CY is COMPLEX array, dimension ( 1 + ( N - 1 )*abs( INCY ) )

### INCY (in)

INCY is INTEGER storage spacing between elements of CY

