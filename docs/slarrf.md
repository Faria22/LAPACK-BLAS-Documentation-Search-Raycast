```fortran
subroutine slarrf	(	n,
		d,
		l,
		ld,
		clstrt,
		clend,
		*                          w,
		wgap,
		werr,
		*                          spdiam,
		clgapl,
		clgapr,
		pivmin,
		sigma,
		*                          dplus,
		lplus,
		work,
		info )
```

 Given the initial representation L D L^T and its cluster of close
 eigenvalues (in a relative measure), W( CLSTRT ), W( CLSTRT+1 ), ...
 W( CLEND ), SLARRF finds a new relatively robust representation
 L D L^T - SIGMA I = L(+) D(+) L(+)^T such that at least one of the
 eigenvalues of L(+) D(+) L(+)^T is relatively isolated.

## Parameters
N : Integer [in]
> The order of the matrix (subblock, if the matrix split).

D : Real Array, Dimension (n) [in]
> The N diagonal elements of the diagonal matrix D.

L : Real Array, Dimension (n-1) [in]
> The (N-1) subdiagonal elements of the unit bidiagonal
> matrix L.

Ld : Real Array, Dimension (n-1) [in]
> The (N-1) elements L(i)*D(i).

Clstrt : Integer [in]
> The index of the first eigenvalue in the cluster.

Clend : Integer [in]
> The index of the last eigenvalue in the cluster.

W : Real Array, Dimension [in]
> dimension is >=  (CLEND-CLSTRT+1)
> The eigenvalue APPROXIMATIONS of L D L^T in ascending order.
> W( CLSTRT ) through W( CLEND ) form the cluster of relatively
> close eigenalues.

Wgap : Real Array, Dimension [in,out]
> dimension is >=  (CLEND-CLSTRT+1)
> The separation from the right neighbor eigenvalue in W.

Werr : Real Array, Dimension [in]
> dimension is >=  (CLEND-CLSTRT+1)
> WERR contain the semiwidth of the uncertainty
> interval of the corresponding eigenvalue APPROXIMATION in W

Spdiam : Real [in]
> estimate of the spectral diameter obtained from the
> Gerschgorin intervals

Clgapl : Real [in]

Clgapr : Real [in]
> absolute gap on each end of the cluster.
> Set by the calling routine to protect against shifts too close
> to eigenvalues outside the cluster.

Pivmin : Real [in]
> The minimum pivot allowed in the Sturm sequence.

Sigma : Real [out]
> The shift used to form L(+) D(+) L(+)^T.

Dplus : Real Array, Dimension (n) [out]
> The N diagonal elements of the diagonal matrix D(+).

Lplus : Real Array, Dimension (n-1) [out]
> The first (N-1) elements of LPLUS contain the subdiagonal
> elements of the unit bidiagonal matrix L(+).

Work : Real Array, Dimension (2*n) [out]
> Workspace.

Info : Integer [out]
> Signals processing OK (=0) or failure (=1)

