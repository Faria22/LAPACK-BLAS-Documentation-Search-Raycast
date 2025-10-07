```fortran
subroutine ctrttf (
		character transr,
		character uplo,
		integer n,
		complex, dimension(0: lda-1, 0: *) a,
		integer lda,
		complex, dimension(0: *) arf,
		integer info
)
```

 CTRTTF copies a triangular matrix A from standard full format (TR)
 to rectangular full packed format (TF) .

## Parameters
Transr : Character*1 [in]
> = 'N':  ARF in Normal mode is wanted;
> = 'C':  ARF in Conjugate Transpose mode is wanted;

Uplo : Character*1 [in]
> = 'U':  A is upper triangular;
> = 'L':  A is lower triangular.

N : Integer [in]
> The order of the matrix A.  N >= 0.

A : Complex Array, Dimension ( Lda, N ) [in]
> On entry, the triangular matrix A.  If UPLO = 'U', the
> leading N-by-N upper triangular part of the array A contains
> the upper triangular matrix, and the strictly lower
> triangular part of A is not referenced.  If UPLO = 'L', the
> leading N-by-N lower triangular part of the array A contains
> the lower triangular matrix, and the strictly upper
> triangular part of A is not referenced.

Lda : Integer [in]
> The leading dimension of the matrix A.  LDA >= max(1,N).

Arf : Complex Array, Dimension ( N*(n+1)/2 ), [out]
> On exit, the upper or lower triangular matrix A stored in
> RFP format. For a further discussion see Notes below.

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value

