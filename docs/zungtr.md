```fortran
subroutine zungtr	(	character	uplo,
		integer	n,
		complex*16, dimension(lda, *)	a,
		integer	lda,
		complex*16, dimension(*)	tau,
		complex*16, dimension(*)	work,
		integer	lwork,
		integer	info )
```

 ZUNGTR generates a complex unitary matrix Q which is defined as the
 product of n-1 elementary reflectors of order N, as returned by
 ZHETRD:

 if UPLO = 'U', Q = H(n-1) . . . H(2) H(1),

 if UPLO = 'L', Q = H(1) H(2) . . . H(n-1).

## Parameters
Uplo : Character*1 [in]
> = 'U': Upper triangle of A contains elementary reflectors
> from ZHETRD;
> = 'L': Lower triangle of A contains elementary reflectors
> from ZHETRD.

N : Integer [in]
> The order of the matrix Q. N >= 0.

A : Complex*16 Array, Dimension (lda,n) [in,out]
> On entry, the vectors which define the elementary reflectors,
> as returned by ZHETRD.
> On exit, the N-by-N unitary matrix Q.

Lda : Integer [in]
> The leading dimension of the array A. LDA >= N.

Tau : Complex*16 Array, Dimension (n-1) [in]
> TAU(i) must contain the scalar factor of the elementary
> reflector H(i), as returned by ZHETRD.

Work : Complex*16 Array, Dimension (max(1,lwork)) [out]
> On exit, if INFO = 0, WORK(1) returns the optimal LWORK.

Lwork : Integer [in]
> The dimension of the array WORK. LWORK >= N-1.
> For optimum performance LWORK >= (N-1)*NB, where NB is
> the optimal blocksize.
> If LWORK = -1, then a workspace query is assumed; the routine
> only calculates the optimal size of the WORK array, returns
> this value as the first entry of the WORK array, and no error
> message related to LWORK is issued by XERBLA.

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value

