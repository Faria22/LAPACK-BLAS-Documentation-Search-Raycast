# ZRSCL

## Function Signature

```fortran
ZRSCL(N, A, X, INCX)
```

## Description


 ZRSCL multiplies an n-element complex vector x by the complex scalar
 1/a.  This is done without overflow or underflow as long as
 the final result x/a does not overflow or underflow.

## Parameters

### N (in)

N is INTEGER The number of components of the vector x.

### A (in)

A is COMPLEX*16 The scalar a which is used to divide each component of x. A must not be 0, or the subroutine will divide by zero.

### X (in,out)

X is COMPLEX*16 array, dimension (1+(N-1)*abs(INCX)) The n-element vector x.

### INCX (in)

INCX is INTEGER The increment between successive values of the vector SX. > 0: SX(1) = X(1) and SX(1+(i-1)*INCX) = x(i), 1< i<= n

