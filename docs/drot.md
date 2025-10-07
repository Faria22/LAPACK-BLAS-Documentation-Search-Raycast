# DROT

## Function Signature

```fortran
DROT(N,DX,INCX,DY,INCY,C,S)
```

## Description


    DROT applies a plane rotation.

## Parameters

### N (in)

N is INTEGER number of elements in input vector(s)

### DX (in,out)

DX is DOUBLE PRECISION array, dimension ( 1 + ( N - 1 )*abs( INCX ) )

### INCX (in)

INCX is INTEGER storage spacing between elements of DX

### DY (in,out)

DY is DOUBLE PRECISION array, dimension ( 1 + ( N - 1 )*abs( INCY ) )

### INCY (in)

INCY is INTEGER storage spacing between elements of DY

### C (in)

C is DOUBLE PRECISION

### S (in)

S is DOUBLE PRECISION

