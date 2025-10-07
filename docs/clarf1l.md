```fortran
subroutine clarf1l	(	character	side,
		integer	m,
		integer	n,
		complex, dimension(*)	v,
		integer	incv,
		complex	tau,
		complex, dimension(ldc, *)	c,
		integer	ldc,
		complex, dimension(*)	work )
```

 CLARF1L applies a complex elementary reflector H to a complex m by n matrix
 C, from either the left or the right. H is represented in the form

       H = I - tau * v * v**H

 where tau is a real scalar and v is a real vector assuming v(lastv) = 1,
 where lastv is the last non-zero element.

 If tau = 0, then H is taken to be the unit matrix.

 To apply H**H (the conjugate transpose of H), supply conjg(tau) instead
 tau.

## Parameters
Side : Character*1 [in]
> = 'L': form  H * C
> = 'R': form  C * H

M : Integer [in]
> The number of rows of the matrix C.

N : Integer [in]
> The number of columns of the matrix C.

V : Complex Array, Dimension [in]
> (1 + (M-1)*abs(INCV)) if SIDE = 'L'
> or (1 + (N-1)*abs(INCV)) if SIDE = 'R'
> The vector v in the representation of H. V is not used if
> TAU = 0.

Incv : Integer [in]
> The increment between elements of v. INCV > 0.

Tau : Complex [in]
> The value tau in the representation of H.

C : Complex Array, Dimension (ldc,n) [in,out]
> On entry, the m by n matrix C.
> On exit, C is overwritten by the matrix H * C if SIDE = 'L',
> or C * H if SIDE = 'R'.

Ldc : Integer [in]
> The leading dimension of the array C. LDC >= max(1,M).

Work : Complex Array, Dimension [out]
> (N) if SIDE = 'L'
> or (M) if SIDE = 'R'

