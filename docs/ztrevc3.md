```fortran
subroutine ztrevc3	(	side,
		howmny,
		select,
		n,
		t,
		ldt,
		vl,
		ldvl,
		vr,
		*      $                    ldvr,
		mm,
		m,
		work,
		lwork,
		rwork,
		lrwork,
		info )
```

 ZTREVC3 computes some or all of the right and/or left eigenvectors of
 a complex upper triangular matrix T.
 Matrices of this type are produced by the Schur factorization of
 a complex general matrix:  A = Q*T*Q**H, as computed by ZHSEQR.

 The right eigenvector x and the left eigenvector y of T corresponding
 to an eigenvalue w are defined by:

              T*x = w*x,     (y**H)*T = w*(y**H)

 where y**H denotes the conjugate transpose of the vector y.
 The eigenvalues are not input to this routine, but are read directly
 from the diagonal of T.

 This routine returns the matrices X and/or Y of right and left
 eigenvectors of T, or the products Q*X and/or Q*Y, where Q is an
 input matrix. If Q is the unitary factor that reduces a matrix A to
 Schur form T, then Q*X and Q*Y are the matrices of right and left
 eigenvectors of A.

 This uses a Level 3 BLAS version of the back transformation.

## Parameters
Side : Character*1 [in]
> = 'R':  compute right eigenvectors only;
> = 'L':  compute left eigenvectors only;
> = 'B':  compute both right and left eigenvectors.

Howmny : Character*1 [in]
> = 'A':  compute all right and/or left eigenvectors;
> = 'B':  compute all right and/or left eigenvectors,
> backtransformed using the matrices supplied in
> VR and/or VL;
> = 'S':  compute selected right and/or left eigenvectors,
> as indicated by the logical array SELECT.

Select : Logical Array, Dimension (n) [in]
> If HOWMNY = 'S', SELECT specifies the eigenvectors to be
> computed.
> The eigenvector corresponding to the j-th eigenvalue is
> computed if SELECT(j) = .TRUE..
> Not referenced if HOWMNY = 'A' or 'B'.

N : Integer [in]
> The order of the matrix T. N >= 0.

T : Complex*16 Array, Dimension (ldt,n) [in,out]
> The upper triangular matrix T.  T is modified, but restored
> on exit.

Ldt : Integer [in]
> The leading dimension of the array T. LDT >= max(1,N).

Vl : Complex*16 Array, Dimension (ldvl,mm) [in,out]
> On entry, if SIDE = 'L' or 'B' and HOWMNY = 'B', VL must
> contain an N-by-N matrix Q (usually the unitary matrix Q of
> Schur vectors returned by ZHSEQR).
> On exit, if SIDE = 'L' or 'B', VL contains:
> if HOWMNY = 'A', the matrix Y of left eigenvectors of T;
> if HOWMNY = 'B', the matrix Q*Y;
> if HOWMNY = 'S', the left eigenvectors of T specified by
> SELECT, stored consecutively in the columns
> of VL, in the same order as their
> eigenvalues.
> Not referenced if SIDE = 'R'.

Ldvl : Integer [in]
> The leading dimension of the array VL.
> LDVL >= 1, and if SIDE = 'L' or 'B', LDVL >= N.

Vr : Complex*16 Array, Dimension (ldvr,mm) [in,out]
> On entry, if SIDE = 'R' or 'B' and HOWMNY = 'B', VR must
> contain an N-by-N matrix Q (usually the unitary matrix Q of
> Schur vectors returned by ZHSEQR).
> On exit, if SIDE = 'R' or 'B', VR contains:
> if HOWMNY = 'A', the matrix X of right eigenvectors of T;
> if HOWMNY = 'B', the matrix Q*X;
> if HOWMNY = 'S', the right eigenvectors of T specified by
> SELECT, stored consecutively in the columns
> of VR, in the same order as their
> eigenvalues.
> Not referenced if SIDE = 'L'.

Ldvr : Integer [in]
> The leading dimension of the array VR.
> LDVR >= 1, and if SIDE = 'R' or 'B', LDVR >= N.

Mm : Integer [in]
> The number of columns in the arrays VL and/or VR. MM >= M.

M : Integer [out]
> The number of columns in the arrays VL and/or VR actually
> used to store the eigenvectors.
> If HOWMNY = 'A' or 'B', M is set to N.
> Each selected eigenvector occupies one column.

Work : Complex*16 Array, Dimension (max(1,lwork)) [out]

Lwork : Integer [in]
> The dimension of array WORK. LWORK >= max(1,2*N).
> For optimum performance, LWORK >= N + 2*N*NB, where NB is
> the optimal blocksize.
> If LWORK = -1, then a workspace query is assumed; the routine
> only calculates the optimal size of the WORK array, returns
> this value as the first entry of the WORK array, and no error
> message related to LWORK is issued by XERBLA.

Rwork : Double Precision Array, Dimension (lrwork) [out]

Lrwork : Integer [in]
> The dimension of array RWORK. LRWORK >= max(1,N).
> If LRWORK = -1, then a workspace query is assumed; the routine
> only calculates the optimal size of the RWORK array, returns
> this value as the first entry of the RWORK array, and no error
> message related to LRWORK is issued by XERBLA.

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value

