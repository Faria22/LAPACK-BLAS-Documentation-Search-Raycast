# CSPMV

## Function Signature

```fortran
CSPMV(UPLO, N, ALPHA, AP, X, INCX, BETA, Y, INCY)
```

## Description


 CSPMV  performs the matrix-vector operation

    y := alpha*A*x + beta*y,

 where alpha and beta are scalars, x and y are n element vectors and
 A is an n by n symmetric matrix, supplied in packed form.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 On entry, UPLO specifies whether the upper or lower triangular part of the matrix A is supplied in the packed array AP as follows: UPLO = 'U' or 'u' The upper triangular part of A is supplied in AP. UPLO = 'L' or 'l' The lower triangular part of A is supplied in AP. Unchanged on exit.

### N (in)

N is INTEGER On entry, N specifies the order of the matrix A. N must be at least zero. Unchanged on exit.

### ALPHA (in)

ALPHA is COMPLEX On entry, ALPHA specifies the scalar alpha. Unchanged on exit.

### AP (in)

AP is COMPLEX array, dimension at least ( ( N*( N + 1 ) )/2 ). Before entry, with UPLO = 'U' or 'u', the array AP must contain the upper triangular part of the symmetric matrix packed sequentially, column by column, so that AP( 1 ) contains a( 1, 1 ), AP( 2 ) and AP( 3 ) contain a( 1, 2 ) and a( 2, 2 ) respectively, and so on. Before entry, with UPLO = 'L' or 'l', the array AP must contain the lower triangular part of the symmetric matrix packed sequentially, column by column, so that AP( 1 ) contains a( 1, 1 ), AP( 2 ) and AP( 3 ) contain a( 2, 1 ) and a( 3, 1 ) respectively, and so on. Unchanged on exit.

### X (in)

X is COMPLEX array, dimension at least ( 1 + ( N - 1 )*abs( INCX ) ). Before entry, the incremented array X must contain the N- element vector x. Unchanged on exit.

### INCX (in)

INCX is INTEGER On entry, INCX specifies the increment for the elements of X. INCX must not be zero. Unchanged on exit.

### BETA (in)

BETA is COMPLEX On entry, BETA specifies the scalar beta. When BETA is supplied as zero then Y need not be set on input. Unchanged on exit.

### Y (in,out)

Y is COMPLEX array, dimension at least ( 1 + ( N - 1 )*abs( INCY ) ). Before entry, the incremented array Y must contain the n element vector y. On exit, Y is overwritten by the updated vector y.

### INCY (in)

INCY is INTEGER On entry, INCY specifies the increment for the elements of Y. INCY must not be zero. Unchanged on exit.

