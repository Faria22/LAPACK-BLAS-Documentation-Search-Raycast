```fortran
subroutine zgemqr	(	side,
		trans,
		m,
		n,
		k,
		a,
		lda,
		t,
		*     $                   tsize,
		c,
		ldc,
		work,
		lwork,
		info )
```

 ZGEMQR overwrites the general real M-by-N matrix C with

                      SIDE = 'L'     SIDE = 'R'
      TRANS = 'N':      Q * C          C * Q
      TRANS = 'T':      Q**H * C       C * Q**H

 where Q is a complex unitary matrix defined as the product
 of blocked elementary reflectors computed by tall skinny
 QR factorization (ZGEQR)


## Parameters
Side : Character*1 [in]
> = 'L': apply Q or Q**H from the Left;
> = 'R': apply Q or Q**H from the Right.

Trans : Character*1 [in]
> = 'N':  No transpose, apply Q;
> = 'C':  Conjugate transpose, apply Q**H.

M : Integer [in]
> The number of rows of the matrix A.  M >=0.

N : Integer [in]
> The number of columns of the matrix C. N >= 0.

K : Integer [in]
> The number of elementary reflectors whose product defines
> the matrix Q.
> If SIDE = 'L', M >= K >= 0;
> if SIDE = 'R', N >= K >= 0.

A : Complex*16 Array, Dimension (lda,k) [in]
> Part of the data structure to represent Q as returned by ZGEQR.

Lda : Integer [in]
> The leading dimension of the array A.
> If SIDE = 'L', LDA >= max(1,M);
> if SIDE = 'R', LDA >= max(1,N).

T : Complex*16 Array, Dimension (max(5,tsize)). [in]
> Part of the data structure to represent Q as returned by ZGEQR.

Tsize : Integer [in]
> The dimension of the array T. TSIZE >= 5.

C : Complex*16 Array, Dimension (ldc,n) [in,out]
> On entry, the M-by-N matrix C.
> On exit, C is overwritten by Q*C or Q**H*C or C*Q**H or C*Q.

Ldc : Integer [in]
> The leading dimension of the array C. LDC >= max(1,M).

Work : (workspace) Complex*16 Array, Dimension (max(1,lwork)) [out]
> On exit, if INFO = 0, WORK(1) returns the minimal LWORK.

Lwork : Integer [in]
> The dimension of the array WORK. LWORK >= 1.
> If LWORK = -1, then a workspace query is assumed. The routine
> only calculates the size of the WORK array, returns this
> value as WORK(1), and no error message related to WORK
> is issued by XERBLA.

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value

