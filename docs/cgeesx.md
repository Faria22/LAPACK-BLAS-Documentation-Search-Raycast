```fortran
subroutine cgeesx	(	jobvs,
		sort,
		select,
		sense,
		n,
		a,
		lda,
		sdim,
		w,
		*                          vs,
		ldvs,
		rconde,
		rcondv,
		work,
		lwork,
		rwork,
		*                          bwork,
		info )
```

 CGEESX computes for an N-by-N complex nonsymmetric matrix A, the
 eigenvalues, the Schur form T, and, optionally, the matrix of Schur
 vectors Z.  This gives the Schur factorization A = Z*T*(Z**H).

 Optionally, it also orders the eigenvalues on the diagonal of the
 Schur form so that selected eigenvalues are at the top left;
 computes a reciprocal condition number for the average of the
 selected eigenvalues (RCONDE); and computes a reciprocal condition
 number for the right invariant subspace corresponding to the
 selected eigenvalues (RCONDV).  The leading columns of Z form an
 orthonormal basis for this invariant subspace.

 For further explanation of the reciprocal condition numbers RCONDE
 and RCONDV, see Section 4.10 of the LAPACK Users' Guide (where
 these quantities are called s and sep respectively).

 A complex matrix is in Schur form if it is upper triangular.

## Parameters
Jobvs : Character*1 [in]
> = 'N': Schur vectors are not computed;
> = 'V': Schur vectors are computed.

Sort : Character*1 [in]
> Specifies whether or not to order the eigenvalues on the
> diagonal of the Schur form.
> = 'N': Eigenvalues are not ordered;
> = 'S': Eigenvalues are ordered (see SELECT).

Select : a Logical Function of One Complex Argument [in]
> SELECT must be declared EXTERNAL in the calling subroutine.
> If SORT = 'S', SELECT is used to select eigenvalues to order
> to the top left of the Schur form.
> If SORT = 'N', SELECT is not referenced.
> An eigenvalue W(j) is selected if SELECT(W(j)) is true.

Sense : Character*1 [in]
> Determines which reciprocal condition numbers are computed.
> = 'N': None are computed;
> = 'E': Computed for average of selected eigenvalues only;
> = 'V': Computed for selected right invariant subspace only;
> = 'B': Computed for both.
> If SENSE = 'E', 'V' or 'B', SORT must equal 'S'.

N : Integer [in]
> The order of the matrix A. N >= 0.

A : Complex Array, Dimension (lda, N) [in,out]
> On entry, the N-by-N matrix A.
> On exit, A is overwritten by its Schur form T.

Lda : Integer [in]
> The leading dimension of the array A.  LDA >= max(1,N).

Sdim : Integer [out]
> If SORT = 'N', SDIM = 0.
> If SORT = 'S', SDIM = number of eigenvalues for which
> SELECT is true.

W : Complex Array, Dimension (n) [out]
> W contains the computed eigenvalues, in the same order
> that they appear on the diagonal of the output Schur form T.

Vs : Complex Array, Dimension (ldvs,n) [out]
> If JOBVS = 'V', VS contains the unitary matrix Z of Schur
> vectors.
> If JOBVS = 'N', VS is not referenced.

Ldvs : Integer [in]
> The leading dimension of the array VS.  LDVS >= 1, and if
> JOBVS = 'V', LDVS >= N.

Rconde : Real [out]
> If SENSE = 'E' or 'B', RCONDE contains the reciprocal
> condition number for the average of the selected eigenvalues.
> Not referenced if SENSE = 'N' or 'V'.

Rcondv : Real [out]
> If SENSE = 'V' or 'B', RCONDV contains the reciprocal
> condition number for the selected right invariant subspace.
> Not referenced if SENSE = 'N' or 'E'.

Work : Complex Array, Dimension (max(1,lwork)) [out]
> On exit, if INFO = 0, WORK(1) returns the optimal LWORK.

Lwork : Integer [in]
> The dimension of the array WORK.  LWORK >= max(1,2*N).
> Also, if SENSE = 'E' or 'V' or 'B', LWORK >= 2*SDIM*(N-SDIM),
> where SDIM is the number of selected eigenvalues computed by
> this routine.  Note that 2*SDIM*(N-SDIM) <= N*N/2. Note also
> that an error is only returned if LWORK < max(1,2*N), but if
> SENSE = 'E' or 'V' or 'B' this may not be large enough.
> For good performance, LWORK must generally be larger.
> If LWORK = -1, then a workspace query is assumed; the routine
> only calculates upper bound on the optimal size of the
> array WORK, returns this value as the first entry of the WORK
> array, and no error message related to LWORK is issued by
> XERBLA.

Rwork : Real Array, Dimension (n) [out]

Bwork : Logical Array, Dimension (n) [out]
> Not referenced if SORT = 'N'.

Info : Integer [out]
> = 0: successful exit
> < 0: if INFO = -i, the i-th argument had an illegal value.
> > 0: if INFO = i, and i is
> <= N: the QR algorithm failed to compute all the
> eigenvalues; elements 1:ILO-1 and i+1:N of W
> contain those eigenvalues which have converged; if
> JOBVS = 'V', VS contains the transformation which
> reduces A to its partially converged Schur form.
> = N+1: the eigenvalues could not be reordered because some
> eigenvalues were too close to separate (the problem
> is very ill-conditioned);
> = N+2: after reordering, roundoff changed values of some
> complex eigenvalues so that leading eigenvalues in
> the Schur form no longer satisfy SELECT=.TRUE.  This
> could also be caused by underflow due to scaling.

