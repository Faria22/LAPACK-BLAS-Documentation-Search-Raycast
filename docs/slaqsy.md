```fortran
subroutine slaqsy	(	character	uplo,
		integer	n,
		real, dimension(lda, *)	a,
		integer	lda,
		real, dimension(*)	s,
		real	scond,
		real	amax,
		character	equed )
```

 SLAQSY equilibrates a symmetric matrix A using the scaling factors
 in the vector S.

## Parameters
Uplo : Character*1 [in]
> Specifies whether the upper or lower triangular part of the
> symmetric matrix A is stored.
> = 'U':  Upper triangular
> = 'L':  Lower triangular

N : Integer [in]
> The order of the matrix A.  N >= 0.

A : Real Array, Dimension (lda,n) [in,out]
> On entry, the symmetric matrix A.  If UPLO = 'U', the leading
> n by n upper triangular part of A contains the upper
> triangular part of the matrix A, and the strictly lower
> triangular part of A is not referenced.  If UPLO = 'L', the
> leading n by n lower triangular part of A contains the lower
> triangular part of the matrix A, and the strictly upper
> triangular part of A is not referenced.
> On exit, if EQUED = 'Y', the equilibrated matrix:
> diag(S) * A * diag(S).

Lda : Integer [in]
> The leading dimension of the array A.  LDA >= max(N,1).

S : Real Array, Dimension (n) [in]
> The scale factors for A.

Scond : Real [in]
> Ratio of the smallest S(i) to the largest S(i).

Amax : Real [in]
> Absolute value of largest matrix entry.

Equed : Character*1 [out]
> Specifies whether or not equilibration was done.
> = 'N':  No equilibration.
> = 'Y':  Equilibration was done, i.e., A has been replaced by
> diag(S) * A * diag(S).

