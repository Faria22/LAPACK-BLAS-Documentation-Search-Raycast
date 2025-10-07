```fortran
subroutine caxpby	(	integer	n,
		complex	ca,
		complex, dimension(*)	cx,
		integer	incx,
		complex	cb,
		complex, dimension(*)	cy,
		integer	incy )
```

    CAXPBY constant times a vector plus constant times a vector.

    Y = ALPHA * X + BETA * Y


## Parameters
N : Integer [in]
> number of elements in input vector(s)

Ca : Complex [in]
> On entry, CA specifies the scalar alpha.

Cx : Complex Array, Dimension ( 1 + ( N - 1 )*abs( Incx ) ) [in]

Incx : Integer [in]
> storage spacing between elements of CX

Cb : Complex [in]
> On entry, CB specifies the scalar beta.

Cy : Complex Array, Dimension ( 1 + ( N - 1 )*abs( Incy ) ) [in,out]

Incy : Integer [in]
> storage spacing between elements of CY

