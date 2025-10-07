```fortran
subroutine slartv (
		integer n,
		real, dimension(*) x,
		integer incx,
		real, dimension(*) y,
		integer incy,
		real, dimension(*) c,
		real, dimension(*) s,
		integer incc
)
```

 SLARTV applies a vector of real plane rotations to elements of the
 real vectors x and y. For i = 1,2,...,n

    ( x(i) ) := (  c(i)  s(i) ) ( x(i) )
    ( y(i) )    ( -s(i)  c(i) ) ( y(i) )

## Parameters
N : Integer [in]
> The number of plane rotations to be applied.

X : Real Array, [in,out]
> dimension (1+(N-1)*INCX)
> The vector x.

Incx : Integer [in]
> The increment between elements of X. INCX > 0.

Y : Real Array, [in,out]
> dimension (1+(N-1)*INCY)
> The vector y.

Incy : Integer [in]
> The increment between elements of Y. INCY > 0.

C : Real Array, Dimension (1+(n-1)*incc) [in]
> The cosines of the plane rotations.

S : Real Array, Dimension (1+(n-1)*incc) [in]
> The sines of the plane rotations.

Incc : Integer [in]
> The increment between elements of C and S. INCC > 0.

