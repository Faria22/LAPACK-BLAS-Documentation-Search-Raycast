```fortran
subroutine zcopy	(	integer	n,
		complex*16, dimension(*)	zx,
		integer	incx,
		complex*16, dimension(*)	zy,
		integer	incy )
```

    ZCOPY copies a vector, x, to a vector, y.

## Parameters
N : Integer [in]
> number of elements in input vector(s)

Zx : Complex*16 Array, Dimension ( 1 + ( N - 1 )*abs( Incx ) ) [in]

Incx : Integer [in]
> storage spacing between elements of ZX

Zy : Complex*16 Array, Dimension ( 1 + ( N - 1 )*abs( Incy ) ) [out]

Incy : Integer [in]
> storage spacing between elements of ZY

