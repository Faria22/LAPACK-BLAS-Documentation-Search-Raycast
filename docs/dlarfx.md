```fortran
subroutine dlarfx (
		character side,
		integer m,
		integer n,
		double precision, dimension(*) v,
		double precision tau,
		double precision, dimension(ldc, *) c,
		integer ldc,
		double precision, dimension(*) work
)
```

 DLARFX applies a real elementary reflector H to a real m by n
 matrix C, from either the left or the right. H is represented in the
 form

       H = I - tau * v * v**T

 where tau is a real scalar and v is a real vector.

 If tau = 0, then H is taken to be the unit matrix

 This version uses inline code if H has order < 11.

## Parameters
Side : Character*1 [in]
> = 'L': form  H * C
> = 'R': form  C * H

M : Integer [in]
> The number of rows of the matrix C.

N : Integer [in]
> The number of columns of the matrix C.

V : Double Precision Array, Dimension (m) If Side = 'l' [in]
> or (N) if SIDE = 'R'
> The vector v in the representation of H.

Tau : Double Precision [in]
> The value tau in the representation of H.

C : Double Precision Array, Dimension (ldc,n) [in,out]
> On entry, the m by n matrix C.
> On exit, C is overwritten by the matrix H * C if SIDE = 'L',
> or C * H if SIDE = 'R'.

Ldc : Integer [in]
> The leading dimension of the array C. LDC >= (1,M).

Work : Double Precision Array, Dimension [out]
> (N) if SIDE = 'L'
> or (M) if SIDE = 'R'
> WORK is not referenced if H has order < 11.

