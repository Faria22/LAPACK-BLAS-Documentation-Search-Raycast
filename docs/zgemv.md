# ZGEMV

## Function Signature

```fortran
ZGEMV(TRANS,M,N,ALPHA,A,LDA,X,INCX,BETA,Y,INCY)
```

## Description


 ZGEMV  performs one of the matrix-vector operations

    y := alpha*A*x + beta*y,   or   y := alpha*A**T*x + beta*y,   or

    y := alpha*A**H*x + beta*y,

 where alpha and beta are scalars, x and y are vectors and A is an
 m by n matrix.

## Parameters

### TRANS (in)

TRANS is CHARACTER*1 On entry, TRANS specifies the operation to be performed as follows: TRANS = 'N' or 'n' y := alpha*A*x + beta*y. TRANS = 'T' or 't' y := alpha*A**T*x + beta*y. TRANS = 'C' or 'c' y := alpha*A**H*x + beta*y.

### M (in)

M is INTEGER On entry, M specifies the number of rows of the matrix A. M must be at least zero.

### N (in)

N is INTEGER On entry, N specifies the number of columns of the matrix A. N must be at least zero.

### ALPHA (in)

ALPHA is COMPLEX*16 On entry, ALPHA specifies the scalar alpha.

### A (in)

A is COMPLEX*16 array, dimension ( LDA, N ) Before entry, the leading m by n part of the array A must contain the matrix of coefficients.

### LDA (in)

LDA is INTEGER On entry, LDA specifies the first dimension of A as declared in the calling (sub) program. LDA must be at least max( 1, m ).

### X (in)

X is COMPLEX*16 array, dimension at least ( 1 + ( n - 1 )*abs( INCX ) ) when TRANS = 'N' or 'n' and at least ( 1 + ( m - 1 )*abs( INCX ) ) otherwise. Before entry, the incremented array X must contain the vector x.

### INCX (in)

INCX is INTEGER On entry, INCX specifies the increment for the elements of X. INCX must not be zero.

### BETA (in)

BETA is COMPLEX*16 On entry, BETA specifies the scalar beta. When BETA is supplied as zero then Y need not be set on input.

### Y (in,out)

Y is COMPLEX*16 array, dimension at least ( 1 + ( m - 1 )*abs( INCY ) ) when TRANS = 'N' or 'n' and at least ( 1 + ( n - 1 )*abs( INCY ) ) otherwise. Before entry with BETA non-zero, the incremented array Y must contain the vector y. On exit, Y is overwritten by the updated vector y. If either m or n is zero, then Y not referenced and the function performs a quick return.

### INCY (in)

INCY is INTEGER On entry, INCY specifies the increment for the elements of Y. INCY must not be zero.

