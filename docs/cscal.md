```fortran
subroutine cscal (
		integer n,
		complex ca,
		complex, dimension(*) cx,
		integer incx
)
```

    CSCAL scales a vector by a constant.

## Parameters
N : Integer [in]
> number of elements in input vector(s)

Ca : Complex [in]
> On entry, CA specifies the scalar alpha.

Cx : Complex Array, Dimension ( 1 + ( N - 1 )*abs( Incx ) ) [in,out]

Incx : Integer [in]
> storage spacing between elements of CX

