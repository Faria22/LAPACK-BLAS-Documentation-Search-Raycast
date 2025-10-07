```fortran
subroutine slas2	(	real	f,
		real	g,
		real	h,
		real	ssmin,
		real	ssmax )
```

 SLAS2  computes the singular values of the 2-by-2 matrix
    [  F   G  ]
    [  0   H  ].
 On return, SSMIN is the smaller singular value and SSMAX is the
 larger singular value.

## Parameters
F : Real [in]
> The (1,1) element of the 2-by-2 matrix.

G : Real [in]
> The (1,2) element of the 2-by-2 matrix.

H : Real [in]
> The (2,2) element of the 2-by-2 matrix.

Ssmin : Real [out]
> The smaller singular value.

Ssmax : Real [out]
> The larger singular value.

