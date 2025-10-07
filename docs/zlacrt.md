```fortran
subroutine zlacrt	(	integer	n,
		complex*16, dimension(*)	cx,
		integer	incx,
		complex*16, dimension(*)	cy,
		integer	incy,
		complex*16	c,
		complex*16	s )
```

 ZLACRT performs the operation

    (  c  s )( x )  ==> ( x )
    ( -s  c )( y )      ( y )

 where c and s are complex and the vectors x and y are complex.

## Parameters
N : Integer [in]
> The number of elements in the vectors CX and CY.

Cx : Complex*16 Array, Dimension (n) [in,out]
> On input, the vector x.
> On output, CX is overwritten with c*x + s*y.

Incx : Integer [in]
> The increment between successive values of CX.  INCX <> 0.

Cy : Complex*16 Array, Dimension (n) [in,out]
> On input, the vector y.
> On output, CY is overwritten with -s*x + c*y.

Incy : Integer [in]
> The increment between successive values of CY.  INCY <> 0.

C : Complex*16 [in]

S : Complex*16 [in]
> C and S define the matrix
> [  C   S  ].
> [ -S   C  ]

