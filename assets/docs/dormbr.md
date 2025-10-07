```fortran
subroutine dormbr (
		vect,
		side,
		trans,
		m,
		n,
		k,
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

 If VECT = 'Q', DORMBR overwrites the general real M-by-N matrix C
 with
                 SIDE = 'L'     SIDE = 'R'
 TRANS = 'N':      Q * C          C * Q
 TRANS = 'T':      Q**T * C       C * Q**T

 If VECT = 'P', DORMBR overwrites the general real M-by-N matrix C
 with
                 SIDE = 'L'     SIDE = 'R'
 TRANS = 'N':      P * C          C * P
 TRANS = 'T':      P**T * C       C * P**T

 Here Q and P**T are the orthogonal matrices determined by DGEBRD when
 reducing a real matrix A to bidiagonal form: A = Q * B * P**T. Q and
 P**T are defined as products of elementary reflectors H(i) and G(i)
 respectively.

 Let nq = m if SIDE = 'L' and nq = n if SIDE = 'R'. Thus nq is the
 order of the orthogonal matrix Q or P**T that is applied.

 If VECT = 'Q', A is assumed to have been an NQ-by-K matrix:
 if nq >= k, Q = H(1) H(2) . . . H(k);
 if nq < k, Q = H(1) H(2) . . . H(nq-1).

 If VECT = 'P', A is assumed to have been a K-by-NQ matrix:
 if k < nq, P = G(1) G(2) . . . G(k);
 if k >= nq, P = G(1) G(2) . . . G(nq-1).

## Parameters
Vect : Character*1 [in]
> = 'Q': apply Q or Q**T;
> = 'P': apply P or P**T.

Side : Character*1 [in]
> = 'L': apply Q, Q**T, P or P**T from the Left;
> = 'R': apply Q, Q**T, P or P**T from the Right.

Trans : Character*1 [in]
> = 'N':  No transpose, apply Q  or P;
> = 'T':  Transpose, apply Q**T or P**T.

M : Integer [in]
> The number of rows of the matrix C. M >= 0.

N : Integer [in]
> The number of columns of the matrix C. N >= 0.

K : Integer [in]
> If VECT = 'Q', the number of columns in the original
> matrix reduced by DGEBRD.
> If VECT = 'P', the number of rows in the original
> matrix reduced by DGEBRD.
> K >= 0.

A : Double Precision Array, Dimension [in]
> (LDA,min(nq,K)) if VECT = 'Q'
> (LDA,nq)        if VECT = 'P'
> The vectors which define the elementary reflectors H(i) and
> G(i), whose products determine the matrices Q and P, as
> returned by DGEBRD.

Lda : Integer [in]
> The leading dimension of the array A.
> If VECT = 'Q', LDA >= max(1,nq);
> if VECT = 'P', LDA >= max(1,min(nq,K)).

Tau : Double Precision Array, Dimension (min(nq,k)) [in]
> TAU(i) must contain the scalar factor of the elementary
> reflector H(i) or G(i) which determines Q or P, as returned
> by DGEBRD in the array argument TAUQ or TAUP.

C : Double Precision Array, Dimension (ldc,n) [in,out]
> On entry, the M-by-N matrix C.
> On exit, C is overwritten by Q*C or Q**T*C or C*Q**T or C*Q
> or P*C or P**T*C or C*P or C*P**T.

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

