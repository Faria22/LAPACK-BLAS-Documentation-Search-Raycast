```fortran
subroutine zswap (
		integer n,
		complex*16, dimension(*) zx,
		integer incx,
		complex*16, dimension(*) zy,
		integer incy
)
```

    ZSWAP interchanges two vectors.

## Parameters
N : Integer [in]
> number of elements in input vector(s)

Zx : Complex*16 Array, Dimension ( 1 + ( N - 1 )*abs( Incx ) ) [in,out]

Incx : Integer [in]
> storage spacing between elements of ZX

Zy : Complex*16 Array, Dimension ( 1 + ( N - 1 )*abs( Incy ) ) [in,out]

Incy : Integer [in]
> storage spacing between elements of ZY

