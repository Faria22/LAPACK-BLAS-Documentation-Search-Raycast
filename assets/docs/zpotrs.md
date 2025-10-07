```fortran
subroutine zpotrs (
		character uplo,
		integer n,
		integer nrhs,
		complex*16, dimension(lda, *) a,
		integer lda,
		complex*16, dimension(ldb, *) b,
		integer ldb,
		integer info
)
```

 ZPOTRS solves a system of linear equations A*X = B with a Hermitian
 positive definite matrix A using the Cholesky factorization
 A = U**H * U or A = L * L**H computed by ZPOTRF.

## Parameters
Uplo : Character*1 [in]
> = 'U':  Upper triangle of A is stored;
> = 'L':  Lower triangle of A is stored.

N : Integer [in]
> The order of the matrix A.  N >= 0.

Nrhs : Integer [in]
> The number of right hand sides, i.e., the number of columns
> of the matrix B.  NRHS >= 0.

A : Complex*16 Array, Dimension (lda,n) [in]
> The triangular factor U or L from the Cholesky factorization
> A = U**H * U or A = L * L**H, as computed by ZPOTRF.

Lda : Integer [in]
> The leading dimension of the array A.  LDA >= max(1,N).

B : Complex*16 Array, Dimension (ldb,nrhs) [in,out]
> On entry, the right hand side matrix B.
> On exit, the solution matrix X.

Ldb : Integer [in]
> The leading dimension of the array B.  LDB >= max(1,N).

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value

