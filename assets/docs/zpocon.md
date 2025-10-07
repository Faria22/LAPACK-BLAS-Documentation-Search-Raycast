```fortran
subroutine zpocon (
		uplo,
		n,
		a,
		lda,
		anorm,
		rcond,
		work,
		rwork,
		*                          info
)
```

 ZPOCON estimates the reciprocal of the condition number (in the
 1-norm) of a complex Hermitian positive definite matrix using the
 Cholesky factorization A = U**H*U or A = L*L**H computed by ZPOTRF.

 An estimate is obtained for norm(inv(A)), and the reciprocal of the
 condition number is computed as RCOND = 1 / (ANORM * norm(inv(A))).

## Parameters
Uplo : Character*1 [in]
> = 'U':  Upper triangle of A is stored;
> = 'L':  Lower triangle of A is stored.

N : Integer [in]
> The order of the matrix A.  N >= 0.

A : Complex*16 Array, Dimension (lda,n) [in]
> The triangular factor U or L from the Cholesky factorization
> A = U**H*U or A = L*L**H, as computed by ZPOTRF.

Lda : Integer [in]
> The leading dimension of the array A.  LDA >= max(1,N).

Anorm : Double Precision [in]
> The 1-norm (or infinity-norm) of the Hermitian matrix A.

Rcond : Double Precision [out]
> The reciprocal of the condition number of the matrix A,
> computed as RCOND = 1/(ANORM * AINVNM), where AINVNM is an
> estimate of the 1-norm of inv(A) computed in this routine.

Work : Complex*16 Array, Dimension (2*n) [out]

Rwork : Double Precision Array, Dimension (n) [out]

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value

