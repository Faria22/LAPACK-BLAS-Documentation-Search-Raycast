```fortran
subroutine sgesc2 (
		integer n,
		real, dimension(lda, *) a,
		integer lda,
		real, dimension(*) rhs,
		integer, dimension(*) ipiv,
		integer, dimension(*) jpiv,
		real scale
)
```

 SGESC2 solves a system of linear equations

           A * X = scale* RHS

 with a general N-by-N matrix A using the LU factorization with
 complete pivoting computed by SGETC2.

## Parameters
N : Integer [in]
> The order of the matrix A.

A : Real Array, Dimension (lda,n) [in]
> On entry, the  LU part of the factorization of the n-by-n
> matrix A computed by SGETC2:  A = P * L * U * Q

Lda : Integer [in]
> The leading dimension of the array A.  LDA >= max(1, N).

Rhs : Real Array, Dimension (n). [in,out]
> On entry, the right hand side vector b.
> On exit, the solution vector X.

Ipiv : Integer Array, Dimension (n). [in]
> The pivot indices; for 1 <= i <= N, row i of the
> matrix has been interchanged with row IPIV(i).

Jpiv : Integer Array, Dimension (n). [in]
> The pivot indices; for 1 <= j <= N, column j of the
> matrix has been interchanged with column JPIV(j).

Scale : Real [out]
> On exit, SCALE contains the scale factor. SCALE is chosen
> 0 <= SCALE <= 1 to prevent overflow in the solution.

