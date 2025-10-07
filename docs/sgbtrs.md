```fortran
subroutine sgbtrs	(	trans,
		n,
		kl,
		ku,
		nrhs,
		ab,
		ldab,
		ipiv,
		b,
		ldb,
		*                          info )
```

 SGBTRS solves a system of linear equations
    A * X = B  or  A**T * X = B
 with a general band matrix A using the LU factorization computed
 by SGBTRF.

## Parameters
Trans : Character*1 [in]
> Specifies the form of the system of equations.
> = 'N':  A * X = B  (No transpose)
> = 'T':  A**T* X = B  (Transpose)
> = 'C':  A**T* X = B  (Conjugate transpose = Transpose)

N : Integer [in]
> The order of the matrix A.  N >= 0.

Kl : Integer [in]
> The number of subdiagonals within the band of A.  KL >= 0.

Ku : Integer [in]
> The number of superdiagonals within the band of A.  KU >= 0.

Nrhs : Integer [in]
> The number of right hand sides, i.e., the number of columns
> of the matrix B.  NRHS >= 0.

Ab : Real Array, Dimension (ldab,n) [in]
> Details of the LU factorization of the band matrix A, as
> computed by SGBTRF.  U is stored as an upper triangular band
> matrix with KL+KU superdiagonals in rows 1 to KL+KU+1, and
> the multipliers used during the factorization are stored in
> rows KL+KU+2 to 2*KL+KU+1.

Ldab : Integer [in]
> The leading dimension of the array AB.  LDAB >= 2*KL+KU+1.

Ipiv : Integer Array, Dimension (n) [in]
> The pivot indices; for 1 <= i <= N, row i of the matrix was
> interchanged with row IPIV(i).

B : Real Array, Dimension (ldb,nrhs) [in,out]
> On entry, the right hand side matrix B.
> On exit, the solution matrix X.

Ldb : Integer [in]
> The leading dimension of the array B.  LDB >= max(1,N).

Info : Integer [out]
> = 0:  successful exit
> < 0: if INFO = -i, the i-th argument had an illegal value

