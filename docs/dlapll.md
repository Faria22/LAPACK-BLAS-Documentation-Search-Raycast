# DLAPLL

## Function Signature

```fortran
DLAPLL(N, X, INCX, Y, INCY, SSMIN)
```

## Description


 Given two column vectors X and Y, let

                      A = ( X Y ).

 The subroutine first computes the QR factorization of A = Q*R,
 and then computes the SVD of the 2-by-2 upper triangular matrix R.
 The smaller singular value of R is returned in SSMIN, which is used
 as the measurement of the linear dependency of the vectors X and Y.

## Parameters

### N (in)

N is INTEGER The length of the vectors X and Y.

### X (in,out)

X is DOUBLE PRECISION array, dimension (1+(N-1)*INCX) On entry, X contains the N-vector X. On exit, X is overwritten.

### INCX (in)

INCX is INTEGER The increment between successive elements of X. INCX > 0.

### Y (in,out)

Y is DOUBLE PRECISION array, dimension (1+(N-1)*INCY) On entry, Y contains the N-vector Y. On exit, Y is overwritten.

### INCY (in)

INCY is INTEGER The increment between successive elements of Y. INCY > 0.

### SSMIN (out)

SSMIN is DOUBLE PRECISION The smallest singular value of the N-by-2 matrix A = ( X Y ).

