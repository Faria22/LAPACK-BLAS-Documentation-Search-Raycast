```fortran
subroutine zgetrs (
		character trans,
		integer n,
		integer nrhs,
		complex*16, dimension(lda, *) a,
		integer lda,
		integer, dimension(*) ipiv,
		complex*16, dimension(ldb, *) b,
		integer ldb,
		integer info
)
```

 ZGETRS solves a system of linear equations
    A * X = B,  A**T * X = B,  or  A**H * X = B
 with a general N-by-N matrix A using the LU factorization computed
 by ZGETRF.

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
> of the matrix B.  NRHS >= 0.

A : Complex*16 Array, Dimension (lda,n) [in]
> The factors L and U from the factorization A = P*L*U
> as computed by ZGETRF.

Lda : Integer [in]
> The leading dimension of the array A.  LDA >= max(1,N).

Ipiv : Integer Array, Dimension (n) [in]
> The pivot indices from ZGETRF; for 1<=i<=N, row i of the
> matrix was interchanged with row IPIV(i).

B : Complex*16 Array, Dimension (ldb,nrhs) [in,out]
> On entry, the right hand side matrix B.
> On exit, the solution matrix X.

Ldb : Integer [in]
> The leading dimension of the array B.  LDB >= max(1,N).

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value

