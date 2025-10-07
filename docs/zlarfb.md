```fortran
subroutine zlarfb (
		side,
		trans,
		direct,
		storev,
		m,
		n,
		k,
		v,
		ldv,
		*                          t,
		ldt,
		c,
		ldc,
		work,
		ldwork
)
```

 ZLARFB applies a complex block reflector H or its transpose H**H to a
 complex M-by-N matrix C, from either the left or the right.

## Parameters
Side : Character*1 [in]
> = 'L': apply H or H**H from the Left
> = 'R': apply H or H**H from the Right

Trans : Character*1 [in]
> = 'N': apply H (No transpose)
> = 'C': apply H**H (Conjugate transpose)

Direct : Character*1 [in]
> Indicates how H is formed from a product of elementary
> reflectors
> = 'F': H = H(1) H(2) . . . H(k) (Forward)
> = 'B': H = H(k) . . . H(2) H(1) (Backward)

Storev : Character*1 [in]
> Indicates how the vectors which define the elementary
> reflectors are stored:
> = 'C': Columnwise
> = 'R': Rowwise

M : Integer [in]
> The number of rows of the matrix C.

N : Integer [in]
> The number of columns of the matrix C.

K : Integer [in]
> The order of the matrix T (= the number of elementary
> reflectors whose product defines the block reflector).
> If SIDE = 'L', M >= K >= 0;
> if SIDE = 'R', N >= K >= 0.

V : Complex*16 Array, Dimension [in]
> (LDV,K) if STOREV = 'C'
> (LDV,M) if STOREV = 'R' and SIDE = 'L'
> (LDV,N) if STOREV = 'R' and SIDE = 'R'
> See Further Details.

Ldv : Integer [in]
> The leading dimension of the array V.
> If STOREV = 'C' and SIDE = 'L', LDV >= max(1,M);
> if STOREV = 'C' and SIDE = 'R', LDV >= max(1,N);
> if STOREV = 'R', LDV >= K.

T : Complex*16 Array, Dimension (ldt,k) [in]
> The triangular K-by-K matrix T in the representation of the
> block reflector.

Ldt : Integer [in]
> The leading dimension of the array T. LDT >= K.

C : Complex*16 Array, Dimension (ldc,n) [in,out]
> On entry, the M-by-N matrix C.
> On exit, C is overwritten by H*C or H**H*C or C*H or C*H**H.

Ldc : Integer [in]
> The leading dimension of the array C. LDC >= max(1,M).

Work : Complex*16 Array, Dimension (ldwork,k) [out]

Ldwork : Integer [in]
> The leading dimension of the array WORK.
> If SIDE = 'L', LDWORK >= max(1,N);
> if SIDE = 'R', LDWORK >= max(1,M).

