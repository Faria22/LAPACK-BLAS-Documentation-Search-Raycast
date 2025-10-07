```fortran
subroutine slasd8	(	icompq,
		k,
		d,
		z,
		vf,
		vl,
		difl,
		difr,
		lddifr,
		*                          dsigma,
		work,
		info )
```

 SLASD8 finds the square roots of the roots of the secular equation,
 as defined by the values in DSIGMA and Z. It makes the appropriate
 calls to SLASD4, and stores, for each  element in D, the distance
 to its two nearest poles (elements in DSIGMA). It also updates
 the arrays VF and VL, the first and last components of all the
 right singular vectors of the original bidiagonal matrix.

 SLASD8 is called from SLASD6.

## Parameters
Icompq : Integer [in]
> Specifies whether singular vectors are to be computed in
> factored form in the calling routine:
> = 0: Compute singular values only.
> = 1: Compute singular vectors in factored form as well.

K : Integer [in]
> The number of terms in the rational function to be solved
> by SLASD4.  K >= 1.

D : Real Array, Dimension ( K ) [out]
> On output, D contains the updated singular values.

Z : Real Array, Dimension ( K ) [in,out]
> On entry, the first K elements of this array contain the
> components of the deflation-adjusted updating row vector.
> On exit, Z is updated.

Vf : Real Array, Dimension ( K ) [in,out]
> On entry, VF contains  information passed through DBEDE8.
> On exit, VF contains the first K components of the first
> components of all right singular vectors of the bidiagonal
> matrix.

Vl : Real Array, Dimension ( K ) [in,out]
> On entry, VL contains  information passed through DBEDE8.
> On exit, VL contains the first K components of the last
> components of all right singular vectors of the bidiagonal
> matrix.

Difl : Real Array, Dimension ( K ) [out]
> On exit, DIFL(I) = D(I) - DSIGMA(I).

Difr : Real Array, [out]
> dimension ( LDDIFR, 2 ) if ICOMPQ = 1 and
> dimension ( K ) if ICOMPQ = 0.
> On exit, DIFR(I,1) = D(I) - DSIGMA(I+1), DIFR(K,1) is not
> defined and will not be referenced.
> If ICOMPQ = 1, DIFR(1:K,2) is an array containing the
> normalizing factors for the right singular vector matrix.

Lddifr : Integer [in]
> The leading dimension of DIFR, must be at least K.

Dsigma : Real Array, Dimension ( K ) [in]
> On entry, the first K elements of this array contain the old
> roots of the deflated updating problem.  These are the poles
> of the secular equation.

Work : Real Array, Dimension (3*k) [out]

Info : Integer [out]
> = 0:  successful exit.
> < 0:  if INFO = -i, the i-th argument had an illegal value.
> > 0:  if INFO = 1, a singular value did not converge

