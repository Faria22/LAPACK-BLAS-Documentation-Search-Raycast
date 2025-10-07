```fortran
subroutine slarrj (
		n,
		d,
		e2,
		ifirst,
		ilast,
		*                          rtol,
		offset,
		w,
		werr,
		work,
		iwork,
		*                          pivmin,
		spdiam,
		info
)
```

 Given the initial eigenvalue approximations of T, SLARRJ
 does  bisection to refine the eigenvalues of T,
 W( IFIRST-OFFSET ) through W( ILAST-OFFSET ), to more accuracy. Initial
 guesses for these eigenvalues are input in W, the corresponding estimate
 of the error in these guesses in WERR. During bisection, intervals
 [left, right] are maintained by storing their mid-points and
 semi-widths in the arrays W and WERR respectively.

## Parameters
N : Integer [in]
> The order of the matrix.

D : Real Array, Dimension (n) [in]
> The N diagonal elements of T.

E2 : Real Array, Dimension (n-1) [in]
> The Squares of the (N-1) subdiagonal elements of T.

Ifirst : Integer [in]
> The index of the first eigenvalue to be computed.

Ilast : Integer [in]
> The index of the last eigenvalue to be computed.

Rtol : Real [in]
> Tolerance for the convergence of the bisection intervals.
> An interval [LEFT,RIGHT] has converged if
> RIGHT-LEFT < RTOL*MAX(|LEFT|,|RIGHT|).

Offset : Integer [in]
> Offset for the arrays W and WERR, i.e., the IFIRST-OFFSET
> through ILAST-OFFSET elements of these arrays are to be used.

W : Real Array, Dimension (n) [in,out]
> On input, W( IFIRST-OFFSET ) through W( ILAST-OFFSET ) are
> estimates of the eigenvalues of L D L^T indexed IFIRST through
> ILAST.
> On output, these estimates are refined.

Werr : Real Array, Dimension (n) [in,out]
> On input, WERR( IFIRST-OFFSET ) through WERR( ILAST-OFFSET ) are
> the errors in the estimates of the corresponding elements in W.
> On output, these errors are refined.

Work : Real Array, Dimension (2*n) [out]
> Workspace.

Iwork : Integer Array, Dimension (2*n) [out]
> Workspace.

Pivmin : Real [in]
> The minimum pivot in the Sturm sequence for T.

Spdiam : Real [in]
> The spectral diameter of T.

Info : Integer [out]
> Error flag.

