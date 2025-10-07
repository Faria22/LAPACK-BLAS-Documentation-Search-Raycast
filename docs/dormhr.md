```fortran
subroutine dormhr	(	side,
		trans,
		m,
		n,
		ilo,
		ihi,
		a,
		lda,
		tau,
		c,
		*                          ldc,
		work,
		lwork,
		info )
```

 DORMHR overwrites the general real M-by-N matrix C with

                 SIDE = 'L'     SIDE = 'R'
 TRANS = 'N':      Q * C          C * Q
 TRANS = 'T':      Q**T * C       C * Q**T

 where Q is a real orthogonal matrix of order nq, with nq = m if
 SIDE = 'L' and nq = n if SIDE = 'R'. Q is defined as the product of
 IHI-ILO elementary reflectors, as returned by DGEHRD:

 Q = H(ilo) H(ilo+1) . . . H(ihi-1).

## Parameters
Side : Character*1 [in]
> = 'L': apply Q or Q**T from the Left;
> = 'R': apply Q or Q**T from the Right.

Trans : Character*1 [in]
> = 'N':  No transpose, apply Q;
> = 'T':  Transpose, apply Q**T.

M : Integer [in]
> The number of rows of the matrix C. M >= 0.

N : Integer [in]
> The number of columns of the matrix C. N >= 0.

Ilo : Integer [in]

Ihi : Integer [in]
> ILO and IHI must have the same values as in the previous call
> of DGEHRD. Q is equal to the unit matrix except in the
> submatrix Q(ilo+1:ihi,ilo+1:ihi).
> If SIDE = 'L', then 1 <= ILO <= IHI <= M, if M > 0, and
> ILO = 1 and IHI = 0, if M = 0;
> if SIDE = 'R', then 1 <= ILO <= IHI <= N, if N > 0, and
> ILO = 1 and IHI = 0, if N = 0.

A : Double Precision Array, Dimension [in]
> (LDA,M) if SIDE = 'L'
> (LDA,N) if SIDE = 'R'
> The vectors which define the elementary reflectors, as
> returned by DGEHRD.

Lda : Integer [in]
> The leading dimension of the array A.
> LDA >= max(1,M) if SIDE = 'L'; LDA >= max(1,N) if SIDE = 'R'.

Tau : Double Precision Array, Dimension [in]
> (M-1) if SIDE = 'L'
> (N-1) if SIDE = 'R'
> TAU(i) must contain the scalar factor of the elementary
> reflector H(i), as returned by DGEHRD.

C : Double Precision Array, Dimension (ldc,n) [in,out]
> On entry, the M-by-N matrix C.
> On exit, C is overwritten by Q*C or Q**T*C or C*Q**T or C*Q.

Ldc : Integer [in]
> The leading dimension of the array C. LDC >= max(1,M).

Work : Double Precision Array, Dimension (max(1,lwork)) [out]
> On exit, if INFO = 0, WORK(1) returns the optimal LWORK.

Lwork : Integer [in]
> The dimension of the array WORK.
> If SIDE = 'L', LWORK >= max(1,N);
> if SIDE = 'R', LWORK >= max(1,M).
> For optimum performance LWORK >= N*NB if SIDE = 'L', and
> LWORK >= M*NB if SIDE = 'R', where NB is the optimal
> blocksize.
> If LWORK = -1, then a workspace query is assumed; the routine
> only calculates the optimal size of the WORK array, returns
> this value as the first entry of the WORK array, and no error
> message related to LWORK is issued by XERBLA.

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value

