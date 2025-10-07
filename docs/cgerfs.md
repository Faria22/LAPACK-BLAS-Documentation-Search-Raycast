```fortran
subroutine cgerfs (
		trans,
		n,
		nrhs,
		a,
		lda,
		af,
		ldaf,
		ipiv,
		b,
		ldb,
		*                          x,
		ldx,
		ferr,
		berr,
		work,
		rwork,
		info
)
```

 CGERFS improves the computed solution to a system of linear
 equations and provides error bounds and backward error estimates for
 the solution.

## Parameters
Trans : Character*1 [in]
> Specifies the form of the system of equations:
> = 'N':  A * X = B     (No transpose)
> = 'T':  A**T * X = B  (Transpose)
> = 'C':  A**H * X = B  (Conjugate transpose)

N : Integer [in]
> The order of the matrix A.  N >= 0.

Nrhs : Integer [in]
> The number of right hand sides, i.e., the number of columns
> of the matrices B and X.  NRHS >= 0.

A : Complex Array, Dimension (lda,n) [in]
> The original N-by-N matrix A.

Lda : Integer [in]
> The leading dimension of the array A.  LDA >= max(1,N).

Af : Complex Array, Dimension (ldaf,n) [in]
> The factors L and U from the factorization A = P*L*U
> as computed by CGETRF.

Ldaf : Integer [in]
> The leading dimension of the array AF.  LDAF >= max(1,N).

Ipiv : Integer Array, Dimension (n) [in]
> The pivot indices from CGETRF; for 1<=i<=N, row i of the
> matrix was interchanged with row IPIV(i).

B : Complex Array, Dimension (ldb,nrhs) [in]
> The right hand side matrix B.

Ldb : Integer [in]
> The leading dimension of the array B.  LDB >= max(1,N).

X : Complex Array, Dimension (ldx,nrhs) [in,out]
> On entry, the solution matrix X, as computed by CGETRS.
> On exit, the improved solution matrix X.

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

Work : Complex Array, Dimension (2*n) [out]

Rwork : Real Array, Dimension (n) [out]

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value

