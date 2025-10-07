```fortran
subroutine dgtrfs (
		trans,
		n,
		nrhs,
		dl,
		d,
		du,
		dlf,
		df,
		duf,
		du2,
		*                          ipiv,
		b,
		ldb,
		x,
		ldx,
		ferr,
		berr,
		work,
		iwork,
		*                          info
)
```

 DGTRFS improves the computed solution to a system of linear
 equations when the coefficient matrix is tridiagonal, and provides
 error bounds and backward error estimates for the solution.

## Parameters
Trans : Character*1 [in]
> Specifies the form of the system of equations:
> = 'N':  A * X = B     (No transpose)
> = 'T':  A**T * X = B  (Transpose)
> = 'C':  A**H * X = B  (Conjugate transpose = Transpose)

N : Integer [in]
> The order of the matrix A.  N >= 0.

Nrhs : Integer [in]
> The number of right hand sides, i.e., the number of columns
> of the matrix B.  NRHS >= 0.

Dl : Double Precision Array, Dimension (n-1) [in]
> The (n-1) subdiagonal elements of A.

D : Double Precision Array, Dimension (n) [in]
> The diagonal elements of A.

Du : Double Precision Array, Dimension (n-1) [in]
> The (n-1) superdiagonal elements of A.

Dlf : Double Precision Array, Dimension (n-1) [in]
> The (n-1) multipliers that define the matrix L from the
> LU factorization of A as computed by DGTTRF.

Df : Double Precision Array, Dimension (n) [in]
> The n diagonal elements of the upper triangular matrix U from
> the LU factorization of A.

Duf : Double Precision Array, Dimension (n-1) [in]
> The (n-1) elements of the first superdiagonal of U.

Du2 : Double Precision Array, Dimension (n-2) [in]
> The (n-2) elements of the second superdiagonal of U.

Ipiv : Integer Array, Dimension (n) [in]
> The pivot indices; for 1 <= i <= n, row i of the matrix was
> interchanged with row IPIV(i).  IPIV(i) will always be either
> i or i+1; IPIV(i) = i indicates a row interchange was not
> required.

B : Double Precision Array, Dimension (ldb,nrhs) [in]
> The right hand side matrix B.

Ldb : Integer [in]
> The leading dimension of the array B.  LDB >= max(1,N).

X : Double Precision Array, Dimension (ldx,nrhs) [in,out]
> On entry, the solution matrix X, as computed by DGTTRS.
> On exit, the improved solution matrix X.

Ldx : Integer [in]
> The leading dimension of the array X.  LDX >= max(1,N).

Ferr : Double Precision Array, Dimension (nrhs) [out]
> The estimated forward error bound for each solution vector
> X(j) (the j-th column of the solution matrix X).
> If XTRUE is the true solution corresponding to X(j), FERR(j)
> is an estimated upper bound for the magnitude of the largest
> element in (X(j) - XTRUE) divided by the magnitude of the
> largest element in X(j).  The estimate is as reliable as
> the estimate for RCOND, and is almost always a slight
> overestimate of the true error.

Berr : Double Precision Array, Dimension (nrhs) [out]
> The componentwise relative backward error of each solution
> vector X(j) (i.e., the smallest relative change in
> any element of A or B that makes X(j) an exact solution).

Work : Double Precision Array, Dimension (3*n) [out]

Iwork : Integer Array, Dimension (n) [out]

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value

