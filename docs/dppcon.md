```fortran
subroutine dppcon (
		character uplo,
		integer n,
		double precision, dimension(*) ap,
		double precision anorm,
		double precision rcond,
		double precision, dimension(*) work,
		integer, dimension(*) iwork,
		integer info
)
```

 DPPCON estimates the reciprocal of the condition number (in the
 1-norm) of a real symmetric positive definite packed matrix using
 the Cholesky factorization A = U**T*U or A = L*L**T computed by
 DPPTRF.

 An estimate is obtained for norm(inv(A)), and the reciprocal of the
 condition number is computed as RCOND = 1 / (ANORM * norm(inv(A))).

## Parameters
Uplo : Character*1 [in]
> = 'U':  Upper triangle of A is stored;
> = 'L':  Lower triangle of A is stored.

N : Integer [in]
> The order of the matrix A.  N >= 0.

Ap : Double Precision Array, Dimension (n*(n+1)/2) [in]
> The triangular factor U or L from the Cholesky factorization
> A = U**T*U or A = L*L**T, packed columnwise in a linear
> array.  The j-th column of U or L is stored in the array AP
> as follows:
> if UPLO = 'U', AP(i + (j-1)*j/2) = U(i,j) for 1<=i<=j;
> if UPLO = 'L', AP(i + (j-1)*(2n-j)/2) = L(i,j) for j<=i<=n.

Anorm : Double Precision [in]
> The 1-norm (or infinity-norm) of the symmetric matrix A.

Rcond : Double Precision [out]
> The reciprocal of the condition number of the matrix A,
> computed as RCOND = 1/(ANORM * AINVNM), where AINVNM is an
> estimate of the 1-norm of inv(A) computed in this routine.

Work : Double Precision Array, Dimension (3*n) [out]

Iwork : Integer Array, Dimension (n) [out]

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value

