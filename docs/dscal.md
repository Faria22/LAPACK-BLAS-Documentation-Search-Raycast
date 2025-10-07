```fortran
subroutine dscal	(	integer	n,
		double precision	da,
		double precision, dimension(*)	dx,
		integer	incx )
```

    DSCAL scales a vector by a constant.
    uses unrolled loops for increment equal to 1.

## Parameters
N : Integer [in]
> number of elements in input vector(s)

Da : Double Precision [in]
> On entry, DA specifies the scalar alpha.

Dx : Double Precision Array, Dimension ( 1 + ( N - 1 )*abs( Incx ) ) [in,out]

Incx : Integer [in]
> storage spacing between elements of DX

