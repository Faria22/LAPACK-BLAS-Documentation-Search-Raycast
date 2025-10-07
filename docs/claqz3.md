```fortran
subroutine claqz3	(	ilschur,
		ilq,
		ilz,
		n,
		ilo,
		ihi,
		nshifts,
		*     $    nblock_desired,
		alpha,
		beta,
		a,
		lda,
		b,
		ldb,
		q,
		ldq,
		z,
		ldz,
		*     $    qc,
		ldqc,
		zc,
		ldzc,
		work,
		lwork,
		info )
```

 CLAQZ3 Executes a single multishift QZ sweep

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

Nshifts : Integer [in]
> The desired number of shifts to use

Nblock_desired : Integer [in]
> The desired size of the computational windows

Alpha : Complex Array. Sr Contains [in]
> the alpha parts of the shifts to use.

Beta : Complex Array. Ss Contains [in]
> the scale of the shifts to use.

A : Complex Array, Dimension (lda, N) [in,out]

Lda : Integer [in]
> The leading dimension of the array A.  LDA >= max( 1, N ).

B : Complex Array, Dimension (ldb, N) [in,out]

Ldb : Integer [in]
> The leading dimension of the array B.  LDB >= max( 1, N ).

Q : Complex Array, Dimension (ldq, N) [in,out]

Ldq : Integer [in]

Z : Complex Array, Dimension (ldz, N) [in,out]

Ldz : Integer [in]

Qc : Complex Array, Dimension (ldqc, Nblock_desired) [in,out]

Ldqc : Integer [in]

Zc : Complex Array, Dimension (ldzc, Nblock_desired) [in,out]

Ldzc : Integer [in]

Work : Complex Array, Dimension (max(1,lwork)) [out]
> On exit, if INFO >= 0, WORK(1) returns the optimal LWORK.

Lwork : Integer [in]
> The dimension of the array WORK.  LWORK >= max(1,N).
> If LWORK = -1, then a workspace query is assumed; the routine
> only calculates the optimal size of the WORK array, returns
> this value as the first entry of the WORK array, and no error
> message related to LWORK is issued by XERBLA.

Info : Integer [out]
> = 0: successful exit
> < 0: if INFO = -i, the i-th argument had an illegal value

