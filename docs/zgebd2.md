```fortran
subroutine zgebd2	(	integer	m,
		integer	n,
		complex*16, dimension(lda, *)	a,
		integer	lda,
		double precision, dimension(*)	d,
		double precision, dimension(*)	e,
		complex*16, dimension(*)	tauq,
		complex*16, dimension(*)	taup,
		complex*16, dimension(*)	work,
		integer	info )
```

 ZGEBD2 reduces a complex general m by n matrix A to upper or lower
 real bidiagonal form B by a unitary transformation: Q**H * A * P = B.

 If m >= n, B is upper bidiagonal; if m < n, B is lower bidiagonal.

## Parameters
M : Integer [in]
> The number of rows in the matrix A.  M >= 0.

N : Integer [in]
> The number of columns in the matrix A.  N >= 0.

A : Complex*16 Array, Dimension (lda,n) [in,out]
> On entry, the m by n general matrix to be reduced.
> On exit,
> if m >= n, the diagonal and the first superdiagonal are
> overwritten with the upper bidiagonal matrix B; the
> elements below the diagonal, with the array TAUQ, represent
> the unitary matrix Q as a product of elementary
> reflectors, and the elements above the first superdiagonal,
> with the array TAUP, represent the unitary matrix P as
> a product of elementary reflectors;
> if m < n, the diagonal and the first subdiagonal are
> overwritten with the lower bidiagonal matrix B; the
> elements below the first subdiagonal, with the array TAUQ,
> represent the unitary matrix Q as a product of
> elementary reflectors, and the elements above the diagonal,
> with the array TAUP, represent the unitary matrix P as
> a product of elementary reflectors.
> See Further Details.

Lda : Integer [in]
> The leading dimension of the array A.  LDA >= max(1,M).

D : Double Precision Array, Dimension (min(m,n)) [out]
> The diagonal elements of the bidiagonal matrix B:
> D(i) = A(i,i).

E : Double Precision Array, Dimension (min(m,n)-1) [out]
> The off-diagonal elements of the bidiagonal matrix B:
> if m >= n, E(i) = A(i,i+1) for i = 1,2,...,n-1;
> if m < n, E(i) = A(i+1,i) for i = 1,2,...,m-1.

Tauq : Complex*16 Array, Dimension (min(m,n)) [out]
> The scalar factors of the elementary reflectors which
> represent the unitary matrix Q. See Further Details.

Taup : Complex*16 Array, Dimension (min(m,n)) [out]
> The scalar factors of the elementary reflectors which
> represent the unitary matrix P. See Further Details.

Work : Complex*16 Array, Dimension (max(m,n)) [out]

Info : Integer [out]
> = 0: successful exit
> < 0: if INFO = -i, the i-th argument had an illegal value.

