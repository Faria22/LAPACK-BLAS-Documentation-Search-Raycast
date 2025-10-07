```fortran
subroutine zlaqz2	(	ilschur,
		ilq,
		ilz,
		n,
		ilo,
		ihi,
		nw,
		a,
		lda,
		b,
		*     $    ldb,
		q,
		ldq,
		z,
		ldz,
		ns,
		nd,
		alpha,
		beta,
		qc,
		ldqc,
		zc,
		ldzc,
		*     $    work,
		lwork,
		rwork,
		rec,
		info )
```

 ZLAQZ2 performs AED

## Parameters
Ilschur : Logical [in]
> Determines whether or not to update the full Schur form

Ilq : Logical [in]
> Determines whether or not to update the matrix Q

Ilz : Logical [in]
> Determines whether or not to update the matrix Z

N : Integer [in]
> The order of the matrices A, B, Q, and Z.  N >= 0.

Ilo : Integer [in]

Ihi : Integer [in]
> ILO and IHI mark the rows and columns of (A,B) which
> are to be normalized

Nw : Integer [in]
> The desired size of the deflation window.

A : Complex*16 Array, Dimension (lda, N) [in,out]

Lda : Integer [in]
> The leading dimension of the array A.  LDA >= max( 1, N ).

B : Complex*16 Array, Dimension (ldb, N) [in,out]

Ldb : Integer [in]
> The leading dimension of the array B.  LDB >= max( 1, N ).

Q : Complex*16 Array, Dimension (ldq, N) [in,out]

Ldq : Integer [in]

Z : Complex*16 Array, Dimension (ldz, N) [in,out]

Ldz : Integer [in]

Ns : Integer [out]
> The number of unconverged eigenvalues available to
> use as shifts.

Nd : Integer [out]
> The number of converged eigenvalues found.

Alpha : Complex*16 Array, Dimension (n) [out]
> Each scalar alpha defining an eigenvalue
> of GNEP.

Beta : Complex*16 Array, Dimension (n) [out]
> The scalars beta that define the eigenvalues of GNEP.
> Together, the quantities alpha = ALPHA(j) and
> beta = BETA(j) represent the j-th eigenvalue of the matrix
> pair (A,B), in one of the forms lambda = alpha/beta or
> mu = beta/alpha.  Since either lambda or mu may overflow,
> they should not, in general, be computed.

Qc : Complex*16 Array, Dimension (ldqc, Nw) [in,out]

Ldqc : Integer [in]

Zc : Complex*16 Array, Dimension (ldzc, Nw) [in,out]

Ldzc : Integer [in]

Work : Complex*16 Array, Dimension (max(1,lwork)) [out]
> On exit, if INFO >= 0, WORK(1) returns the optimal LWORK.

Lwork : Integer [in]
> The dimension of the array WORK.  LWORK >= max(1,N).
> If LWORK = -1, then a workspace query is assumed; the routine
> only calculates the optimal size of the WORK array, returns
> this value as the first entry of the WORK array, and no error
> message related to LWORK is issued by XERBLA.

Rwork : Double Precision Array, Dimension (n) [out]

Rec : Integer [in]
> REC indicates the current recursion level. Should be set
> to 0 on first call.

Info : Integer [out]
> = 0: successful exit
> < 0: if INFO = -i, the i-th argument had an illegal value

