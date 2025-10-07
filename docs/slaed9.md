```fortran
subroutine slaed9 (
		k,
		kstart,
		kstop,
		n,
		d,
		q,
		ldq,
		rho,
		dlambda,
		*                          w,
		s,
		lds,
		info
)
```

 SLAED9 finds the roots of the secular equation, as defined by the
 values in D, Z, and RHO, between KSTART and KSTOP.  It makes the
 appropriate calls to SLAED4 and then stores the new matrix of
 eigenvectors for use in calculating the next level of Z vectors.

## Parameters
K : Integer [in]
> The number of terms in the rational function to be solved by
> SLAED4.  K >= 0.

Kstart : Integer [in]

Kstop : Integer [in]
> The updated eigenvalues Lambda(I), KSTART <= I <= KSTOP
> are to be computed.  1 <= KSTART <= KSTOP <= K.

N : Integer [in]
> The number of rows and columns in the Q matrix.
> N >= K (delation may result in N > K).

D : Real Array, Dimension (n) [out]
> D(I) contains the updated eigenvalues
> for KSTART <= I <= KSTOP.

Q : Real Array, Dimension (ldq,n) [out]

Ldq : Integer [in]
> The leading dimension of the array Q.  LDQ >= max( 1, N ).

Rho : Real [in]
> The value of the parameter in the rank one update equation.
> RHO >= 0 required.

Dlambda : Real Array, Dimension (k) [in]
> The first K elements of this array contain the old roots
> of the deflated updating problem.  These are the poles
> of the secular equation.

W : Real Array, Dimension (k) [in]
> The first K elements of this array contain the components
> of the deflation-adjusted updating vector.

S : Real Array, Dimension (lds, K) [out]
> Will contain the eigenvectors of the repaired matrix which
> will be stored for subsequent Z vector calculation and
> multiplied by the previously accumulated eigenvectors
> to update the system.

Lds : Integer [in]
> The leading dimension of S.  LDS >= max( 1, K ).

Info : Integer [out]
> = 0:  successful exit.
> < 0:  if INFO = -i, the i-th argument had an illegal value.
> > 0:  if INFO = 1, an eigenvalue did not converge

