```fortran
subroutine cgeqp3	(	m,
		n,
		a,
		lda,
		jpvt,
		tau,
		work,
		lwork,
		rwork,
		*                          info )
```

 CGEQP3 computes a QR factorization with column pivoting of a
 matrix A:  A*P = Q*R  using Level 3 BLAS.

## Parameters
M : Integer [in]
> The number of rows of the matrix A. M >= 0.

N : Integer [in]
> The number of columns of the matrix A.  N >= 0.

A : Complex Array, Dimension (lda,n) [in,out]
> On entry, the M-by-N matrix A.
> On exit, the upper triangle of the array contains the
> min(M,N)-by-N upper trapezoidal matrix R; the elements below
> the diagonal, together with the array TAU, represent the
> unitary matrix Q as a product of min(M,N) elementary
> reflectors.

Lda : Integer [in]
> The leading dimension of the array A. LDA >= max(1,M).

Jpvt : Integer Array, Dimension (n) [in,out]
> On entry, if JPVT(J).ne.0, the J-th column of A is permuted
> to the front of A*P (a leading column); if JPVT(J)=0,
> the J-th column of A is a free column.
> On exit, if JPVT(J)=K, then the J-th column of A*P was the
> the K-th column of A.

Tau : Complex Array, Dimension (min(m,n)) [out]
> The scalar factors of the elementary reflectors.

Work : Complex Array, Dimension (max(1,lwork)) [out]
> On exit, if INFO=0, WORK(1) returns the optimal LWORK.

Lwork : Integer [in]
> The dimension of the array WORK. LWORK >= N+1.
> For optimal performance LWORK >= ( N+1 )*NB, where NB
> is the optimal blocksize.
> If LWORK = -1, then a workspace query is assumed; the routine
> only calculates the optimal size of the WORK array, returns
> this value as the first entry of the WORK array, and no error
> message related to LWORK is issued by XERBLA.

Rwork : Real Array, Dimension (2*n) [out]

Info : Integer [out]
> = 0: successful exit.
> < 0: if INFO = -i, the i-th argument had an illegal value.

