# SSPR2

## Function Signature

```fortran
SSPR2(UPLO,N,ALPHA,X,INCX,Y,INCY,AP)
```

## Description


 SSPR2  performs the symmetric rank 2 operation

    A := alpha*x*y**T + alpha*y*x**T + A,

 where alpha is a scalar, x and y are n element vectors and A is an
 n by n symmetric matrix, supplied in packed form.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 On entry, UPLO specifies whether the upper or lower triangular part of the matrix A is supplied in the packed array AP as follows: UPLO = 'U' or 'u' The upper triangular part of A is supplied in AP. UPLO = 'L' or 'l' The lower triangular part of A is supplied in AP.

### N (in)

N is INTEGER On entry, N specifies the order of the matrix A. N must be at least zero.

### ALPHA (in)

ALPHA is REAL On entry, ALPHA specifies the scalar alpha.

### X (in)

X is REAL array, dimension at least ( 1 + ( n - 1 )*abs( INCX ) ). Before entry, the incremented array X must contain the n element vector x.

### INCX (in)

INCX is INTEGER On entry, INCX specifies the increment for the elements of X. INCX must not be zero.

### Y (in)

Y is REAL array, dimension at least ( 1 + ( n - 1 )*abs( INCY ) ). Before entry, the incremented array Y must contain the n element vector y.

### INCY (in)

INCY is INTEGER On entry, INCY specifies the increment for the elements of Y. INCY must not be zero.

### AP (in,out)

AP is REAL array, dimension at least ( ( n*( n + 1 ) )/2 ). Before entry with UPLO = 'U' or 'u', the array AP must contain the upper triangular part of the symmetric matrix packed sequentially, column by column, so that AP( 1 ) contains a( 1, 1 ), AP( 2 ) and AP( 3 ) contain a( 1, 2 ) and a( 2, 2 ) respectively, and so on. On exit, the array AP is overwritten by the upper triangular part of the updated matrix. Before entry with UPLO = 'L' or 'l', the array AP must contain the lower triangular part of the symmetric matrix packed sequentially, column by column, so that AP( 1 ) contains a( 1, 1 ), AP( 2 ) and AP( 3 ) contain a( 2, 1 ) and a( 3, 1 ) respectively, and so on. On exit, the array AP is overwritten by the lower triangular part of the updated matrix.

