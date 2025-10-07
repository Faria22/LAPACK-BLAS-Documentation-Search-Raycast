```fortran
subroutine cbbcsd	(	jobu1,
		jobu2,
		jobv1t,
		jobv2t,
		trans,
		m,
		p,
		q,
		*                          theta,
		phi,
		u1,
		ldu1,
		u2,
		ldu2,
		v1t,
		ldv1t,
		*                          v2t,
		ldv2t,
		b11d,
		b11e,
		b12d,
		b12e,
		b21d,
		b21e,
		*                          b22d,
		b22e,
		rwork,
		lrwork,
		info )
```

 CBBCSD computes the CS decomposition of a unitary matrix in
 bidiagonal-block form,


     [ B11 | B12 0  0 ]
     [  0  |  0 -I  0 ]
 X = [----------------]
     [ B21 | B22 0  0 ]
     [  0  |  0  0  I ]

                               [  C | -S  0  0 ]
                   [ U1 |    ] [  0 |  0 -I  0 ] [ V1 |    ]**H
                 = [---------] [---------------] [---------]   .
                   [    | U2 ] [  S |  C  0  0 ] [    | V2 ]
                               [  0 |  0  0  I ]

 X is M-by-M, its top-left block is P-by-Q, and Q must be no larger
 than P, M-P, or M-Q. (If Q is not the smallest index, then X must be
 transposed and/or permuted. This can be done in constant time using
 the TRANS and SIGNS options. See CUNCSD for details.)

 The bidiagonal matrices B11, B12, B21, and B22 are represented
 implicitly by angles THETA(1:Q) and PHI(1:Q-1).

 The unitary matrices U1, U2, V1T, and V2T are input/output.
 The input matrices are pre- or post-multiplied by the appropriate
 singular vector matrices.

## Parameters
Jobu1 : Character [in]
> = 'Y':      U1 is updated;
> otherwise:  U1 is not updated.

Jobu2 : Character [in]
> = 'Y':      U2 is updated;
> otherwise:  U2 is not updated.

Jobv1t : Character [in]
> = 'Y':      V1T is updated;
> otherwise:  V1T is not updated.

Jobv2t : Character [in]
> = 'Y':      V2T is updated;
> otherwise:  V2T is not updated.

Trans : Character [in]
> = 'T':      X, U1, U2, V1T, and V2T are stored in row-major
> order;
> otherwise:  X, U1, U2, V1T, and V2T are stored in column-
> major order.

M : Integer [in]
> The number of rows and columns in X, the unitary matrix in
> bidiagonal-block form.

P : Integer [in]
> The number of rows in the top-left block of X. 0 <= P <= M.

Q : Integer [in]
> The number of columns in the top-left block of X.
> 0 <= Q <= MIN(P,M-P,M-Q).

Theta : Real Array, Dimension (q) [in,out]
> On entry, the angles THETA(1),...,THETA(Q) that, along with
> PHI(1), ...,PHI(Q-1), define the matrix in bidiagonal-block
> form. On exit, the angles whose cosines and sines define the
> diagonal blocks in the CS decomposition.

Phi : Real Array, Dimension (q-1) [in,out]
> The angles PHI(1),...,PHI(Q-1) that, along with THETA(1),...,
> THETA(Q), define the matrix in bidiagonal-block form.

U1 : Complex Array, Dimension (ldu1,p) [in,out]
> On entry, a P-by-P matrix. On exit, U1 is postmultiplied
> by the left singular vector matrix common to [ B11 ; 0 ] and
> [ B12 0 0 ; 0 -I 0 0 ].

Ldu1 : Integer [in]
> The leading dimension of the array U1, LDU1 >= MAX(1,P).

U2 : Complex Array, Dimension (ldu2,m-p) [in,out]
> On entry, an (M-P)-by-(M-P) matrix. On exit, U2 is
> postmultiplied by the left singular vector matrix common to
> [ B21 ; 0 ] and [ B22 0 0 ; 0 0 I ].

Ldu2 : Integer [in]
> The leading dimension of the array U2, LDU2 >= MAX(1,M-P).

V1t : Complex Array, Dimension (ldv1t,q) [in,out]
> On entry, a Q-by-Q matrix. On exit, V1T is premultiplied
> by the conjugate transpose of the right singular vector
> matrix common to [ B11 ; 0 ] and [ B21 ; 0 ].

Ldv1t : Integer [in]
> The leading dimension of the array V1T, LDV1T >= MAX(1,Q).

V2t : Complex Array, Dimension (ldv2t,m-q) [in,out]
> On entry, an (M-Q)-by-(M-Q) matrix. On exit, V2T is
> premultiplied by the conjugate transpose of the right
> singular vector matrix common to [ B12 0 0 ; 0 -I 0 ] and
> [ B22 0 0 ; 0 0 I ].

Ldv2t : Integer [in]
> The leading dimension of the array V2T, LDV2T >= MAX(1,M-Q).

B11d : Real Array, Dimension (q) [out]
> When CBBCSD converges, B11D contains the cosines of THETA(1),
> ..., THETA(Q). If CBBCSD fails to converge, then B11D
> contains the diagonal of the partially reduced top-left
> block.

B11e : Real Array, Dimension (q-1) [out]
> When CBBCSD converges, B11E contains zeros. If CBBCSD fails
> to converge, then B11E contains the superdiagonal of the
> partially reduced top-left block.

B12d : Real Array, Dimension (q) [out]
> When CBBCSD converges, B12D contains the negative sines of
> THETA(1), ..., THETA(Q). If CBBCSD fails to converge, then
> B12D contains the diagonal of the partially reduced top-right
> block.

B12e : Real Array, Dimension (q-1) [out]
> When CBBCSD converges, B12E contains zeros. If CBBCSD fails
> to converge, then B12E contains the subdiagonal of the
> partially reduced top-right block.

B21d : Real Array, Dimension (q) [out]
> When CBBCSD converges, B21D contains the negative sines of
> THETA(1), ..., THETA(Q). If CBBCSD fails to converge, then
> B21D contains the diagonal of the partially reduced bottom-left
> block.

B21e : Real Array, Dimension (q-1) [out]
> When CBBCSD converges, B21E contains zeros. If CBBCSD fails
> to converge, then B21E contains the subdiagonal of the
> partially reduced bottom-left block.

B22d : Real Array, Dimension (q) [out]
> When CBBCSD converges, B22D contains the negative sines of
> THETA(1), ..., THETA(Q). If CBBCSD fails to converge, then
> B22D contains the diagonal of the partially reduced bottom-right
> block.

B22e : Real Array, Dimension (q-1) [out]
> When CBBCSD converges, B22E contains zeros. If CBBCSD fails
> to converge, then B22E contains the subdiagonal of the
> partially reduced bottom-right block.

Rwork : Real Array, Dimension (max(1,lrwork)) [out]
> On exit, if INFO = 0, RWORK(1) returns the optimal LRWORK.

Lrwork : Integer [in]
> The dimension of the array RWORK. LRWORK >= MAX(1,8*Q).
> If LRWORK = -1, then a workspace query is assumed; the
> routine only calculates the optimal size of the RWORK array,
> returns this value as the first entry of the work array, and
> no error message related to LRWORK is issued by XERBLA.

Info : Integer [out]
> = 0:  successful exit.
> < 0:  if INFO = -i, the i-th argument had an illegal value.
> > 0:  if CBBCSD did not converge, INFO specifies the number
> of nonzero entries in PHI, and B11D, B11E, etc.,
> contain the partially reduced matrix.

