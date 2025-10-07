```fortran
subroutine zlar2v	(	integer	n,
		complex*16, dimension(*)	x,
		complex*16, dimension(*)	y,
		complex*16, dimension(*)	z,
		integer	incx,
		double precision, dimension(*)	c,
		complex*16, dimension(*)	s,
		integer	incc )
```

 ZLAR2V applies a vector of complex plane rotations with real cosines
 from both sides to a sequence of 2-by-2 complex Hermitian matrices,
 defined by the elements of the vectors x, y and z. For i = 1,2,...,n

    (       x(i)  z(i) ) :=
    ( conjg(z(i)) y(i) )

      (  c(i) conjg(s(i)) ) (       x(i)  z(i) ) ( c(i) -conjg(s(i)) )
      ( -s(i)       c(i)  ) ( conjg(z(i)) y(i) ) ( s(i)        c(i)  )

## Parameters
N : Integer [in]
> The number of plane rotations to be applied.

X : Complex*16 Array, Dimension (1+(n-1)*incx) [in,out]
> The vector x; the elements of x are assumed to be real.

Y : Complex*16 Array, Dimension (1+(n-1)*incx) [in,out]
> The vector y; the elements of y are assumed to be real.

Z : Complex*16 Array, Dimension (1+(n-1)*incx) [in,out]
> The vector z.

Incx : Integer [in]
> The increment between elements of X, Y and Z. INCX > 0.

C : Double Precision Array, Dimension (1+(n-1)*incc) [in]
> The cosines of the plane rotations.

S : Complex*16 Array, Dimension (1+(n-1)*incc) [in]
> The sines of the plane rotations.

Incc : Integer [in]
> The increment between elements of C and S. INCC > 0.

