```fortran
subroutine dlaein (
		rightv,
		noinit,
		n,
		h,
		ldh,
		wr,
		wi,
		vr,
		vi,
		b,
		*                          ldb,
		work,
		eps3,
		smlnum,
		bignum,
		info
)
```

 DLAEIN uses inverse iteration to find a right or left eigenvector
 corresponding to the eigenvalue (WR,WI) of a real upper Hessenberg
 matrix H.

## Parameters
Rightv : Logical [in]
> = .TRUE. : compute right eigenvector;
> = .FALSE.: compute left eigenvector.

Noinit : Logical [in]
> = .TRUE. : no initial vector supplied in (VR,VI).
> = .FALSE.: initial vector supplied in (VR,VI).

N : Integer [in]
> The order of the matrix H.  N >= 0.

H : Double Precision Array, Dimension (ldh,n) [in]
> The upper Hessenberg matrix H.

Ldh : Integer [in]
> The leading dimension of the array H.  LDH >= max(1,N).

Wr : Double Precision [in]

Wi : Double Precision [in]
> The real and imaginary parts of the eigenvalue of H whose
> corresponding right or left eigenvector is to be computed.

Vr : Double Precision Array, Dimension (n) [in,out]

Vi : Double Precision Array, Dimension (n) [in,out]
> On entry, if NOINIT = .FALSE. and WI = 0.0, VR must contain
> a real starting vector for inverse iteration using the real
> eigenvalue WR; if NOINIT = .FALSE. and WI.ne.0.0, VR and VI
> must contain the real and imaginary parts of a complex
> starting vector for inverse iteration using the complex
> eigenvalue (WR,WI); otherwise VR and VI need not be set.
> On exit, if WI = 0.0 (real eigenvalue), VR contains the
> computed real eigenvector; if WI.ne.0.0 (complex eigenvalue),
> VR and VI contain the real and imaginary parts of the
> computed complex eigenvector. The eigenvector is normalized
> so that the component of largest magnitude has magnitude 1;
> here the magnitude of a complex number (x,y) is taken to be
> |x| + |y|.
> VI is not referenced if WI = 0.0.

B : Double Precision Array, Dimension (ldb,n) [out]

Ldb : Integer [in]
> The leading dimension of the array B.  LDB >= N+1.

Work : Double Precision Array, Dimension (n) [out]

Eps3 : Double Precision [in]
> A small machine-dependent value which is used to perturb
> close eigenvalues, and to replace zero pivots.

Smlnum : Double Precision [in]
> A machine-dependent value close to the underflow threshold.

Bignum : Double Precision [in]
> A machine-dependent value close to the overflow threshold.

Info : Integer [out]
> = 0:  successful exit
> = 1:  inverse iteration did not converge; VR is set to the
> last iterate, and so is VI if WI.ne.0.0.

