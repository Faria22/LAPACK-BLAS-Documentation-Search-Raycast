```fortran
subroutine sscal (
		integer n,
		real sa,
		real, dimension(*) sx,
		integer incx
)
```

    SSCAL scales a vector by a constant.
    uses unrolled loops for increment equal to 1.

## Parameters
N : Integer [in]
> number of elements in input vector(s)

Sa : Real [in]
> On entry, SA specifies the scalar alpha.

Sx : Real Array, Dimension ( 1 + ( N - 1 )*abs( Incx ) ) [in,out]

Incx : Integer [in]
> storage spacing between elements of SX

