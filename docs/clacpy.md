```fortran
subroutine clacpy	(	character	uplo,
		integer	m,
		integer	n,
		complex, dimension(lda, *)	a,
		integer	lda,
		complex, dimension(ldb, *)	b,
		integer	ldb )
```

 CLACPY copies all or part of a two-dimensional matrix A to another
 matrix B.

## Parameters
Uplo : Character*1 [in]
> Specifies the part of the matrix A to be copied to B.
> = 'U':      Upper triangular part
> = 'L':      Lower triangular part
> Otherwise:  All of the matrix A

M : Integer [in]
> The number of rows of the matrix A.  M >= 0.

N : Integer [in]
> The number of columns of the matrix A.  N >= 0.

A : Complex Array, Dimension (lda,n) [in]
> The m by n matrix A.  If UPLO = 'U', only the upper trapezium
> is accessed; if UPLO = 'L', only the lower trapezium is
> accessed.

Lda : Integer [in]
> The leading dimension of the array A.  LDA >= max(1,M).

B : Complex Array, Dimension (ldb,n) [out]
> On exit, B = A in the locations specified by UPLO.

Ldb : Integer [in]
> The leading dimension of the array B.  LDB >= max(1,M).

