```fortran
subroutine clatrz	(	integer	m,
		integer	n,
		integer	l,
		complex, dimension(lda, *)	a,
		integer	lda,
		complex, dimension(*)	tau,
		complex, dimension(*)	work )
```

 CLATRZ factors the M-by-(M+L) complex upper trapezoidal matrix
 [ A1 A2 ] = [ A(1:M,1:M) A(1:M,N-L+1:N) ] as ( R  0 ) * Z by means
 of unitary transformations, where  Z is an (M+L)-by-(M+L) unitary
 matrix and, R and A1 are M-by-M upper triangular matrices.

## Parameters
M : Integer [in]
> The number of rows of the matrix A.  M >= 0.

N : Integer [in]
> The number of columns of the matrix A.  N >= 0.

L : Integer [in]
> The number of columns of the matrix A containing the
> meaningful part of the Householder vectors. N-M >= L >= 0.

A : Complex Array, Dimension (lda,n) [in,out]
> On entry, the leading M-by-N upper trapezoidal part of the
> array A must contain the matrix to be factorized.
> On exit, the leading M-by-M upper triangular part of A
> contains the upper triangular matrix R, and elements N-L+1 to
> N of the first M rows of A, with the array TAU, represent the
> unitary matrix Z as a product of M elementary reflectors.

Lda : Integer [in]
> The leading dimension of the array A.  LDA >= max(1,M).

Tau : Complex Array, Dimension (m) [out]
> The scalar factors of the elementary reflectors.

Work : Complex Array, Dimension (m) [out]

