```fortran
subroutine zdscal (
		integer n,
		double precision da,
		complex*16, dimension(*) zx,
		integer incx
)
```

    ZDSCAL scales a vector by a constant.

## Parameters
N : Integer [in]
> number of elements in input vector(s)

Da : Double Precision [in]
> On entry, DA specifies the scalar alpha.

Zx : Complex*16 Array, Dimension ( 1 + ( N - 1 )*abs( Incx ) ) [in,out]

Incx : Integer [in]
> storage spacing between elements of ZX

