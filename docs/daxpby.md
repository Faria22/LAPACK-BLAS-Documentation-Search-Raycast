# DAXPBY

## Function Signature

```fortran
DAXPBY(N,DA,DX,INCX,DB,DY,INCY)
```

## Description


    DAXPBY constant times a vector plus constant times a vector.

    Y = ALPHA * X + BETA * Y


## Parameters

### N (in)

N is INTEGER number of elements in input vector(s)

### DA (in)

DA is DOUBLE PRECISION On entry, DA specifies the scalar alpha.

### DX (in)

DX is DOUBLE PRECISION array, dimension ( 1 + ( N - 1 )*abs( INCX ) )

### INCX (in)

INCX is INTEGER storage spacing between elements of DX

### DB (in)

DB is DOUBLE PRECISION On entry, DB specifies the scalar beta.

### DY (in,out)

DY is DOUBLE PRECISION array, dimension ( 1 + ( N - 1 )*abs( INCY ) )

### INCY (in)

INCY is INTEGER storage spacing between elements of DY

