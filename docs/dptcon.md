```fortran
subroutine dptcon	(	integer	n,
		double precision, dimension(*)	d,
		double precision, dimension(*)	e,
		double precision	anorm,
		double precision	rcond,
		double precision, dimension(*)	work,
		integer	info )
```

 DPTCON computes the reciprocal of the condition number (in the
 1-norm) of a real symmetric positive definite tridiagonal matrix
 using the factorization A = L*D*L**T or A = U**T*D*U computed by
 DPTTRF.

 Norm(inv(A)) is computed by a direct method, and the reciprocal of
 the condition number is computed as
              RCOND = 1 / (ANORM * norm(inv(A))).

## Parameters
N : Integer [in]
> The order of the matrix A.  N >= 0.

D : Double Precision Array, Dimension (n) [in]
> The n diagonal elements of the diagonal matrix D from the
> factorization of A, as computed by DPTTRF.

E : Double Precision Array, Dimension (n-1) [in]
> The (n-1) off-diagonal elements of the unit bidiagonal factor
> U or L from the factorization of A,  as computed by DPTTRF.

Anorm : Double Precision [in]
> The 1-norm of the original matrix A.

Rcond : Double Precision [out]
> The reciprocal of the condition number of the matrix A,
> computed as RCOND = 1/(ANORM * AINVNM), where AINVNM is the
> 1-norm of inv(A) computed in this routine.

Work : Double Precision Array, Dimension (n) [out]

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value

