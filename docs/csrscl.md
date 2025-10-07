# CSRSCL

## Function Signature

```fortran
CSRSCL(N, SA, SX, INCX)
```

## Description


 CSRSCL multiplies an n-element complex vector x by the real scalar
 1/a.  This is done without overflow or underflow as long as
 the final result x/a does not overflow or underflow.

## Parameters

### N (in)

N is INTEGER The number of components of the vector x.

### SA (in)

SA is REAL The scalar a which is used to divide each component of x. SA must be >= 0, or the subroutine will divide by zero.

### SX (in,out)

SX is COMPLEX array, dimension (1+(N-1)*abs(INCX)) The n-element vector x.

### INCX (in)

INCX is INTEGER The increment between successive values of the vector SX. > 0: SX(1) = X(1) and SX(1+(i-1)*INCX) = x(i), 1< i<= n

