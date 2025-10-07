# ZHER

## Function Signature

```fortran
ZHER(UPLO,N,ALPHA,X,INCX,A,LDA)
```

## Description


 ZHER   performs the hermitian rank 1 operation

    A := alpha*x*x**H + A,

 where alpha is a real scalar, x is an n element vector and A is an
 n by n hermitian matrix.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 On entry, UPLO specifies whether the upper or lower triangular part of the array A is to be referenced as follows: UPLO = 'U' or 'u' Only the upper triangular part of A is to be referenced. UPLO = 'L' or 'l' Only the lower triangular part of A is to be referenced.

### N (in)

N is INTEGER On entry, N specifies the order of the matrix A. N must be at least zero.

### ALPHA (in)

ALPHA is DOUBLE PRECISION. On entry, ALPHA specifies the scalar alpha.

### X (in)

X is COMPLEX*16 array, dimension at least ( 1 + ( n - 1 )*abs( INCX ) ). Before entry, the incremented array X must contain the n element vector x.

### INCX (in)

INCX is INTEGER On entry, INCX specifies the increment for the elements of X. INCX must not be zero.

### A (in,out)

A is COMPLEX*16 array, dimension ( LDA, N ) Before entry with UPLO = 'U' or 'u', the leading n by n upper triangular part of the array A must contain the upper triangular part of the hermitian matrix and the strictly lower triangular part of A is not referenced. On exit, the upper triangular part of the array A is overwritten by the upper triangular part of the updated matrix. Before entry with UPLO = 'L' or 'l', the leading n by n lower triangular part of the array A must contain the lower triangular part of the hermitian matrix and the strictly upper triangular part of A is not referenced. On exit, the lower triangular part of the array A is overwritten by the lower triangular part of the updated matrix. Note that the imaginary parts of the diagonal elements need not be set, they are assumed to be zero, and on exit they are set to zero.

### LDA (in)

LDA is INTEGER On entry, LDA specifies the first dimension of A as declared in the calling (sub) program. LDA must be at least max( 1, n ).

