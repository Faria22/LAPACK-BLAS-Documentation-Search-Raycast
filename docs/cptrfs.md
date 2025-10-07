```fortran
subroutine cptrfs (
		uplo,
		n,
		nrhs,
		d,
		e,
		df,
		ef,
		b,
		ldb,
		x,
		ldx,
		*                          ferr,
		berr,
		work,
		rwork,
		info
)
```

 CPTRFS improves the computed solution to a system of linear
 equations when the coefficient matrix is Hermitian positive definite
 and tridiagonal, and provides error bounds and backward error
 estimates for the solution.

## Parameters
Uplo : Character*1 [in]
> Specifies whether the superdiagonal or the subdiagonal of the
> tridiagonal matrix A is stored and the form of the
> factorization:
> = 'U':  E is the superdiagonal of A, and A = U**H*D*U;
> = 'L':  E is the subdiagonal of A, and A = L*D*L**H.
> (The two forms are equivalent if A is real.)

N : Integer [in]
> The order of the matrix A.  N >= 0.

Nrhs : Integer [in]
> The number of right hand sides, i.e., the number of columns
> of the matrix B.  NRHS >= 0.

D : Real Array, Dimension (n) [in]
> The n real diagonal elements of the tridiagonal matrix A.

E : Complex Array, Dimension (n-1) [in]
> The (n-1) off-diagonal elements of the tridiagonal matrix A
> (see UPLO).

Df : Real Array, Dimension (n) [in]
> The n diagonal elements of the diagonal matrix D from
> the factorization computed by CPTTRF.

Ef : Complex Array, Dimension (n-1) [in]
> The (n-1) off-diagonal elements of the unit bidiagonal
> factor U or L from the factorization computed by CPTTRF
> (see UPLO).

B : Complex Array, Dimension (ldb,nrhs) [in]
> The right hand side matrix B.

Ldb : Integer [in]
> The leading dimension of the array B.  LDB >= max(1,N).

X : Complex Array, Dimension (ldx,nrhs) [in,out]
> On entry, the solution matrix X, as computed by CPTTRS.
> On exit, the improved solution matrix X.

Ldx : Integer [in]
> The leading dimension of the array X.  LDX >= max(1,N).

Ferr : Real Array, Dimension (nrhs) [out]
> The forward error bound for each solution vector
> X(j) (the j-th column of the solution matrix X).
> If XTRUE is the true solution corresponding to X(j), FERR(j)
> is an estimated upper bound for the magnitude of the largest
> element in (X(j) - XTRUE) divided by the magnitude of the
> largest element in X(j).

Berr : Real Array, Dimension (nrhs) [out]
> The componentwise relative backward error of each solution
> vector X(j) (i.e., the smallest relative change in
> any element of A or B that makes X(j) an exact solution).

Work : Complex Array, Dimension (n) [out]

Rwork : Real Array, Dimension (n) [out]

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value

