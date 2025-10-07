```fortran
subroutine dlasy2 (
		ltranl,
		ltranr,
		isgn,
		n1,
		n2,
		tl,
		ldtl,
		tr,
		*                          ldtr,
		b,
		ldb,
		scale,
		x,
		ldx,
		xnorm,
		info
)
```

 DLASY2 solves for the N1 by N2 matrix X, 1 <= N1,N2 <= 2, in

        op(TL)*X + ISGN*X*op(TR) = SCALE*B,

 where TL is N1 by N1, TR is N2 by N2, B is N1 by N2, and ISGN = 1 or
 -1.  op(T) = T or T**T, where T**T denotes the transpose of T.

## Parameters
Ltranl : Logical [in]
> On entry, LTRANL specifies the op(TL):
> = .FALSE., op(TL) = TL,
> = .TRUE., op(TL) = TL**T.

Ltranr : Logical [in]
> On entry, LTRANR specifies the op(TR):
> = .FALSE., op(TR) = TR,
> = .TRUE., op(TR) = TR**T.

Isgn : Integer [in]
> On entry, ISGN specifies the sign of the equation
> as described before. ISGN may only be 1 or -1.

N1 : Integer [in]
> On entry, N1 specifies the order of matrix TL.
> N1 may only be 0, 1 or 2.

N2 : Integer [in]
> On entry, N2 specifies the order of matrix TR.
> N2 may only be 0, 1 or 2.

Tl : Double Precision Array, Dimension (ldtl,2) [in]
> On entry, TL contains an N1 by N1 matrix.

Ldtl : Integer [in]
> The leading dimension of the matrix TL. LDTL >= max(1,N1).

Tr : Double Precision Array, Dimension (ldtr,2) [in]
> On entry, TR contains an N2 by N2 matrix.

Ldtr : Integer [in]
> The leading dimension of the matrix TR. LDTR >= max(1,N2).

B : Double Precision Array, Dimension (ldb,2) [in]
> On entry, the N1 by N2 matrix B contains the right-hand
> side of the equation.

Ldb : Integer [in]
> The leading dimension of the matrix B. LDB >= max(1,N1).

Scale : Double Precision [out]
> On exit, SCALE contains the scale factor. SCALE is chosen
> less than or equal to 1 to prevent the solution overflowing.

X : Double Precision Array, Dimension (ldx,2) [out]
> On exit, X contains the N1 by N2 solution.

Ldx : Integer [in]
> The leading dimension of the matrix X. LDX >= max(1,N1).

Xnorm : Double Precision [out]
> On exit, XNORM is the infinity-norm of the solution.

Info : Integer [out]
> On exit, INFO is set to
> 0: successful exit.
> 1: TL and TR have too close eigenvalues, so TL or
> TR is perturbed to get a nonsingular equation.
> NOTE: In the interests of speed, this routine does not
> check the inputs for errors.

