```fortran
subroutine slar2v (
		integer n,
		real, dimension(*) x,
		real, dimension(*) y,
		real, dimension(*) z,
		integer incx,
		real, dimension(*) c,
		real, dimension(*) s,
		integer incc
)
```

 SLAR2V applies a vector of real plane rotations from both sides to
 a sequence of 2-by-2 real symmetric matrices, defined by the elements
 of the vectors x, y and z. For i = 1,2,...,n

    ( x(i)  z(i) ) := (  c(i)  s(i) ) ( x(i)  z(i) ) ( c(i) -s(i) )
    ( z(i)  y(i) )    ( -s(i)  c(i) ) ( z(i)  y(i) ) ( s(i)  c(i) )

## Parameters
N : Integer [in]
> The number of plane rotations to be applied.

X : Real Array, [in,out]
> dimension (1+(N-1)*INCX)
> The vector x.

Y : Real Array, [in,out]
> dimension (1+(N-1)*INCX)
> The vector y.

Z : Real Array, [in,out]
> dimension (1+(N-1)*INCX)
> The vector z.

Incx : Integer [in]
> The increment between elements of X, Y and Z. INCX > 0.

C : Real Array, Dimension (1+(n-1)*incc) [in]
> The cosines of the plane rotations.

S : Real Array, Dimension (1+(n-1)*incc) [in]
> The sines of the plane rotations.

Incc : Integer [in]
> The increment between elements of C and S. INCC > 0.

