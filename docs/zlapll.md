```fortran
subroutine zlapll (
		integer n,
		complex*16, dimension(*) x,
		integer incx,
		complex*16, dimension(*) y,
		integer incy,
		double precision ssmin
)
```

 Given two column vectors X and Y, let

                      A = ( X Y ).

 The subroutine first computes the QR factorization of A = Q*R,
 and then computes the SVD of the 2-by-2 upper triangular matrix R.
 The smaller singular value of R is returned in SSMIN, which is used
 as the measurement of the linear dependency of the vectors X and Y.

## Parameters
N : Integer [in]
> The length of the vectors X and Y.

X : Complex*16 Array, Dimension (1+(n-1)*incx) [in,out]
> On entry, X contains the N-vector X.
> On exit, X is overwritten.

Incx : Integer [in]
> The increment between successive elements of X. INCX > 0.

Y : Complex*16 Array, Dimension (1+(n-1)*incy) [in,out]
> On entry, Y contains the N-vector Y.
> On exit, Y is overwritten.

Incy : Integer [in]
> The increment between successive elements of Y. INCY > 0.

Ssmin : Double Precision [out]
> The smallest singular value of the N-by-2 matrix A = ( X Y ).

