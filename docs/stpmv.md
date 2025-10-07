```fortran
subroutine stpmv	(	character	uplo,
		character	trans,
		character	diag,
		integer	n,
		real, dimension(*)	ap,
		real, dimension(*)	x,
		integer	incx )
```

 STPMV  performs one of the matrix-vector operations

    x := A*x,   or   x := A**T*x,

 where x is an n element vector and  A is an n by n unit, or non-unit,
 upper or lower triangular matrix, supplied in packed form.

## Parameters
Uplo : Character*1 [in]
> On entry, UPLO specifies whether the matrix is an upper or
> lower triangular matrix as follows:
> UPLO = 'U' or 'u'   A is an upper triangular matrix.
> UPLO = 'L' or 'l'   A is a lower triangular matrix.

Trans : Character*1 [in]
> On entry, TRANS specifies the operation to be performed as
> follows:
> TRANS = 'N' or 'n'   x := A*x.
> TRANS = 'T' or 't'   x := A**T*x.
> TRANS = 'C' or 'c'   x := A**T*x.

Diag : Character*1 [in]
> On entry, DIAG specifies whether or not A is unit
> triangular as follows:
> DIAG = 'U' or 'u'   A is assumed to be unit triangular.
> DIAG = 'N' or 'n'   A is not assumed to be unit
> triangular.

N : Integer [in]
> On entry, N specifies the order of the matrix A.
> N must be at least zero.

Ap : Real Array, Dimension At Least [in]
> ( ( n*( n + 1 ) )/2 ).
> Before entry with  UPLO = 'U' or 'u', the array AP must
> contain the upper triangular matrix packed sequentially,
> column by column, so that AP( 1 ) contains a( 1, 1 ),
> AP( 2 ) and AP( 3 ) contain a( 1, 2 ) and a( 2, 2 )
> respectively, and so on.
> Before entry with UPLO = 'L' or 'l', the array AP must
> contain the lower triangular matrix packed sequentially,
> column by column, so that AP( 1 ) contains a( 1, 1 ),
> AP( 2 ) and AP( 3 ) contain a( 2, 1 ) and a( 3, 1 )
> respectively, and so on.
> Note that when  DIAG = 'U' or 'u', the diagonal elements of
> A are not referenced, but are assumed to be unity.

X : Real Array, Dimension At Least [in,out]
> ( 1 + ( n - 1 )*abs( INCX ) ).
> Before entry, the incremented array X must contain the n
> element vector x. On exit, X is overwritten with the
> transformed vector x.

Incx : Integer [in]
> On entry, INCX specifies the increment for the elements of
> X. INCX must not be zero.

