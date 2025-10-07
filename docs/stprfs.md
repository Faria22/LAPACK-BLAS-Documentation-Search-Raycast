```fortran
subroutine stprfs	(	uplo,
		trans,
		diag,
		n,
		nrhs,
		ap,
		b,
		ldb,
		x,
		ldx,
		*                          ferr,
		berr,
		work,
		iwork,
		info )
```

 STPRFS provides error bounds and backward error estimates for the
 solution to a system of linear equations with a triangular packed
 coefficient matrix.

 The solution matrix X must be computed by STPTRS or some other
 means before entering this routine.  STPRFS does not do iterative
 refinement because doing so cannot improve the backward error.

## Parameters
Uplo : Character*1 [in]
> = 'U':  A is upper triangular;
> = 'L':  A is lower triangular.

Trans : Character*1 [in]
> Specifies the form of the system of equations:
> = 'N':  A * X = B  (No transpose)
> = 'T':  A**T * X = B  (Transpose)
> = 'C':  A**H * X = B  (Conjugate transpose = Transpose)

Diag : Character*1 [in]
> = 'N':  A is non-unit triangular;
> = 'U':  A is unit triangular.

N : Integer [in]
> The order of the matrix A.  N >= 0.

Nrhs : Integer [in]
> The number of right hand sides, i.e., the number of columns
> of the matrices B and X.  NRHS >= 0.

Ap : Real Array, Dimension (n*(n+1)/2) [in]
> The upper or lower triangular matrix A, packed columnwise in
> a linear array.  The j-th column of A is stored in the array
> AP as follows:
> if UPLO = 'U', AP(i + (j-1)*j/2) = A(i,j) for 1<=i<=j;
> if UPLO = 'L', AP(i + (j-1)*(2*n-j)/2) = A(i,j) for j<=i<=n.
> If DIAG = 'U', the diagonal elements of A are not referenced
> and are assumed to be 1.

B : Real Array, Dimension (ldb,nrhs) [in]
> The right hand side matrix B.

Ldb : Integer [in]
> The leading dimension of the array B.  LDB >= max(1,N).

X : Real Array, Dimension (ldx,nrhs) [in]
> The solution matrix X.

Ldx : Integer [in]
> The leading dimension of the array X.  LDX >= max(1,N).

Ferr : Real Array, Dimension (nrhs) [out]
> The estimated forward error bound for each solution vector
> X(j) (the j-th column of the solution matrix X).
> If XTRUE is the true solution corresponding to X(j), FERR(j)
> is an estimated upper bound for the magnitude of the largest
> element in (X(j) - XTRUE) divided by the magnitude of the
> largest element in X(j).  The estimate is as reliable as
> the estimate for RCOND, and is almost always a slight
> overestimate of the true error.

Berr : Real Array, Dimension (nrhs) [out]
> The componentwise relative backward error of each solution
> vector X(j) (i.e., the smallest relative change in
> any element of A or B that makes X(j) an exact solution).

Work : Real Array, Dimension (3*n) [out]

Iwork : Integer Array, Dimension (n) [out]

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value

