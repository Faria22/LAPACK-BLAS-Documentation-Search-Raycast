```fortran
subroutine ztgex2	(	wantq,
		wantz,
		n,
		a,
		lda,
		b,
		ldb,
		q,
		ldq,
		z,
		*                          ldz,
		j1,
		info )
```

 ZTGEX2 swaps adjacent diagonal 1 by 1 blocks (A11,B11) and (A22,B22)
 in an upper triangular matrix pair (A, B) by an unitary equivalence
 transformation.

 (A, B) must be in generalized Schur canonical form, that is, A and
 B are both upper triangular.

 Optionally, the matrices Q and Z of generalized Schur vectors are
 updated.

        Q(in) * A(in) * Z(in)**H = Q(out) * A(out) * Z(out)**H
        Q(in) * B(in) * Z(in)**H = Q(out) * B(out) * Z(out)**H


## Parameters
Wantq : Logical [in]
> .TRUE. : update the left transformation matrix Q;
> .FALSE.: do not update Q.

Wantz : Logical [in]
> .TRUE. : update the right transformation matrix Z;
> .FALSE.: do not update Z.

N : Integer [in]
> The order of the matrices A and B. N >= 0.

A : Complex*16 Array, Dimensions (lda,n) [in,out]
> On entry, the matrix A in the pair (A, B).
> On exit, the updated matrix A.

Lda : Integer [in]
> The leading dimension of the array A. LDA >= max(1,N).

B : Complex*16 Array, Dimensions (ldb,n) [in,out]
> On entry, the matrix B in the pair (A, B).
> On exit, the updated matrix B.

Ldb : Integer [in]
> The leading dimension of the array B. LDB >= max(1,N).

Q : Complex*16 Array, Dimension (ldq,n) [in,out]
> If WANTQ = .TRUE, on entry, the unitary matrix Q. On exit,
> the updated matrix Q.
> Not referenced if WANTQ = .FALSE..

Ldq : Integer [in]
> The leading dimension of the array Q. LDQ >= 1;
> If WANTQ = .TRUE., LDQ >= N.

Z : Complex*16 Array, Dimension (ldz,n) [in,out]
> If WANTZ = .TRUE, on entry, the unitary matrix Z. On exit,
> the updated matrix Z.
> Not referenced if WANTZ = .FALSE..

Ldz : Integer [in]
> The leading dimension of the array Z. LDZ >= 1;
> If WANTZ = .TRUE., LDZ >= N.

J1 : Integer [in]
> The index to the first block (A11, B11).

Info : Integer [out]
> =0:  Successful exit.
> =1:  The transformed matrix pair (A, B) would be too far
> from generalized Schur form; the problem is ill-
> conditioned.

