```fortran
subroutine ztgexc	(	wantq,
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
		ifst,
		ilst,
		info )
```

 ZTGEXC reorders the generalized Schur decomposition of a complex
 matrix pair (A,B), using an unitary equivalence transformation
 (A, B) := Q * (A, B) * Z**H, so that the diagonal block of (A, B) with
 row index IFST is moved to row ILST.

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

A : Complex*16 Array, Dimension (lda,n) [in,out]
> On entry, the upper triangular matrix A in the pair (A, B).
> On exit, the updated matrix A.

Lda : Integer [in]
> The leading dimension of the array A. LDA >= max(1,N).

B : Complex*16 Array, Dimension (ldb,n) [in,out]
> On entry, the upper triangular matrix B in the pair (A, B).
> On exit, the updated matrix B.

Ldb : Integer [in]
> The leading dimension of the array B. LDB >= max(1,N).

Q : Complex*16 Array, Dimension (ldq,n) [in,out]
> On entry, if WANTQ = .TRUE., the unitary matrix Q.
> On exit, the updated matrix Q.
> If WANTQ = .FALSE., Q is not referenced.

Ldq : Integer [in]
> The leading dimension of the array Q. LDQ >= 1;
> If WANTQ = .TRUE., LDQ >= N.

Z : Complex*16 Array, Dimension (ldz,n) [in,out]
> On entry, if WANTZ = .TRUE., the unitary matrix Z.
> On exit, the updated matrix Z.
> If WANTZ = .FALSE., Z is not referenced.

Ldz : Integer [in]
> The leading dimension of the array Z. LDZ >= 1;
> If WANTZ = .TRUE., LDZ >= N.

Ifst : Integer [in]

Ilst : Integer [in,out]
> Specify the reordering of the diagonal blocks of (A, B).
> The block with row index IFST is moved to row ILST, by a
> sequence of swapping between adjacent blocks.

Info : Integer [out]
> =0:  Successful exit.
> <0:  if INFO = -i, the i-th argument had an illegal value.
> =1:  The transformed matrix pair (A, B) would be too far
> from generalized Schur form; the problem is ill-
> conditioned. (A, B) may have been partially reordered,
> and ILST points to the first row of the current
> position of the block being moved.

