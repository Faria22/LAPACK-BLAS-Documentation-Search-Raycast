```fortran
subroutine slamswlq	(	side,
		trans,
		m,
		n,
		k,
		mb,
		nb,
		a,
		lda,
		t,
		*     $                ldt,
		c,
		ldc,
		work,
		lwork,
		info )
```

    SLAMSWLQ overwrites the general real M-by-N matrix C with


                    SIDE = 'L'     SIDE = 'R'
    TRANS = 'N':      Q * C          C * Q
    TRANS = 'T':      Q**T * C       C * Q**T
    where Q is a real orthogonal matrix defined as the product of blocked
    elementary reflectors computed by short wide LQ
    factorization (SLASWLQ)

## Parameters
Side : Character*1 [in]
> = 'L': apply Q or Q**T from the Left;
> = 'R': apply Q or Q**T from the Right.

Trans : Character*1 [in]
> = 'N':  No transpose, apply Q;
> = 'T':  Transpose, apply Q**T.

M : Integer [in]
> The number of rows of the matrix C.  M >=0.

N : Integer [in]
> The number of columns of the matrix C. N >= 0.

K : Integer [in]
> The number of elementary reflectors whose product defines
> the matrix Q.
> M >= K >= 0;

Mb : Integer [in]
> The row block size to be used in the blocked LQ.
> M >= MB >= 1

Nb : Integer [in]
> The column block size to be used in the blocked LQ.
> NB > M.

A : Real Array, Dimension [in]
> (LDA,M) if SIDE = 'L',
> (LDA,N) if SIDE = 'R'
> The i-th row must contain the vector which defines the blocked
> elementary reflector H(i), for i = 1,2,...,k, as returned by
> SLASWLQ in the first k rows of its array argument A.

Lda : Integer [in]
> The leading dimension of the array A. LDA >= max(1,K).

T : Real Array, Dimension [in]
> ( M * Number of blocks(CEIL(N-K/NB-K)),
> The blocked upper triangular block reflectors stored in compact form
> as a sequence of upper triangular blocks.  See below
> for further details.

Ldt : Integer [in]
> The leading dimension of the array T.  LDT >= MB.

C : Real Array, Dimension (ldc,n) [in,out]
> On entry, the M-by-N matrix C.
> On exit, C is overwritten by Q*C or Q**T*C or C*Q**T or C*Q.

Ldc : Integer [in]
> The leading dimension of the array C. LDC >= max(1,M).

Work : (workspace) Real Array, Dimension (max(1,lwork)) [out]
> On exit, if INFO = 0, WORK(1) returns the minimal LWORK.

Lwork : Integer [in]
> The dimension of the array WORK.
> If MIN(M,N,K) = 0, LWORK >= 1.
> If SIDE = 'L', LWORK >= max(1,NB*MB).
> If SIDE = 'R', LWORK >= max(1,M*MB).
> If LWORK = -1, then a workspace query is assumed; the routine
> only calculates the minimal size of the WORK array, returns
> this value as the first entry of the WORK array, and no error
> message related to LWORK is issued by XERBLA.

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value

