# DSDOT

## Function Signature

```fortran
DSDOT(N,SX,INCX,SY,INCY)
```

## Description


 Compute the inner product of two vectors with extended
 precision accumulation and result.

 Returns D.P. dot product accumulated in D.P., for S.P. SX and SY
 DSDOT = sum for I = 0 to N-1 of  SX(LX+I*INCX) * SY(LY+I*INCY),
 where LX = 1 if INCX .GE. 0, else LX = 1+(1-N)*INCX, and LY is
 defined in a similar way using INCY.

## Parameters

### N (in)

N is INTEGER number of elements in input vector(s)

### SX (in)

SX is REAL array, dimension(N) single precision vector with N elements

### INCX (in)

INCX is INTEGER storage spacing between elements of SX

### SY (in)

SY is REAL array, dimension(N) single precision vector with N elements

### INCY (in)

INCY is INTEGER storage spacing between elements of SY

