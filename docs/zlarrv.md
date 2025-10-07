```fortran
subroutine zlarrv (
		n,
		vl,
		vu,
		d,
		l,
		pivmin,
		*                          isplit,
		m,
		dol,
		dou,
		minrgp,
		*                          rtol1,
		rtol2,
		w,
		werr,
		wgap,
		*                          iblock,
		indexw,
		gers,
		z,
		ldz,
		isuppz,
		*                          work,
		iwork,
		info
)
```

 ZLARRV computes the eigenvectors of the tridiagonal matrix
 T = L D L**T given L, D and APPROXIMATIONS to the eigenvalues of L D L**T.
 The input eigenvalues should have been computed by DLARRE.

## Parameters
N : Integer [in]
> The order of the matrix.  N >= 0.

Vl : Double Precision [in]
> Lower bound of the interval that contains the desired
> eigenvalues. VL < VU. Needed to compute gaps on the left or right
> end of the extremal eigenvalues in the desired RANGE.

Vu : Double Precision [in]
> Upper bound of the interval that contains the desired
> eigenvalues. VL < VU. Needed to compute gaps on the left or right
> end of the extremal eigenvalues in the desired RANGE.

D : Double Precision Array, Dimension (n) [in,out]
> On entry, the N diagonal elements of the diagonal matrix D.
> On exit, D may be overwritten.

L : Double Precision Array, Dimension (n) [in,out]
> On entry, the (N-1) subdiagonal elements of the unit
> bidiagonal matrix L are in elements 1 to N-1 of L
> (if the matrix is not split.) At the end of each block
> is stored the corresponding shift as given by DLARRE.
> On exit, L is overwritten.

Pivmin : Double Precision [in]
> The minimum pivot allowed in the Sturm sequence.

Isplit : Integer Array, Dimension (n) [in]
> The splitting points, at which T breaks up into blocks.
> The first block consists of rows/columns 1 to
> ISPLIT( 1 ), the second of rows/columns ISPLIT( 1 )+1
> through ISPLIT( 2 ), etc.

M : Integer [in]
> The total number of input eigenvalues.  0 <= M <= N.

Dol : Integer [in]

Dou : Integer [in]
> If the user wants to compute only selected eigenvectors from all
> the eigenvalues supplied, he can specify an index range DOL:DOU.
> Or else the setting DOL=1, DOU=M should be applied.
> Note that DOL and DOU refer to the order in which the eigenvalues
> are stored in W.
> If the user wants to compute only selected eigenpairs, then
> the columns DOL-1 to DOU+1 of the eigenvector space Z contain the
> computed eigenvectors. All other columns of Z are set to zero.

Minrgp : Double Precision [in]

Rtol1 : Double Precision [in]

Rtol2 : Double Precision [in]
> Parameters for bisection.
> An interval [LEFT,RIGHT] has converged if
> RIGHT-LEFT < MAX( RTOL1*GAP, RTOL2*MAX(|LEFT|,|RIGHT|) )

W : Double Precision Array, Dimension (n) [in,out]
> The first M elements of W contain the APPROXIMATE eigenvalues for
> which eigenvectors are to be computed.  The eigenvalues
> should be grouped by split-off block and ordered from
> smallest to largest within the block ( The output array
> W from DLARRE is expected here ). Furthermore, they are with
> respect to the shift of the corresponding root representation
> for their block. On exit, W holds the eigenvalues of the
> UNshifted matrix.

Werr : Double Precision Array, Dimension (n) [in,out]
> The first M elements contain the semiwidth of the uncertainty
> interval of the corresponding eigenvalue in W

Wgap : Double Precision Array, Dimension (n) [in,out]
> The separation from the right neighbor eigenvalue in W.

Iblock : Integer Array, Dimension (n) [in]
> The indices of the blocks (submatrices) associated with the
> corresponding eigenvalues in W; IBLOCK(i)=1 if eigenvalue
> W(i) belongs to the first block from the top, =2 if W(i)
> belongs to the second block, etc.

Indexw : Integer Array, Dimension (n) [in]
> The indices of the eigenvalues within each block (submatrix);
> for example, INDEXW(i)= 10 and IBLOCK(i)=2 imply that the
> i-th eigenvalue W(i) is the 10-th eigenvalue in the second block.

Gers : Double Precision Array, Dimension (2*n) [in]
> The N Gerschgorin intervals (the i-th Gerschgorin interval
> is (GERS(2*i-1), GERS(2*i)). The Gerschgorin intervals should
> be computed from the original UNshifted matrix.

Z : Complex*16 Array, Dimension (ldz, Max(1,m) ) [out]
> If INFO = 0, the first M columns of Z contain the
> orthonormal eigenvectors of the matrix T
> corresponding to the input eigenvalues, with the i-th
> column of Z holding the eigenvector associated with W(i).
> Note: the user must ensure that at least max(1,M) columns are
> supplied in the array Z.

Ldz : Integer [in]
> The leading dimension of the array Z.  LDZ >= 1, and if
> JOBZ = 'V', LDZ >= max(1,N).

Isuppz : Integer Array, Dimension ( 2*max(1,m) ) [out]
> The support of the eigenvectors in Z, i.e., the indices
> indicating the nonzero elements in Z. The I-th eigenvector
> is nonzero only in elements ISUPPZ( 2*I-1 ) through
> ISUPPZ( 2*I ).

Work : Double Precision Array, Dimension (12*n) [out]

Iwork : Integer Array, Dimension (7*n) [out]

Info : Integer [out]
> = 0:  successful exit
> > 0:  A problem occurred in ZLARRV.
> < 0:  One of the called subroutines signaled an internal problem.
> Needs inspection of the corresponding parameter IINFO
> for further information.
> =-1:  Problem in DLARRB when refining a child's eigenvalues.
> =-2:  Problem in DLARRF when computing the RRR of a child.
> When a child is inside a tight cluster, it can be difficult
> to find an RRR. A partial remedy from the user's point of
> view is to make the parameter MINRGP smaller and recompile.
> However, as the orthogonality of the computed vectors is
> proportional to 1/MINRGP, the user should be aware that
> he might be trading in precision when he decreases MINRGP.
> =-3:  Problem in DLARRB when refining a single eigenvalue
> after the Rayleigh correction was rejected.
> = 5:  The Rayleigh Quotient Iteration failed to converge to
> full accuracy in MAXITR steps.

