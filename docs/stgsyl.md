```fortran
subroutine stgsyl (
		trans,
		ijob,
		m,
		n,
		a,
		lda,
		b,
		ldb,
		c,
		ldc,
		d,
		*                          ldd,
		e,
		lde,
		f,
		ldf,
		scale,
		dif,
		work,
		lwork,
		*                          iwork,
		info
)
```

 STGSYL solves the generalized Sylvester equation:

             A * R - L * B = scale * C                 (1)
             D * R - L * E = scale * F

 where R and L are unknown m-by-n matrices, (A, D), (B, E) and
 (C, F) are given matrix pairs of size m-by-m, n-by-n and m-by-n,
 respectively, with real entries. (A, D) and (B, E) must be in
 generalized (real) Schur canonical form, i.e. A, B are upper quasi
 triangular and D, E are upper triangular.

 The solution (R, L) overwrites (C, F). 0 <= SCALE <= 1 is an output
 scaling factor chosen to avoid overflow.

 In matrix notation (1) is equivalent to solve  Zx = scale b, where
 Z is defined as

            Z = [ kron(In, A)  -kron(B**T, Im) ]         (2)
                [ kron(In, D)  -kron(E**T, Im) ].

 Here Ik is the identity matrix of size k and X**T is the transpose of
 X. kron(X, Y) is the Kronecker product between the matrices X and Y.

 If TRANS = 'T', STGSYL solves the transposed system Z**T*y = scale*b,
 which is equivalent to solve for R and L in

             A**T * R + D**T * L = scale * C           (3)
             R * B**T + L * E**T = scale * -F

 This case (TRANS = 'T') is used to compute an one-norm-based estimate
 of Dif[(A,D), (B,E)], the separation between the matrix pairs (A,D)
 and (B,E), using SLACON.

 If IJOB >= 1, STGSYL computes a Frobenius norm-based estimate
 of Dif[(A,D),(B,E)]. That is, the reciprocal of a lower bound on the
 reciprocal of the smallest singular value of Z. See [1-2] for more
 information.

 This is a level 3 BLAS algorithm.

## Parameters
Trans : Character*1 [in]
> = 'N': solve the generalized Sylvester equation (1).
> = 'T': solve the 'transposed' system (3).

Ijob : Integer [in]
> Specifies what kind of functionality to be performed.
> = 0: solve (1) only.
> = 1: The functionality of 0 and 3.
> = 2: The functionality of 0 and 4.
> = 3: Only an estimate of Dif[(A,D), (B,E)] is computed.
> (look ahead strategy IJOB  = 1 is used).
> = 4: Only an estimate of Dif[(A,D), (B,E)] is computed.
> ( SGECON on sub-systems is used ).
> Not referenced if TRANS = 'T'.

M : Integer [in]
> The order of the matrices A and D, and the row dimension of
> the matrices C, F, R and L.

N : Integer [in]
> The order of the matrices B and E, and the column dimension
> of the matrices C, F, R and L.

A : Real Array, Dimension (lda, M) [in]
> The upper quasi triangular matrix A.

Lda : Integer [in]
> The leading dimension of the array A. LDA >= max(1, M).

B : Real Array, Dimension (ldb, N) [in]
> The upper quasi triangular matrix B.

Ldb : Integer [in]
> The leading dimension of the array B. LDB >= max(1, N).

C : Real Array, Dimension (ldc, N) [in,out]
> On entry, C contains the right-hand-side of the first matrix
> equation in (1) or (3).
> On exit, if IJOB = 0, 1 or 2, C has been overwritten by
> the solution R. If IJOB = 3 or 4 and TRANS = 'N', C holds R,
> the solution achieved during the computation of the
> Dif-estimate.

Ldc : Integer [in]
> The leading dimension of the array C. LDC >= max(1, M).

D : Real Array, Dimension (ldd, M) [in]
> The upper triangular matrix D.

Ldd : Integer [in]
> The leading dimension of the array D. LDD >= max(1, M).

E : Real Array, Dimension (lde, N) [in]
> The upper triangular matrix E.

Lde : Integer [in]
> The leading dimension of the array E. LDE >= max(1, N).

F : Real Array, Dimension (ldf, N) [in,out]
> On entry, F contains the right-hand-side of the second matrix
> equation in (1) or (3).
> On exit, if IJOB = 0, 1 or 2, F has been overwritten by
> the solution L. If IJOB = 3 or 4 and TRANS = 'N', F holds L,
> the solution achieved during the computation of the
> Dif-estimate.

Ldf : Integer [in]
> The leading dimension of the array F. LDF >= max(1, M).

Dif : Real [out]
> On exit DIF is the reciprocal of a lower bound of the
> reciprocal of the Dif-function, i.e. DIF is an upper bound of
> Dif[(A,D), (B,E)] = sigma_min(Z), where Z as in (2).
> IF IJOB = 0 or TRANS = 'T', DIF is not touched.

Scale : Real [out]
> On exit SCALE is the scaling factor in (1) or (3).
> If 0 < SCALE < 1, C and F hold the solutions R and L, resp.,
> to a slightly perturbed system but the input matrices A, B, D
> and E have not been changed. If SCALE = 0, C and F hold the
> solutions R and L, respectively, to the homogeneous system
> with C = F = 0. Normally, SCALE = 1.

Work : Real Array, Dimension (max(1,lwork)) [out]
> On exit, if INFO = 0, WORK(1) returns the optimal LWORK.

Lwork : Integer [in]
> The dimension of the array WORK. LWORK > = 1.
> If IJOB = 1 or 2 and TRANS = 'N', LWORK >= max(1,2*M*N).
> If LWORK = -1, then a workspace query is assumed; the routine
> only calculates the optimal size of the WORK array, returns
> this value as the first entry of the WORK array, and no error
> message related to LWORK is issued by XERBLA.

Iwork : Integer Array, Dimension (m+n+6) [out]

Info : Integer [out]
> =0: successful exit
> <0: If INFO = -i, the i-th argument had an illegal value.
> >0: (A, D) and (B, E) have common or close eigenvalues.

