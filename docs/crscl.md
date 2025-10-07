```fortran
subroutine crscl (
		integer n,
		complex a,
		complex, dimension(*) x,
		integer incx
)
```

 CRSCL multiplies an n-element complex vector x by the complex scalar
 1/a.  This is done without overflow or underflow as long as
 the final result x/a does not overflow or underflow.

## Parameters
N : Integer [in]
> The number of components of the vector x.

A : Complex [in]
> The scalar a which is used to divide each component of x.
> A must not be 0, or the subroutine will divide by zero.

X : Complex Array, Dimension [in,out]
> (1+(N-1)*abs(INCX))
> The n-element vector x.

Incx : Integer [in]
> The increment between successive values of the vector X.
> > 0:  X(1) = X(1) and X(1+(i-1)*INCX) = x(i),     1< i<= n

