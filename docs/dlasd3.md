```fortran
subroutine dlasd3 (
		nl,
		nr,
		sqre,
		k,
		d,
		q,
		ldq,
		dsigma,
		u,
		ldu,
		u2,
		*                          ldu2,
		vt,
		ldvt,
		vt2,
		ldvt2,
		idxc,
		ctot,
		z,
		*                          info
)
```

 DLASD3 finds all the square roots of the roots of the secular
 equation, as defined by the values in D and Z.  It makes the
 appropriate calls to DLASD4 and then updates the singular
 vectors by matrix multiplication.

 DLASD3 is called from DLASD1.

## Parameters
Nl : Integer [in]
> The row dimension of the upper block.  NL >= 1.

Nr : Integer [in]
> The row dimension of the lower block.  NR >= 1.

Sqre : Integer [in]
> = 0: the lower block is an NR-by-NR square matrix.
> = 1: the lower block is an NR-by-(NR+1) rectangular matrix.
> The bidiagonal matrix has N = NL + NR + 1 rows and
> M = N + SQRE >= N columns.

K : Integer [in]
> The size of the secular equation, 1 =< K = < N.

D : Double Precision Array, Dimension(k) [out]
> On exit the square roots of the roots of the secular equation,
> in ascending order.

Q : Double Precision Array, Dimension (ldq,k) [out]

Ldq : Integer [in]
> The leading dimension of the array Q.  LDQ >= K.

Dsigma : Double Precision Array, Dimension(k) [in]
> The first K elements of this array contain the old roots
> of the deflated updating problem.  These are the poles
> of the secular equation.

U : Double Precision Array, Dimension (ldu, N) [out]
> The last N - K columns of this matrix contain the deflated
> left singular vectors.

Ldu : Integer [in]
> The leading dimension of the array U.  LDU >= N.

U2 : Double Precision Array, Dimension (ldu2, N) [in]
> The first K columns of this matrix contain the non-deflated
> left singular vectors for the split problem.

Ldu2 : Integer [in]
> The leading dimension of the array U2.  LDU2 >= N.

Vt : Double Precision Array, Dimension (ldvt, M) [out]
> The last M - K columns of VT**T contain the deflated
> right singular vectors.

Ldvt : Integer [in]
> The leading dimension of the array VT.  LDVT >= N.

Vt2 : Double Precision Array, Dimension (ldvt2, N) [in,out]
> The first K columns of VT2**T contain the non-deflated
> right singular vectors for the split problem.

Ldvt2 : Integer [in]
> The leading dimension of the array VT2.  LDVT2 >= N.

Idxc : Integer Array, Dimension ( N ) [in]
> The permutation used to arrange the columns of U (and rows of
> VT) into three groups:  the first group contains non-zero
> entries only at and above (or before) NL +1; the second
> contains non-zero entries only at and below (or after) NL+2;
> and the third is dense. The first column of U and the row of
> VT are treated separately, however.
> The rows of the singular vectors found by DLASD4
> must be likewise permuted before the matrix multiplies can
> take place.

Ctot : Integer Array, Dimension ( 4 ) [in]
> A count of the total number of the various types of columns
> in U (or rows in VT), as described in IDXC. The fourth column
> type is any column which has been deflated.

Z : Double Precision Array, Dimension (k) [in,out]
> The first K elements of this array contain the components
> of the deflation-adjusted updating row vector.

Info : Integer [out]
> = 0:  successful exit.
> < 0:  if INFO = -i, the i-th argument had an illegal value.
> > 0:  if INFO = 1, a singular value did not converge

