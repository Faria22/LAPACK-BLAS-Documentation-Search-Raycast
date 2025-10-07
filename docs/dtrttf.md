```fortran
subroutine dtrttf	(	character	transr,
		character	uplo,
		integer	n,
		double precision, dimension(0: lda-1, 0: *)	a,
		integer	lda,
		double precision, dimension(0: *)	arf,
		integer	info )
```

 DTRTTF copies a triangular matrix A from standard full format (TR)
 to rectangular full packed format (TF) .

## Parameters
Transr : Character*1 [in]
> = 'N':  ARF in Normal form is wanted;
> = 'T':  ARF in Transpose form is wanted.

Uplo : Character*1 [in]
> = 'U':  Upper triangle of A is stored;
> = 'L':  Lower triangle of A is stored.

N : Integer [in]
> The order of the matrix A. N >= 0.

A : Double Precision Array, Dimension (lda,n). [in]
> On entry, the triangular matrix A.  If UPLO = 'U', the
> leading N-by-N upper triangular part of the array A contains
> the upper triangular matrix, and the strictly lower
> triangular part of A is not referenced.  If UPLO = 'L', the
> leading N-by-N lower triangular part of the array A contains
> the lower triangular matrix, and the strictly upper
> triangular part of A is not referenced.

Lda : Integer [in]
> The leading dimension of the matrix A. LDA >= max(1,N).

Arf : Double Precision Array, Dimension (nt). [out]
> NT=N*(N+1)/2. On exit, the triangular matrix A in RFP format.

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value

