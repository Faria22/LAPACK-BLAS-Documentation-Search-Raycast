```fortran
subroutine sorgtr	(	character	uplo,
		integer	n,
		real, dimension(lda, *)	a,
		integer	lda,
		real, dimension(*)	tau,
		real, dimension(*)	work,
		integer	lwork,
		integer	info )
```

 SORGTR generates a real orthogonal matrix Q which is defined as the
 product of n-1 elementary reflectors of order N, as returned by
 SSYTRD:

 if UPLO = 'U', Q = H(n-1) . . . H(2) H(1),

 if UPLO = 'L', Q = H(1) H(2) . . . H(n-1).

## Parameters
Uplo : Character*1 [in]
> = 'U': Upper triangle of A contains elementary reflectors
> from SSYTRD;
> = 'L': Lower triangle of A contains elementary reflectors
> from SSYTRD.

N : Integer [in]
> The order of the matrix Q. N >= 0.

A : Real Array, Dimension (lda,n) [in,out]
> On entry, the vectors which define the elementary reflectors,
> as returned by SSYTRD.
> On exit, the N-by-N orthogonal matrix Q.

Lda : Integer [in]
> The leading dimension of the array A. LDA >= max(1,N).

Tau : Real Array, Dimension (n-1) [in]
> TAU(i) must contain the scalar factor of the elementary
> reflector H(i), as returned by SSYTRD.

Work : Real Array, Dimension (max(1,lwork)) [out]
> On exit, if INFO = 0, WORK(1) returns the optimal LWORK.

Lwork : Integer [in]
> The dimension of the array WORK. LWORK >= max(1,N-1).
> For optimum performance LWORK >= (N-1)*NB, where NB is
> the optimal blocksize.
> If LWORK = -1, then a workspace query is assumed; the routine
> only calculates the optimal size of the WORK array, returns
> this value as the first entry of the WORK array, and no error
> message related to LWORK is issued by XERBLA.

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value

