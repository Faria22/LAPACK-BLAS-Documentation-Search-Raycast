```fortran
subroutine dlaqz2	(	ilq,
		ilz,
		k,
		istartm,
		istopm,
		ihi,
		a,
		lda,
		b,
		*     $    ldb,
		nq,
		qstart,
		q,
		ldq,
		nz,
		zstart,
		z,
		ldz )
```

      DLAQZ2 chases a 2x2 shift bulge in a matrix pencil down a single position

## Parameters
Ilq : Logical [in]
> Determines whether or not to update the matrix Q

Ilz : Logical [in]
> Determines whether or not to update the matrix Z

K : Integer [in]
> Index indicating the position of the bulge.
> On entry, the bulge is located in
> (A(k+1:k+2,k:k+1),B(k+1:k+2,k:k+1)).
> On exit, the bulge is located in
> (A(k+2:k+3,k+1:k+2),B(k+2:k+3,k+1:k+2)).

Istartm : Integer [in]

Istopm : Integer [in]
> Updates to (A,B) are restricted to
> (istartm:k+3,k:istopm). It is assumed
> without checking that istartm <= k+1 and
> k+2 <= istopm

Ihi : Integer [in]

A : Double Precision Array, Dimension (lda,n) [inout]

Lda : Integer [in]
> The leading dimension of A as declared in
> the calling procedure.

B : Double Precision Array, Dimension (ldb,n) [inout]

Ldb : Integer [in]
> The leading dimension of B as declared in
> the calling procedure.

Nq : Integer [in]
> The order of the matrix Q

Qstart : Integer [in]
> Start index of the matrix Q. Rotations are applied
> To columns k+2-qStart:k+4-qStart of Q.

Q : Double Precision Array, Dimension (ldq,nq) [inout]

Ldq : Integer [in]
> The leading dimension of Q as declared in
> the calling procedure.

Nz : Integer [in]
> The order of the matrix Z

Zstart : Integer [in]
> Start index of the matrix Z. Rotations are applied
> To columns k+1-qStart:k+3-qStart of Z.

Z : Double Precision Array, Dimension (ldz,nz) [inout]

Ldz : Integer [in]
> The leading dimension of Q as declared in
> the calling procedure.

