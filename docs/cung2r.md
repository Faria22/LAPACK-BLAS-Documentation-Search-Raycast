```fortran
subroutine cung2r	(	integer	m,
		integer	n,
		integer	k,
		complex, dimension(lda, *)	a,
		integer	lda,
		complex, dimension(*)	tau,
		complex, dimension(*)	work,
		integer	info )
```

 CUNG2R generates an m by n complex matrix Q with orthonormal columns,
 which is defined as the first n columns of a product of k elementary
 reflectors of order m

       Q  =  H(1) H(2) . . . H(k)

 as returned by CGEQRF.

## Parameters
M : Integer [in]
> The number of rows of the matrix Q. M >= 0.

N : Integer [in]
> The number of columns of the matrix Q. M >= N >= 0.

K : Integer [in]
> The number of elementary reflectors whose product defines the
> matrix Q. N >= K >= 0.

A : Complex Array, Dimension (lda,n) [in,out]
> On entry, the i-th column must contain the vector which
> defines the elementary reflector H(i), for i = 1,2,...,k, as
> returned by CGEQRF in the first k columns of its array
> argument A.
> On exit, the m by n matrix Q.

Lda : Integer [in]
> The first dimension of the array A. LDA >= max(1,M).

Tau : Complex Array, Dimension (k) [in]
> TAU(i) must contain the scalar factor of the elementary
> reflector H(i), as returned by CGEQRF.

Work : Complex Array, Dimension (n) [out]

Info : Integer [out]
> = 0: successful exit
> < 0: if INFO = -i, the i-th argument has an illegal value

