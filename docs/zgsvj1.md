```fortran
subroutine zgsvj1	(	jobv,
		m,
		n,
		n1,
		a,
		lda,
		d,
		sva,
		mv,
		v,
		ldv,
		*                          eps,
		sfmin,
		tol,
		nsweep,
		work,
		lwork,
		info )
```

 ZGSVJ1 is called from ZGESVJ as a pre-processor and that is its main
 purpose. It applies Jacobi rotations in the same way as ZGESVJ does, but
 it targets only particular pivots and it does not check convergence
 (stopping criterion). Few tuning parameters (marked by [TP]) are
 available for the implementer.

 Further Details
 ~~~~~~~~~~~~~~~
 ZGSVJ1 applies few sweeps of Jacobi rotations in the column space of
 the input M-by-N matrix A. The pivot pairs are taken from the (1,2)
 off-diagonal block in the corresponding N-by-N Gram matrix A^T * A. The
 block-entries (tiles) of the (1,2) off-diagonal block are marked by the
 [x]'s in the following scheme:

    | *  *  * [x] [x] [x]|
    | *  *  * [x] [x] [x]|    Row-cycling in the nblr-by-nblc [x] blocks.
    | *  *  * [x] [x] [x]|    Row-cyclic pivoting inside each [x] block.
    |[x] [x] [x] *  *  * |
    |[x] [x] [x] *  *  * |
    |[x] [x] [x] *  *  * |

 In terms of the columns of A, the first N1 columns are rotated 'against'
 the remaining N-N1 columns, trying to increase the angle between the
 corresponding subspaces. The off-diagonal block is N1-by(N-N1) and it is
 tiled using quadratic tiles of side KBL. Here, KBL is a tuning parameter.
 The number of sweeps is given in NSWEEP and the orthogonality threshold
 is given in TOL.

## Parameters
Jobv : Character*1 [in]
> Specifies whether the output from this procedure is used
> to compute the matrix V:
> = 'V': the product of the Jacobi rotations is accumulated
> by postmultiplying the N-by-N array V.
> (See the description of V.)
> = 'A': the product of the Jacobi rotations is accumulated
> by postmultiplying the MV-by-N array V.
> (See the descriptions of MV and V.)
> = 'N': the Jacobi rotations are not accumulated.

M : Integer [in]
> The number of rows of the input matrix A.  M >= 0.

N : Integer [in]
> The number of columns of the input matrix A.
> M >= N >= 0.

N1 : Integer [in]
> N1 specifies the 2 x 2 block partition, the first N1 columns are
> rotated 'against' the remaining N-N1 columns of A.

A : Complex*16 Array, Dimension (lda,n) [in,out]
> On entry, M-by-N matrix A, such that A*diag(D) represents
> the input matrix.
> On exit,
> A_onexit * D_onexit represents the input matrix A*diag(D)
> post-multiplied by a sequence of Jacobi rotations, where the
> rotation threshold and the total number of sweeps are given in
> TOL and NSWEEP, respectively.
> (See the descriptions of N1, D, TOL and NSWEEP.)

Lda : Integer [in]
> The leading dimension of the array A.  LDA >= max(1,M).

D : Complex*16 Array, Dimension (n) [in,out]
> The array D accumulates the scaling factors from the fast scaled
> Jacobi rotations.
> On entry, A*diag(D) represents the input matrix.
> On exit, A_onexit*diag(D_onexit) represents the input matrix
> post-multiplied by a sequence of Jacobi rotations, where the
> rotation threshold and the total number of sweeps are given in
> TOL and NSWEEP, respectively.
> (See the descriptions of N1, A, TOL and NSWEEP.)

Sva : Double Precision Array, Dimension (n) [in,out]
> On entry, SVA contains the Euclidean norms of the columns of
> the matrix A*diag(D).
> On exit, SVA contains the Euclidean norms of the columns of
> the matrix onexit*diag(D_onexit).

Mv : Integer [in]
> If JOBV = 'A', then MV rows of V are post-multiplied by a
> sequence of Jacobi rotations.
> If JOBV = 'N',   then MV is not referenced.

V : Complex*16 Array, Dimension (ldv,n) [in,out]
> If JOBV = 'V' then N rows of V are post-multiplied by a
> sequence of Jacobi rotations.
> If JOBV = 'A' then MV rows of V are post-multiplied by a
> sequence of Jacobi rotations.
> If JOBV = 'N',   then V is not referenced.

Ldv : Integer [in]
> The leading dimension of the array V,  LDV >= 1.
> If JOBV = 'V', LDV >= N.
> If JOBV = 'A', LDV >= MV.

Eps : Double Precision [in]
> EPS = DLAMCH('Epsilon')

Sfmin : Double Precision [in]
> SFMIN = DLAMCH('Safe Minimum')

Tol : Double Precision [in]
> TOL is the threshold for Jacobi rotations. For a pair
> A(:,p), A(:,q) of pivot columns, the Jacobi rotation is
> applied only if ABS(COS(angle(A(:,p),A(:,q)))) > TOL.

Nsweep : Integer [in]
> NSWEEP is the number of sweeps of Jacobi rotations to be
> performed.

Work : Complex*16 Array, Dimension (lwork) [out]

Lwork : Integer [in]
> LWORK is the dimension of WORK. LWORK >= M.

Info : Integer [out]
> = 0:  successful exit.
> < 0:  if INFO = -i, then the i-th argument had an illegal value

