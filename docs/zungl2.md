```fortran
subroutine zungl2	(	integer	m,
		integer	n,
		integer	k,
		complex*16, dimension(lda, *)	a,
		integer	lda,
		complex*16, dimension(*)	tau,
		complex*16, dimension(*)	work,
		integer	info )
```

 ZUNGL2 generates an m-by-n complex matrix Q with orthonormal rows,
 which is defined as the first m rows of a product of k elementary
 reflectors of order n

       Q  =  H(k)**H . . . H(2)**H H(1)**H

 as returned by ZGELQF.

## Parameters
M : Integer [in]
> The number of rows of the matrix Q. M >= 0.

N : Integer [in]
> The number of columns of the matrix Q. N >= M.

K : Integer [in]
> The number of elementary reflectors whose product defines the
> matrix Q. M >= K >= 0.

A : Complex*16 Array, Dimension (lda,n) [in,out]
> On entry, the i-th row must contain the vector which defines
> the elementary reflector H(i), for i = 1,2,...,k, as returned
> by ZGELQF in the first k rows of its array argument A.
> On exit, the m by n matrix Q.

Lda : Integer [in]
> The first dimension of the array A. LDA >= max(1,M).

Tau : Complex*16 Array, Dimension (k) [in]
> TAU(i) must contain the scalar factor of the elementary
> reflector H(i), as returned by ZGELQF.

Work : Complex*16 Array, Dimension (m) [out]

Info : Integer [out]
> = 0: successful exit
> < 0: if INFO = -i, the i-th argument has an illegal value

