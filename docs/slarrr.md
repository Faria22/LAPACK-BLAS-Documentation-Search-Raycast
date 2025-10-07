```fortran
subroutine slarrr	(	integer	n,
		real, dimension(*)	d,
		real, dimension(*)	e,
		integer	info )
```

 Perform tests to decide whether the symmetric tridiagonal matrix T
 warrants expensive computations which guarantee high relative accuracy
 in the eigenvalues.

## Parameters
N : Integer [in]
> The order of the matrix. N > 0.

D : Real Array, Dimension (n) [in]
> The N diagonal elements of the tridiagonal matrix T.

E : Real Array, Dimension (n) [in,out]
> On entry, the first (N-1) entries contain the subdiagonal
> elements of the tridiagonal matrix T; E(N) is set to ZERO.

Info : Integer [out]
> INFO = 0(default) : the matrix warrants computations preserving
> relative accuracy.
> INFO = 1          : the matrix warrants computations guaranteeing
> only absolute accuracy.

