```fortran
subroutine zaxpby	(	integer	n,
		complex*16	za,
		complex*16, dimension(*)	zx,
		integer	incx,
		complex*16	zb,
		complex*16, dimension(*)	zy,
		integer	incy )
```

    ZAXPBY constant times a vector plus constant times a vector.

    Y = ALPHA * X + BETA * Y


## Parameters
N : Integer [in]
> number of elements in input vector(s)

Za : Complex*16 [in]
> On entry, ZA specifies the scalar alpha.

Zx : Complex*16 Array, Dimension ( 1 + ( N - 1 )*abs( Incx ) ) [in]

Incx : Integer [in]
> storage spacing between elements of ZX

Zb : Complex*16 [in]
> On entry, ZB specifies the scalar beta.

Zy : Complex*16 Array, Dimension ( 1 + ( N - 1 )*abs( Incy ) ) [in,out]

Incy : Integer [in]
> storage spacing between elements of ZY

