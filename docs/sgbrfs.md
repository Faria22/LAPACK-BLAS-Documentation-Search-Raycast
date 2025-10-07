```fortran
subroutine sgbrfs (
		trans,
		n,
		kl,
		ku,
		nrhs,
		ab,
		ldab,
		afb,
		ldafb,
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

 SGBRFS improves the computed solution to a system of linear
 equations when the coefficient matrix is banded, and provides
 error bounds and backward error estimates for the solution.

## Parameters
Trans : Character*1 [in]
> Specifies the form of the system of equations:
> = 'N':  A * X = B     (No transpose)
> = 'T':  A**T * X = B  (Transpose)
> = 'C':  A**H * X = B  (Conjugate transpose = Transpose)

N : Integer [in]
> The order of the matrix A.  N >= 0.

Kl : Integer [in]
> The number of subdiagonals within the band of A.  KL >= 0.

Ku : Integer [in]
> The number of superdiagonals within the band of A.  KU >= 0.

Nrhs : Integer [in]
> The number of right hand sides, i.e., the number of columns
> of the matrices B and X.  NRHS >= 0.

Ab : Real Array, Dimension (ldab,n) [in]
> The original band matrix A, stored in rows 1 to KL+KU+1.
> The j-th column of A is stored in the j-th column of the
> array AB as follows:
> AB(ku+1+i-j,j) = A(i,j) for max(1,j-ku)<=i<=min(n,j+kl).

Ldab : Integer [in]
> The leading dimension of the array AB.  LDAB >= KL+KU+1.

Afb : Real Array, Dimension (ldafb,n) [in]
> Details of the LU factorization of the band matrix A, as
> computed by SGBTRF.  U is stored as an upper triangular band
> matrix with KL+KU superdiagonals in rows 1 to KL+KU+1, and
> the multipliers used during the factorization are stored in
> rows KL+KU+2 to 2*KL+KU+1.

Ldafb : Integer [in]
> The leading dimension of the array AFB.  LDAFB >= 2*KL*KU+1.

Ipiv : Integer Array, Dimension (n) [in]
> The pivot indices from SGBTRF; for 1<=i<=N, row i of the
> matrix was interchanged with row IPIV(i).

B : Real Array, Dimension (ldb,nrhs) [in]
> The right hand side matrix B.

Ldb : Integer [in]
> The leading dimension of the array B.  LDB >= max(1,N).

X : Real Array, Dimension (ldx,nrhs) [in,out]
> On entry, the solution matrix X, as computed by SGBTRS.
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

Work : Real Array, Dimension (3*n) [out]

Iwork : Integer Array, Dimension (n) [out]

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value

