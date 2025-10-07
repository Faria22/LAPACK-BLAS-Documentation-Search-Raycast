```fortran
subroutine zlarfy	(	character	uplo,
		integer	n,
		complex*16, dimension(*)	v,
		integer	incv,
		complex*16	tau,
		complex*16, dimension(ldc, *)	c,
		integer	ldc,
		complex*16, dimension(*)	work )
```

 ZLARFY applies an elementary reflector, or Householder matrix, H,
 to an n x n Hermitian matrix C, from both the left and the right.

 H is represented in the form

    H = I - tau * v * v'

 where  tau  is a scalar and  v  is a vector.

 If  tau  is  zero, then  H  is taken to be the unit matrix.

## Parameters
Uplo : Character*1 [in]
> Specifies whether the upper or lower triangular part of the
> Hermitian matrix C is stored.
> = 'U':  Upper triangle
> = 'L':  Lower triangle

N : Integer [in]
> The number of rows and columns of the matrix C.  N >= 0.

V : Complex*16 Array, Dimension [in]
> (1 + (N-1)*abs(INCV))
> The vector v as described above.

Incv : Integer [in]
> The increment between successive elements of v.  INCV must
> not be zero.

Tau : Complex*16 [in]
> The value tau as described above.

C : Complex*16 Array, Dimension (ldc, N) [in,out]
> On entry, the matrix C.
> On exit, C is overwritten by H * C * H'.

Ldc : Integer [in]
> The leading dimension of the array C.  LDC >= max( 1, N ).

Work : Complex*16 Array, Dimension (n) [out]

