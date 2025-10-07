```fortran
subroutine dla_wwaddw (
		integer n,
		double precision, dimension(*) x,
		double precision, dimension(*) y,
		double precision, dimension(*) w
)
```

    DLA_WWADDW adds a vector W into a doubled-single vector (X, Y).

    This works for all extant IBM's hex and binary floating point
    arithmetic, but not for decimal.

## Parameters
N : Integer [in]
> The length of vectors X, Y, and W.

X : Double Precision Array, Dimension (n) [in,out]
> The first part of the doubled-single accumulation vector.

Y : Double Precision Array, Dimension (n) [in,out]
> The second part of the doubled-single accumulation vector.

W : Double Precision Array, Dimension (n) [in]
> The vector to be added.

