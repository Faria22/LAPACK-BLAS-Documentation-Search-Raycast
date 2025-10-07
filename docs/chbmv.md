```fortran
subroutine chbmv (
		character uplo,
		integer n,
		integer k,
		complex alpha,
		complex, dimension(lda,*) a,
		integer lda,
		complex, dimension(*) x,
		integer incx,
		complex beta,
		complex, dimension(*) y,
		integer incy
)
```

 CHBMV  performs the matrix-vector  operation

    y := alpha*A*x + beta*y,

 where alpha and beta are scalars, x and y are n element vectors and
 A is an n by n hermitian band matrix, with k super-diagonals.

## Parameters
Uplo : Character*1 [in]
> On entry, UPLO specifies whether the upper or lower
> triangular part of the band matrix A is being supplied as
> follows:
> UPLO = 'U' or 'u'   The upper triangular part of A is
> being supplied.
> UPLO = 'L' or 'l'   The lower triangular part of A is
> being supplied.

N : Integer [in]
> On entry, N specifies the order of the matrix A.
> N must be at least zero.

K : Integer [in]
> On entry, K specifies the number of super-diagonals of the
> matrix A. K must satisfy  0 .le. K.

Alpha : Complex [in]
> On entry, ALPHA specifies the scalar alpha.

A : Complex Array, Dimension ( Lda, N ) [in]
> Before entry with UPLO = 'U' or 'u', the leading ( k + 1 )
> by n part of the array A must contain the upper triangular
> band part of the hermitian matrix, supplied column by
> column, with the leading diagonal of the matrix in row
> ( k + 1 ) of the array, the first super-diagonal starting at
> position 2 in row k, and so on. The top left k by k triangle
> of the array A is not referenced.
> The following program segment will transfer the upper
> triangular part of a hermitian band matrix from conventional
> full matrix storage to band storage:
> DO 20, J = 1, N
> M = K + 1 - J
> DO 10, I = MAX( 1, J - K ), J
> A( M + I, J ) = matrix( I, J )
> 10    CONTINUE
> 20 CONTINUE
> Before entry with UPLO = 'L' or 'l', the leading ( k + 1 )
> by n part of the array A must contain the lower triangular
> band part of the hermitian matrix, supplied column by
> column, with the leading diagonal of the matrix in row 1 of
> the array, the first sub-diagonal starting at position 1 in
> row 2, and so on. The bottom right k by k triangle of the
> array A is not referenced.
> The following program segment will transfer the lower
> triangular part of a hermitian band matrix from conventional
> full matrix storage to band storage:
> DO 20, J = 1, N
> M = 1 - J
> DO 10, I = J, MIN( N, J + K )
> A( M + I, J ) = matrix( I, J )
> 10    CONTINUE
> 20 CONTINUE
> Note that the imaginary parts of the diagonal elements need
> not be set and are assumed to be zero.

Lda : Integer [in]
> On entry, LDA specifies the first dimension of A as declared
> in the calling (sub) program. LDA must be at least
> ( k + 1 ).

X : Complex Array, Dimension At Least [in]
> ( 1 + ( n - 1 )*abs( INCX ) ).
> Before entry, the incremented array X must contain the
> vector x.

Incx : Integer [in]
> On entry, INCX specifies the increment for the elements of
> X. INCX must not be zero.

Beta : Complex [in]
> On entry, BETA specifies the scalar beta.

Y : Complex Array, Dimension At Least [in,out]
> ( 1 + ( n - 1 )*abs( INCY ) ).
> Before entry, the incremented array Y must contain the
> vector y. On exit, Y is overwritten by the updated vector y.

Incy : Integer [in]
> On entry, INCY specifies the increment for the elements of
> Y. INCY must not be zero.

