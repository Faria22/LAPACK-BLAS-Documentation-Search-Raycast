```fortran
subroutine csscal (
		integer n,
		real sa,
		complex, dimension(*) cx,
		integer incx
)
```

    CSSCAL scales a complex vector by a real constant.

## Parameters
N : Integer [in]
> number of elements in input vector(s)

Sa : Real [in]
> On entry, SA specifies the scalar alpha.

Cx : Complex Array, Dimension ( 1 + ( N - 1 )*abs( Incx ) ) [in,out]

Incx : Integer [in]
> storage spacing between elements of CX

