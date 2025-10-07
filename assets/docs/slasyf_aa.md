```fortran
subroutine slasyf_aa (
		uplo,
		j1,
		m,
		nb,
		a,
		lda,
		ipiv,
		*                             h,
		ldh,
		work
)
```

 DLATRF_AA factorizes a panel of a real symmetric matrix A using
 the Aasen's algorithm. The panel consists of a set of NB rows of A
 when UPLO is U, or a set of NB columns when UPLO is L.

 In order to factorize the panel, the Aasen's algorithm requires the
 last row, or column, of the previous panel. The first row, or column,
 of A is set to be the first row, or column, of an identity matrix,
 which is used to factorize the first panel.

 The resulting J-th row of U, or J-th column of L, is stored in the
 (J-1)-th row, or column, of A (without the unit diagonals), while
 the diagonal and subdiagonal of A are overwritten by those of T.


## Parameters
Uplo : Character*1 [in]
> = 'U':  Upper triangle of A is stored;
> = 'L':  Lower triangle of A is stored.

J1 : Integer [in]
> The location of the first row, or column, of the panel
> within the submatrix of A, passed to this routine, e.g.,
> when called by SSYTRF_AA, for the first panel, J1 is 1,
> while for the remaining panels, J1 is 2.

M : Integer [in]
> The dimension of the submatrix. M >= 0.

Nb : Integer [in]
> The dimension of the panel to be facotorized.

A : Real Array, Dimension (lda,m) For [in,out]
> the first panel, while dimension (LDA,M+1) for the
> remaining panels.
> On entry, A contains the last row, or column, of
> the previous panel, and the trailing submatrix of A
> to be factorized, except for the first panel, only
> the panel is passed.
> On exit, the leading panel is factorized.

Lda : Integer [in]
> The leading dimension of the array A.  LDA >= max(1,M).

Ipiv : Integer Array, Dimension (m) [out]
> Details of the row and column interchanges,
> the row and column k were interchanged with the row and
> column IPIV(k).

H : Real Workspace, Dimension (ldh,nb). [in,out]

Ldh : Integer [in]
> The leading dimension of the workspace H. LDH >= max(1,M).

Work : Real Workspace, Dimension (m). [out]

