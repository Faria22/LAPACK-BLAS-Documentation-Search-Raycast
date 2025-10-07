# SSYR

## Function Signature

```fortran
SSYR(UPLO,N,ALPHA,X,INCX,A,LDA)
```

## Description


 SSYR   performs the symmetric rank 1 operation

    A := alpha*x*x**T + A,

 where alpha is a real scalar, x is an n element vector and A is an
 n by n symmetric matrix.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 On entry, UPLO specifies whether the upper or lower triangular part of the array A is to be referenced as follows: UPLO = 'U' or 'u' Only the upper triangular part of A is to be referenced. UPLO = 'L' or 'l' Only the lower triangular part of A is to be referenced.

### N (in)

N is INTEGER On entry, N specifies the order of the matrix A. N must be at least zero.

### ALPHA (in)

ALPHA is REAL On entry, ALPHA specifies the scalar alpha.

### X (in)

X is REAL array, dimension at least ( 1 + ( n - 1 )*abs( INCX ) ). Before entry, the incremented array X must contain the n element vector x.

### INCX (in)

INCX is INTEGER On entry, INCX specifies the increment for the elements of X. INCX must not be zero.

### A (in,out)

A is REAL array, dimension ( LDA, N ) Before entry with UPLO = 'U' or 'u', the leading n by n upper triangular part of the array A must contain the upper triangular part of the symmetric matrix and the strictly lower triangular part of A is not referenced. On exit, the upper triangular part of the array A is overwritten by the upper triangular part of the updated matrix. Before entry with UPLO = 'L' or 'l', the leading n by n lower triangular part of the array A must contain the lower triangular part of the symmetric matrix and the strictly upper triangular part of A is not referenced. On exit, the lower triangular part of the array A is overwritten by the lower triangular part of the updated matrix.

### LDA (in)

LDA is INTEGER On entry, LDA specifies the first dimension of A as declared in the calling (sub) program. LDA must be at least max( 1, n ).

