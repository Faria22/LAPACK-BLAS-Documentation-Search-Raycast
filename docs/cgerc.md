# CGERC

## Function Signature

```fortran
CGERC(M,N,ALPHA,X,INCX,Y,INCY,A,LDA)
```

## Description


 CGERC  performs the rank 1 operation

    A := alpha*x*y**H + A,

 where alpha is a scalar, x is an m element vector, y is an n element
 vector and A is an m by n matrix.

## Parameters

### M (in)

M is INTEGER On entry, M specifies the number of rows of the matrix A. M must be at least zero.

### N (in)

N is INTEGER On entry, N specifies the number of columns of the matrix A. N must be at least zero.

### ALPHA (in)

ALPHA is COMPLEX On entry, ALPHA specifies the scalar alpha.

### X (in)

X is COMPLEX array, dimension at least ( 1 + ( m - 1 )*abs( INCX ) ). Before entry, the incremented array X must contain the m element vector x.

### INCX (in)

INCX is INTEGER On entry, INCX specifies the increment for the elements of X. INCX must not be zero.

### Y (in)

Y is COMPLEX array, dimension at least ( 1 + ( n - 1 )*abs( INCY ) ). Before entry, the incremented array Y must contain the n element vector y.

### INCY (in)

INCY is INTEGER On entry, INCY specifies the increment for the elements of Y. INCY must not be zero.

### A (in,out)

A is COMPLEX array, dimension ( LDA, N ) Before entry, the leading m by n part of the array A must contain the matrix of coefficients. On exit, A is overwritten by the updated matrix.

### LDA (in)

LDA is INTEGER On entry, LDA specifies the first dimension of A as declared in the calling (sub) program. LDA must be at least max( 1, m ).

