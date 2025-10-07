```fortran
subroutine clacgv	(	integer	n,
		complex, dimension(*)	x,
		integer	incx )
```

 CLACGV conjugates a complex vector of length N.

## Parameters
N : Integer [in]
> The length of the vector X.  N >= 0.

X : Complex Array, Dimension [in,out]
> (1+(N-1)*abs(INCX))
> On entry, the vector of length N to be conjugated.
> On exit, X is overwritten with conjg(X).

Incx : Integer [in]
> The spacing between successive elements of X.

