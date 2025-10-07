```fortran
subroutine zunmhr (
		side,
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
		info
)
```

 ZUNMHR overwrites the general complex M-by-N matrix C with

                 SIDE = 'L'     SIDE = 'R'
 TRANS = 'N':      Q * C          C * Q
 TRANS = 'C':      Q**H * C       C * Q**H

 where Q is a complex unitary matrix of order nq, with nq = m if
 SIDE = 'L' and nq = n if SIDE = 'R'. Q is defined as the product of
 IHI-ILO elementary reflectors, as returned by ZGEHRD:

 Q = H(ilo) H(ilo+1) . . . H(ihi-1).

## Parameters
Side : Character*1 [in]
> = 'L': apply Q or Q**H from the Left;
> = 'R': apply Q or Q**H from the Right.

Trans : Character*1 [in]
> = 'N': apply Q  (No transpose)
> = 'C': apply Q**H (Conjugate transpose)

M : Integer [in]
> The number of rows of the matrix C. M >= 0.

N : Integer [in]
> The number of columns of the matrix C. N >= 0.

Ilo : Integer [in]

Ihi : Integer [in]
> ILO and IHI must have the same values as in the previous call
> of ZGEHRD. Q is equal to the unit matrix except in the
> submatrix Q(ilo+1:ihi,ilo+1:ihi).
> If SIDE = 'L', then 1 <= ILO <= IHI <= M, if M > 0, and
> ILO = 1 and IHI = 0, if M = 0;
> if SIDE = 'R', then 1 <= ILO <= IHI <= N, if N > 0, and
> ILO = 1 and IHI = 0, if N = 0.

A : Complex*16 Array, Dimension [in]
> (LDA,M) if SIDE = 'L'
> (LDA,N) if SIDE = 'R'
> The vectors which define the elementary reflectors, as
> returned by ZGEHRD.

Lda : Integer [in]
> The leading dimension of the array A.
> LDA >= max(1,M) if SIDE = 'L'; LDA >= max(1,N) if SIDE = 'R'.

Tau : Complex*16 Array, Dimension [in]
> (M-1) if SIDE = 'L'
> (N-1) if SIDE = 'R'
> TAU(i) must contain the scalar factor of the elementary
> reflector H(i), as returned by ZGEHRD.

C : Complex*16 Array, Dimension (ldc,n) [in,out]
> On entry, the M-by-N matrix C.
> On exit, C is overwritten by Q*C or Q**H*C or C*Q**H or C*Q.

Ldc : Integer [in]
> The leading dimension of the array C. LDC >= max(1,M).

Work : Complex*16 Array, Dimension (max(1,lwork)) [out]
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

