```fortran
subroutine clahqr	(	wantt,
		wantz,
		n,
		ilo,
		ihi,
		h,
		ldh,
		w,
		iloz,
		*                          ihiz,
		z,
		ldz,
		info )
```

    CLAHQR is an auxiliary routine called by CHSEQR to update the
    eigenvalues and Schur decomposition already computed by CHSEQR, by
    dealing with the Hessenberg submatrix in rows and columns ILO to
    IHI.

## Parameters
Wantt : Logical [in]
> = .TRUE. : the full Schur form T is required;
> = .FALSE.: only eigenvalues are required.

Wantz : Logical [in]
> = .TRUE. : the matrix of Schur vectors Z is required;
> = .FALSE.: Schur vectors are not required.

N : Integer [in]
> The order of the matrix H.  N >= 0.

Ilo : Integer [in]

Ihi : Integer [in]
> It is assumed that H is already upper triangular in rows and
> columns IHI+1:N, and that H(ILO,ILO-1) = 0 (unless ILO = 1).
> CLAHQR works primarily with the Hessenberg submatrix in rows
> and columns ILO to IHI, but applies transformations to all of
> H if WANTT is .TRUE..
> 1 <= ILO <= max(1,IHI); IHI <= N.

H : Complex Array, Dimension (ldh,n) [in,out]
> On entry, the upper Hessenberg matrix H.
> On exit, if INFO is zero and if WANTT is .TRUE., then H
> is upper triangular in rows and columns ILO:IHI.  If INFO
> is zero and if WANTT is .FALSE., then the contents of H
> are unspecified on exit.  The output state of H in case
> INF is positive is below under the description of INFO.

Ldh : Integer [in]
> The leading dimension of the array H. LDH >= max(1,N).

W : Complex Array, Dimension (n) [out]
> The computed eigenvalues ILO to IHI are stored in the
> corresponding elements of W. If WANTT is .TRUE., the
> eigenvalues are stored in the same order as on the diagonal
> of the Schur form returned in H, with W(i) = H(i,i).

Iloz : Integer [in]

Ihiz : Integer [in]
> Specify the rows of Z to which transformations must be
> applied if WANTZ is .TRUE..
> 1 <= ILOZ <= ILO; IHI <= IHIZ <= N.

Z : Complex Array, Dimension (ldz,n) [in,out]
> If WANTZ is .TRUE., on entry Z must contain the current
> matrix Z of transformations accumulated by CHSEQR, and on
> exit Z has been updated; transformations are applied only to
> the submatrix Z(ILOZ:IHIZ,ILO:IHI).
> If WANTZ is .FALSE., Z is not referenced.

Ldz : Integer [in]
> The leading dimension of the array Z. LDZ >= max(1,N).

Info : Integer [out]
> = 0:  successful exit
> > 0:  if INFO = i, CLAHQR failed to compute all the
> eigenvalues ILO to IHI in a total of 30 iterations
> per eigenvalue; elements i+1:ihi of W contain
> those eigenvalues which have been successfully
> computed.
> If INFO > 0 and WANTT is .FALSE., then on exit,
> the remaining unconverged eigenvalues are the
> eigenvalues of the upper Hessenberg matrix
> rows and columns ILO through INFO of the final,
> output value of H.
> If INFO > 0 and WANTT is .TRUE., then on exit
> (*)       (initial value of H)*U  = U*(final value of H)
> where U is an orthogonal matrix.    The final
> value of H is upper Hessenberg and triangular in
> rows and columns INFO+1 through IHI.
> If INFO > 0 and WANTZ is .TRUE., then on exit
> (final value of Z)  = (initial value of Z)*U
> where U is the orthogonal matrix in (*)
> (regardless of the value of WANTT.)

