```fortran
subroutine ssytri	(	character	uplo,
		integer	n,
		real, dimension(lda, *)	a,
		integer	lda,
		integer, dimension(*)	ipiv,
		real, dimension(*)	work,
		integer	info )
```

 SSYTRI computes the inverse of a real symmetric indefinite matrix
 A using the factorization A = U*D*U**T or A = L*D*L**T computed by
 SSYTRF.

## Parameters
Uplo : Character*1 [in]
> Specifies whether the details of the factorization are stored
> as an upper or lower triangular matrix.
> = 'U':  Upper triangular, form is A = U*D*U**T;
> = 'L':  Lower triangular, form is A = L*D*L**T.

N : Integer [in]
> The order of the matrix A.  N >= 0.

A : Real Array, Dimension (lda,n) [in,out]
> On entry, the block diagonal matrix D and the multipliers
> used to obtain the factor U or L as computed by SSYTRF.
> On exit, if INFO = 0, the (symmetric) inverse of the original
> matrix.  If UPLO = 'U', the upper triangular part of the
> inverse is formed and the part of A below the diagonal is not
> referenced; if UPLO = 'L' the lower triangular part of the
> inverse is formed and the part of A above the diagonal is
> not referenced.

Lda : Integer [in]
> The leading dimension of the array A.  LDA >= max(1,N).

Ipiv : Integer Array, Dimension (n) [in]
> Details of the interchanges and the block structure of D
> as determined by SSYTRF.

Work : Real Array, Dimension (n) [out]

Info : Integer [out]
> = 0: successful exit
> < 0: if INFO = -i, the i-th argument had an illegal value
> > 0: if INFO = i, D(i,i) = 0; the matrix is singular and its
> inverse could not be computed.

