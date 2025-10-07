```fortran
subroutine spbrfs	(	uplo,
		n,
		kd,
		nrhs,
		ab,
		ldab,
		afb,
		ldafb,
		b,
		*                          ldb,
		x,
		ldx,
		ferr,
		berr,
		work,
		iwork,
		info )
```

 SPBRFS improves the computed solution to a system of linear
 equations when the coefficient matrix is symmetric positive definite
 and banded, and provides error bounds and backward error estimates
 for the solution.

## Parameters
Uplo : Character*1 [in]
> = 'U':  Upper triangle of A is stored;
> = 'L':  Lower triangle of A is stored.

N : Integer [in]
> The order of the matrix A.  N >= 0.

Kd : Integer [in]
> The number of superdiagonals of the matrix A if UPLO = 'U',
> or the number of subdiagonals if UPLO = 'L'.  KD >= 0.

Nrhs : Integer [in]
> The number of right hand sides, i.e., the number of columns
> of the matrices B and X.  NRHS >= 0.

Ab : Real Array, Dimension (ldab,n) [in]
> The upper or lower triangle of the symmetric band matrix A,
> stored in the first KD+1 rows of the array.  The j-th column
> of A is stored in the j-th column of the array AB as follows:
> if UPLO = 'U', AB(kd+1+i-j,j) = A(i,j) for max(1,j-kd)<=i<=j;
> if UPLO = 'L', AB(1+i-j,j)    = A(i,j) for j<=i<=min(n,j+kd).

Ldab : Integer [in]
> The leading dimension of the array AB.  LDAB >= KD+1.

Afb : Real Array, Dimension (ldafb,n) [in]
> The triangular factor U or L from the Cholesky factorization
> A = U**T*U or A = L*L**T of the band matrix A as computed by
> SPBTRF, in the same storage format as A (see AB).

Ldafb : Integer [in]
> The leading dimension of the array AFB.  LDAFB >= KD+1.

B : Real Array, Dimension (ldb,nrhs) [in]
> The right hand side matrix B.

Ldb : Integer [in]
> The leading dimension of the array B.  LDB >= max(1,N).

X : Real Array, Dimension (ldx,nrhs) [in,out]
> On entry, the solution matrix X, as computed by SPBTRS.
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

