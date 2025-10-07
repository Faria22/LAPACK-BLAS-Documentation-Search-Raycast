```fortran
subroutine zla_wwaddw (
		integer n,
		complex*16, dimension(*) x,
		complex*16, dimension(*) y,
		complex*16, dimension(*) w
)
```

    ZLA_WWADDW adds a vector W into a doubled-single vector (X, Y).

    This works for all extant IBM's hex and binary floating point
    arithmetic, but not for decimal.

## Parameters
N : Integer [in]
> The length of vectors X, Y, and W.

X : Complex*16 Array, Dimension (n) [in,out]
> The first part of the doubled-single accumulation vector.

Y : Complex*16 Array, Dimension (n) [in,out]
> The second part of the doubled-single accumulation vector.

W : Complex*16 Array, Dimension (n) [in]
> The vector to be added.

