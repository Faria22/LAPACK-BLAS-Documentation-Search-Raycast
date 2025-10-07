```fortran
subroutine dsycon_rook	(	uplo,
		n,
		a,
		lda,
		ipiv,
		anorm,
		rcond,
		*                               work,
		iwork,
		info )
```

 DSYCON_ROOK estimates the reciprocal of the condition number (in the
 1-norm) of a real symmetric matrix A using the factorization
 A = U*D*U**T or A = L*D*L**T computed by DSYTRF_ROOK.

 An estimate is obtained for norm(inv(A)), and the reciprocal of the
 condition number is computed as RCOND = 1 / (ANORM * norm(inv(A))).

## Parameters
Uplo : Character*1 [in]
> Specifies whether the details of the factorization are stored
> as an upper or lower triangular matrix.
> = 'U':  Upper triangular, form is A = U*D*U**T;
> = 'L':  Lower triangular, form is A = L*D*L**T.

N : Integer [in]
> The order of the matrix A.  N >= 0.

A : Double Precision Array, Dimension (lda,n) [in]
> The block diagonal matrix D and the multipliers used to
> obtain the factor U or L as computed by DSYTRF_ROOK.

Lda : Integer [in]
> The leading dimension of the array A.  LDA >= max(1,N).

Ipiv : Integer Array, Dimension (n) [in]
> Details of the interchanges and the block structure of D
> as determined by DSYTRF_ROOK.

Anorm : Double Precision [in]
> The 1-norm of the original matrix A.

Rcond : Double Precision [out]
> The reciprocal of the condition number of the matrix A,
> computed as RCOND = 1/(ANORM * AINVNM), where AINVNM is an
> estimate of the 1-norm of inv(A) computed in this routine.

Work : Double Precision Array, Dimension (2*n) [out]

Iwork : Integer Array, Dimension (n) [out]

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value

