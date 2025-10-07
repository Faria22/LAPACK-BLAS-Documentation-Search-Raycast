```fortran
subroutine cla_heamv (
		uplo,
		n,
		alpha,
		a,
		lda,
		x,
		incx,
		beta,
		y,
		*                             incy
)
```

 CLA_SYAMV  performs the matrix-vector operation

         y := alpha*abs(A)*abs(x) + beta*abs(y),

 where alpha and beta are scalars, x and y are vectors and A is an
 n by n symmetric matrix.

 This function is primarily used in calculating error bounds.
 To protect against underflow during evaluation, components in
 the resulting vector are perturbed away from zero by (N+1)
 times the underflow threshold.  To prevent unnecessarily large
 errors for block-structure embedded in general matrices,
 "symbolically" zero components are not perturbed.  A zero
 entry is considered "symbolic" if all multiplications involved
 in computing that entry have at least one zero multiplicand.

## Parameters
Uplo : Integer [in]
> On entry, UPLO specifies whether the upper or lower
> triangular part of the array A is to be referenced as
> follows:
> UPLO = BLAS_UPPER   Only the upper triangular part of A
> is to be referenced.
> UPLO = BLAS_LOWER   Only the lower triangular part of A
> is to be referenced.
> Unchanged on exit.

N : Integer [in]
> On entry, N specifies the number of columns of the matrix A.
> N must be at least zero.
> Unchanged on exit.

Alpha : Real . [in]
> On entry, ALPHA specifies the scalar alpha.
> Unchanged on exit.

A : Complex Array, Dimension ( Lda, N ). [in]
> Before entry, the leading m by n part of the array A must
> contain the matrix of coefficients.
> Unchanged on exit.

Lda : Integer [in]
> On entry, LDA specifies the first dimension of A as declared
> in the calling (sub) program. LDA must be at least
> max( 1, n ).
> Unchanged on exit.

X : Complex Array, Dimension [in]
> ( 1 + ( n - 1 )*abs( INCX ) )
> Before entry, the incremented array X must contain the
> vector x.
> Unchanged on exit.

Incx : Integer [in]
> On entry, INCX specifies the increment for the elements of
> X. INCX must not be zero.
> Unchanged on exit.

Beta : Real . [in]
> On entry, BETA specifies the scalar beta. When BETA is
> supplied as zero then Y need not be set on input.
> Unchanged on exit.

Y : Real Array, Dimension [in,out]
> ( 1 + ( n - 1 )*abs( INCY ) )
> Before entry with BETA non-zero, the incremented array Y
> must contain the vector y. On exit, Y is overwritten by the
> updated vector y.

Incy : Integer [in]
> On entry, INCY specifies the increment for the elements of
> Y. INCY must not be zero.
> Unchanged on exit.

