```fortran
subroutine sspcon (
		uplo,
		n,
		ap,
		ipiv,
		anorm,
		rcond,
		work,
		iwork,
		*                          info
)
```

 SSPCON estimates the reciprocal of the condition number (in the
 1-norm) of a real symmetric packed matrix A using the factorization
 A = U*D*U**T or A = L*D*L**T computed by SSPTRF.

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

Ap : Real Array, Dimension (n*(n+1)/2) [in]
> The block diagonal matrix D and the multipliers used to
> obtain the factor U or L as computed by SSPTRF, stored as a
> packed triangular matrix.

Ipiv : Integer Array, Dimension (n) [in]
> Details of the interchanges and the block structure of D
> as determined by SSPTRF.

Anorm : Real [in]
> The 1-norm of the original matrix A.

Rcond : Real [out]
> The reciprocal of the condition number of the matrix A,
> computed as RCOND = 1/(ANORM * AINVNM), where AINVNM is an
> estimate of the 1-norm of inv(A) computed in this routine.

Work : Real Array, Dimension (2*n) [out]

Iwork : Integer Array, Dimension (n) [out]

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value

