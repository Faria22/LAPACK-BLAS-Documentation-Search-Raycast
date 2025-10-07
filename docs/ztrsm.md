```fortran
subroutine ztrsm	(	character	side,
		character	uplo,
		character	transa,
		character	diag,
		integer	m,
		integer	n,
		complex*16	alpha,
		complex*16, dimension(lda,*)	a,
		integer	lda,
		complex*16, dimension(ldb,*)	b,
		integer	ldb )
```

 ZTRSM  solves one of the matrix equations

    op( A )*X = alpha*B,   or   X*op( A ) = alpha*B,

 where alpha is a scalar, X and B are m by n matrices, A is a unit, or
 non-unit,  upper or lower triangular matrix  and  op( A )  is one  of

    op( A ) = A   or   op( A ) = A**T   or   op( A ) = A**H.

 The matrix X is overwritten on B.

## Parameters
Side : Character*1 [in]
> On entry, SIDE specifies whether op( A ) appears on the left
> or right of X as follows:
> SIDE = 'L' or 'l'   op( A )*X = alpha*B.
> SIDE = 'R' or 'r'   X*op( A ) = alpha*B.

Uplo : Character*1 [in]
> On entry, UPLO specifies whether the matrix A is an upper or
> lower triangular matrix as follows:
> UPLO = 'U' or 'u'   A is an upper triangular matrix.
> UPLO = 'L' or 'l'   A is a lower triangular matrix.

Transa : Character*1 [in]
> On entry, TRANSA specifies the form of op( A ) to be used in
> the matrix multiplication as follows:
> TRANSA = 'N' or 'n'   op( A ) = A.
> TRANSA = 'T' or 't'   op( A ) = A**T.
> TRANSA = 'C' or 'c'   op( A ) = A**H.

Diag : Character*1 [in]
> On entry, DIAG specifies whether or not A is unit triangular
> as follows:
> DIAG = 'U' or 'u'   A is assumed to be unit triangular.
> DIAG = 'N' or 'n'   A is not assumed to be unit
> triangular.

M : Integer [in]
> On entry, M specifies the number of rows of B. M must be at
> least zero.

N : Integer [in]
> On entry, N specifies the number of columns of B.  N must be
> at least zero.

Alpha : Complex*16 [in]
> On entry,  ALPHA specifies the scalar  alpha. When  alpha is
> zero then  A is not referenced and  B need not be set before
> entry.

A : Complex*16 Array, Dimension ( Lda, K ), [in]
> where k is m when SIDE = 'L' or 'l'
> and k is n when SIDE = 'R' or 'r'.
> Before entry  with  UPLO = 'U' or 'u',  the  leading  k by k
> upper triangular part of the array  A must contain the upper
> triangular matrix  and the strictly lower triangular part of
> A is not referenced.
> Before entry  with  UPLO = 'L' or 'l',  the  leading  k by k
> lower triangular part of the array  A must contain the lower
> triangular matrix  and the strictly upper triangular part of
> A is not referenced.
> Note that when  DIAG = 'U' or 'u',  the diagonal elements of
> A  are not referenced either,  but are assumed to be  unity.

Lda : Integer [in]
> On entry, LDA specifies the first dimension of A as declared
> in the calling (sub) program.  When  SIDE = 'L' or 'l'  then
> LDA  must be at least  max( 1, m ),  when  SIDE = 'R' or 'r'
> then LDA must be at least max( 1, n ).

B : Complex*16 Array, Dimension ( Ldb, N ) [in,out]
> Before entry,  the leading  m by n part of the array  B must
> contain  the  right-hand  side  matrix  B,  and  on exit  is
> overwritten by the solution matrix  X.

Ldb : Integer [in]
> On entry, LDB specifies the first dimension of B as declared
> in  the  calling  (sub)  program.   LDB  must  be  at  least
> max( 1, m ).

