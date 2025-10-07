# SAXPBY

## Function Signature

```fortran
SAXPBY(N,SA,SX,INCX,SB,SY,INCY)
```

## Description


    SAXPBY constant times a vector plus constant times a vector.

    Y = ALPHA * X + BETA * Y


## Parameters

### N (in)

N is INTEGER number of elements in input vector(s)

### SA (in)

SA is REAL On entry, SA specifies the scalar alpha.

### SX (in)

SX is REAL array, dimension ( 1 + ( N - 1 )*abs( INCX ) )

### INCX (in)

INCX is INTEGER storage spacing between elements of SX

### SB (in)

SB is REAL On entry, SB specifies the scalar beta.

### SY (in,out)

SY is REAL array, dimension ( 1 + ( N - 1 )*abs( INCY ) )

### INCY (in)

INCY is INTEGER storage spacing between elements of SY

