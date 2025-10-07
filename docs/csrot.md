```fortran
subroutine csrot	(	integer	n,
		complex, dimension(*)	cx,
		integer	incx,
		complex, dimension(*)	cy,
		integer	incy,
		real	c,
		real	s )
```

 CSROT applies a plane rotation, where the cos and sin (c and s) are real
 and the vectors cx and cy are complex.
 jack dongarra, linpack, 3/11/78.

## Parameters
N : Integer [in]
> On entry, N specifies the order of the vectors cx and cy.
> N must be at least zero.

Cx : Complex Array, Dimension At Least [in,out]
> ( 1 + ( N - 1 )*abs( INCX ) ).
> Before entry, the incremented array CX must contain the n
> element vector cx. On exit, CX is overwritten by the updated
> vector cx.

Incx : Integer [in]
> On entry, INCX specifies the increment for the elements of
> CX. INCX must not be zero.

Cy : Complex Array, Dimension At Least [in,out]
> ( 1 + ( N - 1 )*abs( INCY ) ).
> Before entry, the incremented array CY must contain the n
> element vector cy. On exit, CY is overwritten by the updated
> vector cy.

Incy : Integer [in]
> On entry, INCY specifies the increment for the elements of
> CY. INCY must not be zero.

C : Real [in]
> On entry, C specifies the cosine, cos.

S : Real [in]
> On entry, S specifies the sine, sin.

