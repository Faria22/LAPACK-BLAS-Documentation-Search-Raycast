```fortran
subroutine zlatrd	(	character	uplo,
		integer	n,
		integer	nb,
		complex*16, dimension(lda, *)	a,
		integer	lda,
		double precision, dimension(*)	e,
		complex*16, dimension(*)	tau,
		complex*16, dimension(ldw, *)	w,
		integer	ldw )
```

 ZLATRD reduces NB rows and columns of a complex Hermitian matrix A to
 Hermitian tridiagonal form by a unitary similarity
 transformation Q**H * A * Q, and returns the matrices V and W which are
 needed to apply the transformation to the unreduced part of A.

 If UPLO = 'U', ZLATRD reduces the last NB rows and columns of a
 matrix, of which the upper triangle is supplied;
 if UPLO = 'L', ZLATRD reduces the first NB rows and columns of a
 matrix, of which the lower triangle is supplied.

 This is an auxiliary routine called by ZHETRD.

## Parameters
Uplo : Character*1 [in]
> Specifies whether the upper or lower triangular part of the
> Hermitian matrix A is stored:
> = 'U': Upper triangular
> = 'L': Lower triangular

N : Integer [in]
> The order of the matrix A.

Nb : Integer [in]
> The number of rows and columns to be reduced.

A : Complex*16 Array, Dimension (lda,n) [in,out]
> On entry, the Hermitian matrix A.  If UPLO = 'U', the leading
> n-by-n upper triangular part of A contains the upper
> triangular part of the matrix A, and the strictly lower
> triangular part of A is not referenced.  If UPLO = 'L', the
> leading n-by-n lower triangular part of A contains the lower
> triangular part of the matrix A, and the strictly upper
> triangular part of A is not referenced.
> On exit:
> if UPLO = 'U', the last NB columns have been reduced to
> tridiagonal form, with the diagonal elements overwriting
> the diagonal elements of A; the elements above the diagonal
> with the array TAU, represent the unitary matrix Q as a
> product of elementary reflectors;
> if UPLO = 'L', the first NB columns have been reduced to
> tridiagonal form, with the diagonal elements overwriting
> the diagonal elements of A; the elements below the diagonal
> with the array TAU, represent the  unitary matrix Q as a
> product of elementary reflectors.
> See Further Details.

Lda : Integer [in]
> The leading dimension of the array A.  LDA >= max(1,N).

E : Double Precision Array, Dimension (n-1) [out]
> If UPLO = 'U', E(n-nb:n-1) contains the superdiagonal
> elements of the last NB columns of the reduced matrix;
> if UPLO = 'L', E(1:nb) contains the subdiagonal elements of
> the first NB columns of the reduced matrix.

Tau : Complex*16 Array, Dimension (n-1) [out]
> The scalar factors of the elementary reflectors, stored in
> TAU(n-nb:n-1) if UPLO = 'U', and in TAU(1:nb) if UPLO = 'L'.
> See Further Details.

W : Complex*16 Array, Dimension (ldw,nb) [out]
> The n-by-nb matrix W required to update the unreduced part
> of A.

Ldw : Integer [in]
> The leading dimension of the array W. LDW >= max(1,N).

