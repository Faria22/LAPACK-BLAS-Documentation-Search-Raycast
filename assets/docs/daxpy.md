```fortran
subroutine daxpy (
		integer n,
		double precision da,
		double precision, dimension(*) dx,
		integer incx,
		double precision, dimension(*) dy,
		integer incy
)
```

    DAXPY constant times a vector plus a vector.
    uses unrolled loops for increments equal to one.

## Parameters
N : Integer [in]
> number of elements in input vector(s)

Da : Double Precision [in]
> On entry, DA specifies the scalar alpha.

Dx : Double Precision Array, Dimension ( 1 + ( N - 1 )*abs( Incx ) ) [in]

Incx : Integer [in]
> storage spacing between elements of DX

Dy : Double Precision Array, Dimension ( 1 + ( N - 1 )*abs( Incy ) ) [in,out]

Incy : Integer [in]
> storage spacing between elements of DY

