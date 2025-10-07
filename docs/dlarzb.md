```fortran
subroutine dlarzb	(	side,
		trans,
		direct,
		storev,
		m,
		n,
		k,
		l,
		v,
		*                          ldv,
		t,
		ldt,
		c,
		ldc,
		work,
		ldwork )
```

 DLARZB applies a real block reflector H or its transpose H**T to
 a real distributed M-by-N  C from the left or the right.

 Currently, only STOREV = 'R' and DIRECT = 'B' are supported.

## Parameters
Side : Character*1 [in]
> = 'L': apply H or H**T from the Left
> = 'R': apply H or H**T from the Right

Trans : Character*1 [in]
> = 'N': apply H (No transpose)
> = 'C': apply H**T (Transpose)

Direct : Character*1 [in]
> Indicates how H is formed from a product of elementary
> reflectors
> = 'F': H = H(1) H(2) . . . H(k) (Forward, not supported yet)
> = 'B': H = H(k) . . . H(2) H(1) (Backward)

Storev : Character*1 [in]
> Indicates how the vectors which define the elementary
> reflectors are stored:
> = 'C': Columnwise                        (not supported yet)
> = 'R': Rowwise

M : Integer [in]
> The number of rows of the matrix C.

N : Integer [in]
> The number of columns of the matrix C.

K : Integer [in]
> The order of the matrix T (= the number of elementary
> reflectors whose product defines the block reflector).

L : Integer [in]
> The number of columns of the matrix V containing the
> meaningful part of the Householder reflectors.
> If SIDE = 'L', M >= L >= 0, if SIDE = 'R', N >= L >= 0.

V : Double Precision Array, Dimension (ldv,nv). [in]
> If STOREV = 'C', NV = K; if STOREV = 'R', NV = L.

Ldv : Integer [in]
> The leading dimension of the array V.
> If STOREV = 'C', LDV >= L; if STOREV = 'R', LDV >= K.

T : Double Precision Array, Dimension (ldt,k) [in]
> The triangular K-by-K matrix T in the representation of the
> block reflector.

Ldt : Integer [in]
> The leading dimension of the array T. LDT >= K.

C : Double Precision Array, Dimension (ldc,n) [in,out]
> On entry, the M-by-N matrix C.
> On exit, C is overwritten by H*C or H**T*C or C*H or C*H**T.

Ldc : Integer [in]
> The leading dimension of the array C. LDC >= max(1,M).

Work : Double Precision Array, Dimension (ldwork,k) [out]

Ldwork : Integer [in]
> The leading dimension of the array WORK.
> If SIDE = 'L', LDWORK >= max(1,N);
> if SIDE = 'R', LDWORK >= max(1,M).

