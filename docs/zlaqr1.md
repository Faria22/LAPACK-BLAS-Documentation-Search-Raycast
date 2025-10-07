```fortran
subroutine zlaqr1	(	integer	n,
		complex*16, dimension(ldh, *)	h,
		integer	ldh,
		complex*16	s1,
		complex*16	s2,
		complex*16, dimension(*)	v )
```

      Given a 2-by-2 or 3-by-3 matrix H, ZLAQR1 sets v to a
      scalar multiple of the first column of the product

      (*)  K = (H - s1*I)*(H - s2*I)

      scaling to avoid overflows and most underflows.

      This is useful for starting double implicit shift bulges
      in the QR algorithm.

## Parameters
N : Integer [in]
> Order of the matrix H. N must be either 2 or 3.

H : Complex*16 Array, Dimension (ldh,n) [in]
> The 2-by-2 or 3-by-3 matrix H in (*).

Ldh : Integer [in]
> The leading dimension of H as declared in
> the calling procedure.  LDH >= N

S1 : Complex*16 [in]

S2 : Complex*16 [in]
> S1 and S2 are the shifts defining K in (*) above.

V : Complex*16 Array, Dimension (n) [out]
> A scalar multiple of the first column of the
> matrix K in (*).

