```fortran
subroutine spocon	(	uplo,
		n,
		a,
		lda,
		anorm,
		rcond,
		work,
		iwork,
		*                          info )
```

 SPOCON estimates the reciprocal of the condition number (in the
 1-norm) of a real symmetric positive definite matrix using the
 Cholesky factorization A = U**T*U or A = L*L**T computed by SPOTRF.

 An estimate is obtained for norm(inv(A)), and the reciprocal of the
 condition number is computed as RCOND = 1 / (ANORM * norm(inv(A))).

## Parameters
Uplo : Character*1 [in]
> = 'U':  Upper triangle of A is stored;
> = 'L':  Lower triangle of A is stored.

N : Integer [in]
> The order of the matrix A.  N >= 0.

A : Real Array, Dimension (lda,n) [in]
> The triangular factor U or L from the Cholesky factorization
> A = U**T*U or A = L*L**T, as computed by SPOTRF.

Lda : Integer [in]
> The leading dimension of the array A.  LDA >= max(1,N).

Anorm : Real [in]
> The 1-norm (or infinity-norm) of the symmetric matrix A.

Rcond : Real [out]
> The reciprocal of the condition number of the matrix A,
> computed as RCOND = 1/(ANORM * AINVNM), where AINVNM is an
> estimate of the 1-norm of inv(A) computed in this routine.

Work : Real Array, Dimension (3*n) [out]

Iwork : Integer Array, Dimension (n) [out]

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value

