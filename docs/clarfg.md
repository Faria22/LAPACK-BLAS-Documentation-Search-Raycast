```fortran
subroutine clarfg	(	integer	n,
		complex	alpha,
		complex, dimension(*)	x,
		integer	incx,
		complex	tau )
```

 CLARFG generates a complex elementary reflector H of order n, such
 that

       H**H * ( alpha ) = ( beta ),   H**H * H = I.
              (   x   )   (   0  )

 where alpha and beta are scalars, with beta real, and x is an
 (n-1)-element complex vector. H is represented in the form

       H = I - tau * ( 1 ) * ( 1 v**H ) ,
                     ( v )

 where tau is a complex scalar and v is a complex (n-1)-element
 vector. Note that H is not hermitian.

 If the elements of x are all zero and alpha is real, then tau = 0
 and H is taken to be the unit matrix.

 Otherwise  1 <= real(tau) <= 2  and  abs(tau-1) <= 1 .

## Parameters
N : Integer [in]
> The order of the elementary reflector.

Alpha : Complex [in,out]
> On entry, the value alpha.
> On exit, it is overwritten with the value beta.

X : Complex Array, Dimension [in,out]
> (1+(N-2)*abs(INCX))
> On entry, the vector x.
> On exit, it is overwritten with the vector v.

Incx : Integer [in]
> The increment between elements of X. INCX > 0.

Tau : Complex [out]
> The value tau.

