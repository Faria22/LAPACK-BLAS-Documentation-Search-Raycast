```fortran
subroutine claein	(	rightv,
		noinit,
		n,
		h,
		ldh,
		w,
		v,
		b,
		ldb,
		rwork,
		*                          eps3,
		smlnum,
		info )
```

 CLAEIN uses inverse iteration to find a right or left eigenvector
 corresponding to the eigenvalue W of a complex upper Hessenberg
 matrix H.

## Parameters
Rightv : Logical [in]
> = .TRUE. : compute right eigenvector;
> = .FALSE.: compute left eigenvector.

Noinit : Logical [in]
> = .TRUE. : no initial vector supplied in V
> = .FALSE.: initial vector supplied in V.

N : Integer [in]
> The order of the matrix H.  N >= 0.

H : Complex Array, Dimension (ldh,n) [in]
> The upper Hessenberg matrix H.

Ldh : Integer [in]
> The leading dimension of the array H.  LDH >= max(1,N).

W : Complex [in]
> The eigenvalue of H whose corresponding right or left
> eigenvector is to be computed.

V : Complex Array, Dimension (n) [in,out]
> On entry, if NOINIT = .FALSE., V must contain a starting
> vector for inverse iteration; otherwise V need not be set.
> On exit, V contains the computed eigenvector, normalized so
> that the component of largest magnitude has magnitude 1; here
> the magnitude of a complex number (x,y) is taken to be
> |x| + |y|.

B : Complex Array, Dimension (ldb,n) [out]

Ldb : Integer [in]
> The leading dimension of the array B.  LDB >= max(1,N).

Rwork : Real Array, Dimension (n) [out]

Eps3 : Real [in]
> A small machine-dependent value which is used to perturb
> close eigenvalues, and to replace zero pivots.

Smlnum : Real [in]
> A machine-dependent value close to the underflow threshold.

Info : Integer [out]
> = 0:  successful exit
> = 1:  inverse iteration did not converge; V is set to the
> last iterate.

