```fortran
subroutine sla_wwaddw	(	integer	n,
		real, dimension(*)	x,
		real, dimension(*)	y,
		real, dimension(*)	w )
```

    SLA_WWADDW adds a vector W into a doubled-single vector (X, Y).

    This works for all extant IBM's hex and binary floating point
    arithmetic, but not for decimal.

## Parameters
N : Integer [in]
> The length of vectors X, Y, and W.

X : Real Array, Dimension (n) [in,out]
> The first part of the doubled-single accumulation vector.

Y : Real Array, Dimension (n) [in,out]
> The second part of the doubled-single accumulation vector.

W : Real Array, Dimension (n) [in]
> The vector to be added.

