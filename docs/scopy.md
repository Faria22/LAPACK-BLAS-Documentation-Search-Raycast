```fortran
subroutine scopy (
		integer n,
		real, dimension(*) sx,
		integer incx,
		real, dimension(*) sy,
		integer incy
)
```

    SCOPY copies a vector, x, to a vector, y.
    uses unrolled loops for increments equal to 1.

## Parameters
N : Integer [in]
> number of elements in input vector(s)

Sx : Real Array, Dimension ( 1 + ( N - 1 )*abs( Incx ) ) [in]

Incx : Integer [in]
> storage spacing between elements of SX

Sy : Real Array, Dimension ( 1 + ( N - 1 )*abs( Incy ) ) [out]

Incy : Integer [in]
> storage spacing between elements of SY

