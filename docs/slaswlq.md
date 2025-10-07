```fortran
subroutine slaswlq	(	m,
		n,
		mb,
		nb,
		a,
		lda,
		t,
		ldt,
		work,
		*                            lwork,
		info )
```

 SLASWLQ computes a blocked Tall-Skinny LQ factorization of
 a real M-by-N matrix A for M <= N:

    A = ( L 0 ) *  Q,

 where:

    Q is a n-by-N orthogonal matrix, stored on exit in an implicit
    form in the elements above the diagonal of the array A and in
    the elements of the array T;
    L is a lower-triangular M-by-M matrix stored on exit in
    the elements on and below the diagonal of the array A.
    0 is a M-by-(N-M) zero matrix, if M < N, and is not stored.


## Parameters
M : Integer [in]
> The number of rows of the matrix A.  M >= 0.

N : Integer [in]
> The number of columns of the matrix A.  N >= M >= 0.

Mb : Integer [in]
> The row block size to be used in the blocked QR.
> M >= MB >= 1

Nb : Integer [in]
> The column block size to be used in the blocked QR.
> NB > 0.

A : Real Array, Dimension (lda,n) [in,out]
> On entry, the M-by-N matrix A.
> On exit, the elements on and below the diagonal
> of the array contain the N-by-N lower triangular matrix L;
> the elements above the diagonal represent Q by the rows
> of blocked V (see Further Details).

Lda : Integer [in]
> The leading dimension of the array A.  LDA >= max(1,M).

T : Real Array, [out]
> dimension (LDT, N * Number_of_row_blocks)
> where Number_of_row_blocks = CEIL((N-M)/(NB-M))
> The blocked upper triangular block reflectors stored in compact form
> as a sequence of upper triangular blocks.
> See Further Details below.

Ldt : Integer [in]
> The leading dimension of the array T.  LDT >= MB.

Work : (workspace) Real Array, Dimension (max(1,lwork)) [out]
> On exit, if INFO = 0, WORK(1) returns the minimal LWORK.

Lwork : Integer [in]
> The dimension of the array WORK.
> LWORK >= 1, if MIN(M,N) = 0, and LWORK >= MB*M, otherwise.
> If LWORK = -1, then a workspace query is assumed; the routine
> only calculates the minimal size of the WORK array, returns
> this value as the first entry of the WORK array, and no error
> message related to LWORK is issued by XERBLA.

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value

