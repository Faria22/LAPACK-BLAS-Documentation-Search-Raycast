```fortran
subroutine chpcon	(	character	uplo,
		integer	n,
		complex, dimension(*)	ap,
		integer, dimension(*)	ipiv,
		real	anorm,
		real	rcond,
		complex, dimension(*)	work,
		integer	info )
```

 CHPCON estimates the reciprocal of the condition number of a complex
 Hermitian packed matrix A using the factorization A = U*D*U**H or
 A = L*D*L**H computed by CHPTRF.

 An estimate is obtained for norm(inv(A)), and the reciprocal of the
 condition number is computed as RCOND = 1 / (ANORM * norm(inv(A))).

## Parameters
Uplo : Character*1 [in]
> Specifies whether the details of the factorization are stored
> as an upper or lower triangular matrix.
> = 'U':  Upper triangular, form is A = U*D*U**H;
> = 'L':  Lower triangular, form is A = L*D*L**H.

N : Integer [in]
> The order of the matrix A.  N >= 0.

Ap : Complex Array, Dimension (n*(n+1)/2) [in]
> The block diagonal matrix D and the multipliers used to
> obtain the factor U or L as computed by CHPTRF, stored as a
> packed triangular matrix.

Ipiv : Integer Array, Dimension (n) [in]
> Details of the interchanges and the block structure of D
> as determined by CHPTRF.

Anorm : Real [in]
> The 1-norm of the original matrix A.

Rcond : Real [out]
> The reciprocal of the condition number of the matrix A,
> computed as RCOND = 1/(ANORM * AINVNM), where AINVNM is an
> estimate of the 1-norm of inv(A) computed in this routine.

Work : Complex Array, Dimension (2*n) [out]

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value

