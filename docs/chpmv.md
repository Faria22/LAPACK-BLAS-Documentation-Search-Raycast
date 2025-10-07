```fortran
subroutine chpmv (
		character uplo,
		integer n,
		complex alpha,
		complex, dimension(*) ap,
		complex, dimension(*) x,
		integer incx,
		complex beta,
		complex, dimension(*) y,
		integer incy
)
```

 CHPMV  performs the matrix-vector operation

    y := alpha*A*x + beta*y,

 where alpha and beta are scalars, x and y are n element vectors and
 A is an n by n hermitian matrix, supplied in packed form.

## Parameters
Uplo : Character*1 [in]
> On entry, UPLO specifies whether the upper or lower
> triangular part of the matrix A is supplied in the packed
> array AP as follows:
> UPLO = 'U' or 'u'   The upper triangular part of A is
> supplied in AP.
> UPLO = 'L' or 'l'   The lower triangular part of A is
> supplied in AP.

N : Integer [in]
> On entry, N specifies the order of the matrix A.
> N must be at least zero.

Alpha : Complex [in]
> On entry, ALPHA specifies the scalar alpha.

Ap : Complex Array, Dimension At Least [in]
> ( ( n*( n + 1 ) )/2 ).
> Before entry with UPLO = 'U' or 'u', the array AP must
> contain the upper triangular part of the hermitian matrix
> packed sequentially, column by column, so that AP( 1 )
> contains a( 1, 1 ), AP( 2 ) and AP( 3 ) contain a( 1, 2 )
> and a( 2, 2 ) respectively, and so on.
> Before entry with UPLO = 'L' or 'l', the array AP must
> contain the lower triangular part of the hermitian matrix
> packed sequentially, column by column, so that AP( 1 )
> contains a( 1, 1 ), AP( 2 ) and AP( 3 ) contain a( 2, 1 )
> and a( 3, 1 ) respectively, and so on.
> Note that the imaginary parts of the diagonal elements need
> not be set and are assumed to be zero.

X : Complex Array, Dimension At Least [in]
> ( 1 + ( n - 1 )*abs( INCX ) ).
> Before entry, the incremented array X must contain the n
> element vector x.

Incx : Integer [in]
> On entry, INCX specifies the increment for the elements of
> X. INCX must not be zero.

Beta : Complex [in]
> On entry, BETA specifies the scalar beta. When BETA is
> supplied as zero then Y need not be set on input.

Y : Complex Array, Dimension At Least [in,out]
> ( 1 + ( n - 1 )*abs( INCY ) ).
> Before entry, the incremented array Y must contain the n
> element vector y. On exit, Y is overwritten by the updated
> vector y.

Incy : Integer [in]
> On entry, INCY specifies the increment for the elements of
> Y. INCY must not be zero.

