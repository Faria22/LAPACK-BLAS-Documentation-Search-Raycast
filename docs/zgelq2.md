```fortran
subroutine zgelq2	(	integer	m,
		integer	n,
		complex*16, dimension(lda, *)	a,
		integer	lda,
		complex*16, dimension(*)	tau,
		complex*16, dimension(*)	work,
		integer	info )
```

 ZGELQ2 computes an LQ factorization of a complex m-by-n matrix A:

    A = ( L 0 ) *  Q

 where:

    Q is a n-by-n orthogonal matrix;
    L is a lower-triangular m-by-m matrix;
    0 is a m-by-(n-m) zero matrix, if m < n.


## Parameters
M : Integer [in]
> The number of rows of the matrix A.  M >= 0.

N : Integer [in]
> The number of columns of the matrix A.  N >= 0.

A : Complex*16 Array, Dimension (lda,n) [in,out]
> On entry, the m by n matrix A.
> On exit, the elements on and below the diagonal of the array
> contain the m by min(m,n) lower trapezoidal matrix L (L is
> lower triangular if m <= n); the elements above the diagonal,
> with the array TAU, represent the unitary matrix Q as a
> product of elementary reflectors (see Further Details).

Lda : Integer [in]
> The leading dimension of the array A.  LDA >= max(1,M).

Tau : Complex*16 Array, Dimension (min(m,n)) [out]
> The scalar factors of the elementary reflectors (see Further
> Details).

Work : Complex*16 Array, Dimension (m) [out]

Info : Integer [out]
> = 0: successful exit
> < 0: if INFO = -i, the i-th argument had an illegal value

