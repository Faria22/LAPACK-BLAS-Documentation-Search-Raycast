# SCASUM

## Function Signature

```fortran
SCASUM(N,CX,INCX)
```

## Description


    SCASUM takes the sum of the (|Re(.)| + |Im(.)|)'s of a complex vector and
    returns a single precision result.

## Parameters

### N (in)

N is INTEGER number of elements in input vector(s)

### CX (in,out)

CX is COMPLEX array, dimension ( 1 + ( N - 1 )*abs( INCX ) )

### INCX (in)

INCX is INTEGER storage spacing between elements of SX

