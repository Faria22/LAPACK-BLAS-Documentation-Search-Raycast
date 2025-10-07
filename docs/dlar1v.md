```fortran
subroutine dlar1v	(	n,
		b1,
		bn,
		lambda,
		d,
		l,
		ld,
		lld,
		*                  pivmin,
		gaptol,
		z,
		wantnc,
		negcnt,
		ztz,
		mingma,
		*                  r,
		isuppz,
		nrminv,
		resid,
		rqcorr,
		work )
```

 DLAR1V computes the (scaled) r-th column of the inverse of
 the sumbmatrix in rows B1 through BN of the tridiagonal matrix
 L D L**T - sigma I. When sigma is close to an eigenvalue, the
 computed vector is an accurate eigenvector. Usually, r corresponds
 to the index where the eigenvector is largest in magnitude.
 The following steps accomplish this computation :
 (a) Stationary qd transform,  L D L**T - sigma I = L(+) D(+) L(+)**T,
 (b) Progressive qd transform, L D L**T - sigma I = U(-) D(-) U(-)**T,
 (c) Computation of the diagonal elements of the inverse of
     L D L**T - sigma I by combining the above transforms, and choosing
     r as the index where the diagonal of the inverse is (one of the)
     largest in magnitude.
 (d) Computation of the (scaled) r-th column of the inverse using the
     twisted factorization obtained by combining the top part of the
     the stationary and the bottom part of the progressive transform.

## Parameters
N : Integer [in]
> The order of the matrix L D L**T.

B1 : Integer [in]
> First index of the submatrix of L D L**T.

Bn : Integer [in]
> Last index of the submatrix of L D L**T.

Lambda : Double Precision [in]
> The shift. In order to compute an accurate eigenvector,
> LAMBDA should be a good approximation to an eigenvalue
> of L D L**T.

L : Double Precision Array, Dimension (n-1) [in]
> The (n-1) subdiagonal elements of the unit bidiagonal matrix
> L, in elements 1 to N-1.

D : Double Precision Array, Dimension (n) [in]
> The n diagonal elements of the diagonal matrix D.

Ld : Double Precision Array, Dimension (n-1) [in]
> The n-1 elements L(i)*D(i).

Lld : Double Precision Array, Dimension (n-1) [in]
> The n-1 elements L(i)*L(i)*D(i).

Pivmin : Double Precision [in]
> The minimum pivot in the Sturm sequence.

Gaptol : Double Precision [in]
> Tolerance that indicates when eigenvector entries are negligible
> w.r.t. their contribution to the residual.

Z : Double Precision Array, Dimension (n) [in,out]
> On input, all entries of Z must be set to 0.
> On output, Z contains the (scaled) r-th column of the
> inverse. The scaling is such that Z(R) equals 1.

Wantnc : Logical [in]
> Specifies whether NEGCNT has to be computed.

Negcnt : Integer [out]
> If WANTNC is .TRUE. then NEGCNT = the number of pivots < pivmin
> in the  matrix factorization L D L**T, and NEGCNT = -1 otherwise.

Ztz : Double Precision [out]
> The square of the 2-norm of Z.

Mingma : Double Precision [out]
> The reciprocal of the largest (in magnitude) diagonal
> element of the inverse of L D L**T - sigma I.

R : Integer [in,out]
> The twist index for the twisted factorization used to
> compute Z.
> On input, 0 <= R <= N. If R is input as 0, R is set to
> the index where (L D L**T - sigma I)^{-1} is largest
> in magnitude. If 1 <= R <= N, R is unchanged.
> On output, R contains the twist index used to compute Z.
> Ideally, R designates the position of the maximum entry in the
> eigenvector.

Isuppz : Integer Array, Dimension (2) [out]
> The support of the vector in Z, i.e., the vector Z is
> nonzero only in elements ISUPPZ(1) through ISUPPZ( 2 ).

Nrminv : Double Precision [out]
> NRMINV = 1/SQRT( ZTZ )

Resid : Double Precision [out]
> The residual of the FP vector.
> RESID = ABS( MINGMA )/SQRT( ZTZ )

Rqcorr : Double Precision [out]
> The Rayleigh Quotient correction to LAMBDA.
> RQCORR = MINGMA*TMP

Work : Double Precision Array, Dimension (4*n) [out]

