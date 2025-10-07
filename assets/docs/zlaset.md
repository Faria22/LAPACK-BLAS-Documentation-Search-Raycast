```fortran
subroutine zlaset (
		character uplo,
		integer m,
		integer n,
		complex*16 alpha,
		complex*16 beta,
		complex*16, dimension(lda, *) a,
		integer lda
)
```

 ZLASET initializes a 2-D array A to BETA on the diagonal and
 ALPHA on the offdiagonals.

## Parameters
Uplo : Character*1 [in]
> Specifies the part of the matrix A to be set.
> = 'U':      Upper triangular part is set. The lower triangle
> is unchanged.
> = 'L':      Lower triangular part is set. The upper triangle
> is unchanged.
> Otherwise:  All of the matrix A is set.

M : Integer [in]
> On entry, M specifies the number of rows of A.

N : Integer [in]
> On entry, N specifies the number of columns of A.

Alpha : Complex*16 [in]
> All the offdiagonal array elements are set to ALPHA.

Beta : Complex*16 [in]
> All the diagonal array elements are set to BETA.

A : Complex*16 Array, Dimension (lda,n) [out]
> On entry, the m by n matrix A.
> On exit, A(i,j) = ALPHA, 1 <= i <= m, 1 <= j <= n, i.ne.j;
> A(i,i) = BETA , 1 <= i <= min(m,n)

Lda : Integer [in]
> The leading dimension of the array A.  LDA >= max(1,M).

