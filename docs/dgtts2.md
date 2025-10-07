```fortran
subroutine dgtts2	(	integer	itrans,
		integer	n,
		integer	nrhs,
		double precision, dimension(*)	dl,
		double precision, dimension(*)	d,
		double precision, dimension(*)	du,
		double precision, dimension(*)	du2,
		integer, dimension(*)	ipiv,
		double precision, dimension(ldb, *)	b,
		integer	ldb )
```

 DGTTS2 solves one of the systems of equations
    A*X = B  or  A**T*X = B,
 with a tridiagonal matrix A using the LU factorization computed
 by DGTTRF.

## Parameters
Itrans : Integer [in]
> Specifies the form of the system of equations.
> = 0:  A * X = B  (No transpose)
> = 1:  A**T* X = B  (Transpose)
> = 2:  A**T* X = B  (Conjugate transpose = Transpose)

N : Integer [in]
> The order of the matrix A.

Nrhs : Integer [in]
> The number of right hand sides, i.e., the number of columns
> of the matrix B.  NRHS >= 0.

Dl : Double Precision Array, Dimension (n-1) [in]
> The (n-1) multipliers that define the matrix L from the
> LU factorization of A.

D : Double Precision Array, Dimension (n) [in]
> The n diagonal elements of the upper triangular matrix U from
> the LU factorization of A.

Du : Double Precision Array, Dimension (n-1) [in]
> The (n-1) elements of the first super-diagonal of U.

Du2 : Double Precision Array, Dimension (n-2) [in]
> The (n-2) elements of the second super-diagonal of U.

Ipiv : Integer Array, Dimension (n) [in]
> The pivot indices; for 1 <= i <= n, row i of the matrix was
> interchanged with row IPIV(i).  IPIV(i) will always be either
> i or i+1; IPIV(i) = i indicates a row interchange was not
> required.

B : Double Precision Array, Dimension (ldb,nrhs) [in,out]
> On entry, the matrix of right hand side vectors B.
> On exit, B is overwritten by the solution vectors X.

Ldb : Integer [in]
> The leading dimension of the array B.  LDB >= max(1,N).

