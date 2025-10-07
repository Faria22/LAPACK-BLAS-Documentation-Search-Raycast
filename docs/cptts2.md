```fortran
subroutine cptts2 (
		integer iuplo,
		integer n,
		integer nrhs,
		real, dimension(*) d,
		complex, dimension(*) e,
		complex, dimension(ldb, *) b,
		integer ldb
)
```

 CPTTS2 solves a tridiagonal system of the form
    A * X = B
 using the factorization A = U**H*D*U or A = L*D*L**H computed by CPTTRF.
 D is a diagonal matrix specified in the vector D, U (or L) is a unit
 bidiagonal matrix whose superdiagonal (subdiagonal) is specified in
 the vector E, and X and B are N by NRHS matrices.

## Parameters
Iuplo : Integer [in]
> Specifies the form of the factorization and whether the
> vector E is the superdiagonal of the upper bidiagonal factor
> U or the subdiagonal of the lower bidiagonal factor L.
> = 1:  A = U**H *D*U, E is the superdiagonal of U
> = 0:  A = L*D*L**H, E is the subdiagonal of L

N : Integer [in]
> The order of the tridiagonal matrix A.  N >= 0.

Nrhs : Integer [in]
> The number of right hand sides, i.e., the number of columns
> of the matrix B.  NRHS >= 0.

D : Real Array, Dimension (n) [in]
> The n diagonal elements of the diagonal matrix D from the
> factorization A = U**H *D*U or A = L*D*L**H.

E : Complex Array, Dimension (n-1) [in]
> If IUPLO = 1, the (n-1) superdiagonal elements of the unit
> bidiagonal factor U from the factorization A = U**H*D*U.
> If IUPLO = 0, the (n-1) subdiagonal elements of the unit
> bidiagonal factor L from the factorization A = L*D*L**H.

B : Complex Array, Dimension (ldb,nrhs) [in,out]
> On entry, the right hand side vectors B for the system of
> linear equations.
> On exit, the solution vectors, X.

Ldb : Integer [in]
> The leading dimension of the array B.  LDB >= max(1,N).

