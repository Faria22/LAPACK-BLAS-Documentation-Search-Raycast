```fortran
subroutine dlaset (
		character uplo,
		integer m,
		integer n,
		double precision alpha,
		double precision beta,
		double precision, dimension(lda, *) a,
		integer lda
)
```

 DLASET initializes an m-by-n matrix A to BETA on the diagonal and
 ALPHA on the offdiagonals.

## Parameters
Uplo : Character*1 [in]
> Specifies the part of the matrix A to be set.
> = 'U':      Upper triangular part is set; the strictly lower
> triangular part of A is not changed.
> = 'L':      Lower triangular part is set; the strictly upper
> triangular part of A is not changed.
> Otherwise:  All of the matrix A is set.

M : Integer [in]
> The number of rows of the matrix A.  M >= 0.

N : Integer [in]
> The number of columns of the matrix A.  N >= 0.

Alpha : Double Precision [in]
> The constant to which the offdiagonal elements are to be set.

Beta : Double Precision [in]
> The constant to which the diagonal elements are to be set.

A : Double Precision Array, Dimension (lda,n) [out]
> On exit, the leading m-by-n submatrix of A is set as follows:
> if UPLO = 'U', A(i,j) = ALPHA, 1<=i<=j-1, 1<=j<=n,
> if UPLO = 'L', A(i,j) = ALPHA, j+1<=i<=m, 1<=j<=n,
> otherwise,     A(i,j) = ALPHA, 1<=i<=m, 1<=j<=n, i.ne.j,
> and, for all UPLO, A(i,i) = BETA, 1<=i<=min(m,n).

Lda : Integer [in]
> The leading dimension of the array A.  LDA >= max(1,M).

