```fortran
subroutine claqr5 (
		wantt,
		wantz,
		kacc22,
		n,
		ktop,
		kbot,
		nshfts,
		s,
		*                          h,
		ldh,
		iloz,
		ihiz,
		z,
		ldz,
		v,
		ldv,
		u,
		ldu,
		nv,
		*                          wv,
		ldwv,
		nh,
		wh,
		ldwh
)
```

    CLAQR5 called by CLAQR0 performs a
    single small-bulge multi-shift QR sweep.

## Parameters
Wantt : Logical [in]
> WANTT = .true. if the triangular Schur factor
> is being computed.  WANTT is set to .false. otherwise.

Wantz : Logical [in]
> WANTZ = .true. if the unitary Schur factor is being
> computed.  WANTZ is set to .false. otherwise.

Kacc22 : Integer With Value 0, 1, or 2. [in]
> Specifies the computation mode of far-from-diagonal
> orthogonal updates.
> = 0: CLAQR5 does not accumulate reflections and does not
> use matrix-matrix multiply to update far-from-diagonal
> matrix entries.
> = 1: CLAQR5 accumulates reflections and uses matrix-matrix
> multiply to update the far-from-diagonal matrix entries.
> = 2: Same as KACC22 = 1. This option used to enable exploiting
> the 2-by-2 structure during matrix multiplications, but
> this is no longer supported.

N : Integer [in]
> N is the order of the Hessenberg matrix H upon which this
> subroutine operates.

Ktop : Integer [in]

Kbot : Integer [in]
> These are the first and last rows and columns of an
> isolated diagonal block upon which the QR sweep is to be
> applied. It is assumed without a check that
> either KTOP = 1  or   H(KTOP,KTOP-1) = 0
> and
> either KBOT = N  or   H(KBOT+1,KBOT) = 0.

Nshfts : Integer [in]
> NSHFTS gives the number of simultaneous shifts.  NSHFTS
> must be positive and even.

S : Complex Array, Dimension (nshfts) [in,out]
> S contains the shifts of origin that define the multi-
> shift QR sweep.  On output S may be reordered.

H : Complex Array, Dimension (ldh,n) [in,out]
> On input H contains a Hessenberg matrix.  On output a
> multi-shift QR sweep with shifts SR(J)+i*SI(J) is applied
> to the isolated diagonal block in rows and columns KTOP
> through KBOT.

Ldh : Integer [in]
> LDH is the leading dimension of H just as declared in the
> calling procedure.  LDH >= MAX(1,N).

Iloz : Integer [in]

Ihiz : Integer [in]
> Specify the rows of Z to which transformations must be
> applied if WANTZ is .TRUE.. 1 <= ILOZ <= IHIZ <= N

Z : Complex Array, Dimension (ldz,ihiz) [in,out]
> If WANTZ = .TRUE., then the QR Sweep unitary
> similarity transformation is accumulated into
> Z(ILOZ:IHIZ,ILOZ:IHIZ) from the right.
> If WANTZ = .FALSE., then Z is unreferenced.

Ldz : Integer [in]
> LDA is the leading dimension of Z just as declared in
> the calling procedure. LDZ >= N.

V : Complex Array, Dimension (ldv,nshfts/2) [out]

Ldv : Integer [in]
> LDV is the leading dimension of V as declared in the
> calling procedure.  LDV >= 3.

U : Complex Array, Dimension (ldu,2*nshfts) [out]

Ldu : Integer [in]
> LDU is the leading dimension of U just as declared in the
> in the calling subroutine.  LDU >= 2*NSHFTS.

Nv : Integer [in]
> NV is the number of rows in WV agailable for workspace.
> NV >= 1.

Wv : Complex Array, Dimension (ldwv,2*nshfts) [out]

Ldwv : Integer [in]
> LDWV is the leading dimension of WV as declared in the
> in the calling subroutine.  LDWV >= NV.

Nh : Integer [in]
> NH is the number of columns in array WH available for
> workspace. NH >= 1.

Wh : Complex Array, Dimension (ldwh,nh) [out]

Ldwh : Integer [in]
> Leading dimension of WH just as declared in the
> calling procedure.  LDWH >= 2*NSHFTS.

