```fortran
subroutine ssyconv (
		character uplo,
		character way,
		integer n,
		real, dimension(lda, *) a,
		integer lda,
		integer, dimension(*) ipiv,
		real, dimension(*) e,
		integer info
)
```

 SSYCONV convert A given by TRF into L and D and vice-versa.
 Get Non-diag elements of D (returned in workspace) and
 apply or reverse permutation done in TRF.

## Parameters
Uplo : Character*1 [in]
> Specifies whether the details of the factorization are stored
> as an upper or lower triangular matrix.
> = 'U':  Upper triangular, form is A = U*D*U**T;
> = 'L':  Lower triangular, form is A = L*D*L**T.

Way : Character*1 [in]
> = 'C': Convert
> = 'R': Revert

N : Integer [in]
> The order of the matrix A.  N >= 0.

A : Real Array, Dimension (lda,n) [in,out]
> The block diagonal matrix D and the multipliers used to
> obtain the factor U or L as computed by SSYTRF.

Lda : Integer [in]
> The leading dimension of the array A.  LDA >= max(1,N).

Ipiv : Integer Array, Dimension (n) [in]
> Details of the interchanges and the block structure of D
> as determined by SSYTRF.

E : Real Array, Dimension (n) [out]
> E stores the supdiagonal/subdiagonal of the symmetric 1-by-1
> or 2-by-2 block diagonal matrix D in LDLT.

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value

