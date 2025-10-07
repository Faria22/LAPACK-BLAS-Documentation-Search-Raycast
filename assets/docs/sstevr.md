```fortran
subroutine sstevr (
		jobz,
		range,
		n,
		d,
		e,
		vl,
		vu,
		il,
		iu,
		abstol,
		*                          m,
		w,
		z,
		ldz,
		isuppz,
		work,
		lwork,
		iwork,
		*                          liwork,
		info
)
```

 SSTEVR computes selected eigenvalues and, optionally, eigenvectors
 of a real symmetric tridiagonal matrix T.  Eigenvalues and
 eigenvectors can be selected by specifying either a range of values
 or a range of indices for the desired eigenvalues.

 Whenever possible, SSTEVR calls SSTEMR to compute the
 eigenspectrum using Relatively Robust Representations.  SSTEMR
 computes eigenvalues by the dqds algorithm, while orthogonal
 eigenvectors are computed from various "good" L D L^T representations
 (also known as Relatively Robust Representations). Gram-Schmidt
 orthogonalization is avoided as far as possible. More specifically,
 the various steps of the algorithm are as follows. For the i-th
 unreduced block of T,
    (a) Compute T - sigma_i = L_i D_i L_i^T, such that L_i D_i L_i^T
         is a relatively robust representation,
    (b) Compute the eigenvalues, lambda_j, of L_i D_i L_i^T to high
        relative accuracy by the dqds algorithm,
    (c) If there is a cluster of close eigenvalues, "choose" sigma_i
        close to the cluster, and go to step (a),
    (d) Given the approximate eigenvalue lambda_j of L_i D_i L_i^T,
        compute the corresponding eigenvector by forming a
        rank-revealing twisted factorization.
 The desired accuracy of the output can be specified by the input
 parameter ABSTOL.

 For more details, see "A new O(n^2) algorithm for the symmetric
 tridiagonal eigenvalue/eigenvector problem", by Inderjit Dhillon,
 Computer Science Division Technical Report No. UCB//CSD-97-971,
 UC Berkeley, May 1997.


 Note 1 : SSTEVR calls SSTEMR when the full spectrum is requested
 on machines which conform to the ieee-754 floating point standard.
 SSTEVR calls SSTEBZ and SSTEIN on non-ieee machines and
 when partial spectrum requests are made.

 Normal execution of SSTEMR may create NaNs and infinities and
 hence may abort due to a floating point exception in environments
 which do not handle NaNs and infinities in the ieee standard default
 manner.

## Parameters
Jobz : Character*1 [in]
> = 'N':  Compute eigenvalues only;
> = 'V':  Compute eigenvalues and eigenvectors.

Range : Character*1 [in]
> = 'A': all eigenvalues will be found.
> = 'V': all eigenvalues in the half-open interval (VL,VU]
> will be found.
> = 'I': the IL-th through IU-th eigenvalues will be found.
> For RANGE = 'V' or 'I' and IU - IL < N - 1, SSTEBZ and
> SSTEIN are called

N : Integer [in]
> The order of the matrix.  N >= 0.

D : Real Array, Dimension (n) [in,out]
> On entry, the n diagonal elements of the tridiagonal matrix
> A.
> On exit, D may be multiplied by a constant factor chosen
> to avoid over/underflow in computing the eigenvalues.

E : Real Array, Dimension (max(1,n-1)) [in,out]
> On entry, the (n-1) subdiagonal elements of the tridiagonal
> matrix A in elements 1 to N-1 of E.
> On exit, E may be multiplied by a constant factor chosen
> to avoid over/underflow in computing the eigenvalues.

Vl : Real [in]
> If RANGE='V', the lower bound of the interval to
> be searched for eigenvalues. VL < VU.
> Not referenced if RANGE = 'A' or 'I'.

Vu : Real [in]
> If RANGE='V', the upper bound of the interval to
> be searched for eigenvalues. VL < VU.
> Not referenced if RANGE = 'A' or 'I'.

Il : Integer [in]
> If RANGE='I', the index of the
> smallest eigenvalue to be returned.
> 1 <= IL <= IU <= N, if N > 0; IL = 1 and IU = 0 if N = 0.
> Not referenced if RANGE = 'A' or 'V'.

Iu : Integer [in]
> If RANGE='I', the index of the
> largest eigenvalue to be returned.
> 1 <= IL <= IU <= N, if N > 0; IL = 1 and IU = 0 if N = 0.
> Not referenced if RANGE = 'A' or 'V'.

Abstol : Real [in]
> The absolute error tolerance for the eigenvalues.
> An approximate eigenvalue is accepted as converged
> when it is determined to lie in an interval [a,b]
> of width less than or equal to
> ABSTOL + EPS *   max( |a|,|b| ) ,
> where EPS is the machine precision.  If ABSTOL is less than
> or equal to zero, then  EPS*|T|  will be used in its place,
> where |T| is the 1-norm of the tridiagonal matrix obtained
> by reducing A to tridiagonal form.
> See "Computing Small Singular Values of Bidiagonal Matrices
> with Guaranteed High Relative Accuracy," by Demmel and
> Kahan, LAPACK Working Note #3.
> If high relative accuracy is important, set ABSTOL to
> SLAMCH( 'Safe minimum' ).  Doing so will guarantee that
> eigenvalues are computed to high relative accuracy when
> possible in future releases.  The current code does not
> make any guarantees about high relative accuracy, but
> future releases will. See J. Barlow and J. Demmel,
> "Computing Accurate Eigensystems of Scaled Diagonally
> Dominant Matrices", LAPACK Working Note #7, for a discussion
> of which matrices define their eigenvalues to high relative
> accuracy.

M : Integer [out]
> The total number of eigenvalues found.  0 <= M <= N.
> If RANGE = 'A', M = N, and if RANGE = 'I', M = IU-IL+1.

W : Real Array, Dimension (n) [out]
> The first M elements contain the selected eigenvalues in
> ascending order.

Z : Real Array, Dimension (ldz, Max(1,m) ) [out]
> If JOBZ = 'V', then if INFO = 0, the first M columns of Z
> contain the orthonormal eigenvectors of the matrix A
> corresponding to the selected eigenvalues, with the i-th
> column of Z holding the eigenvector associated with W(i).
> Note: the user must ensure that at least max(1,M) columns are
> supplied in the array Z; if RANGE = 'V', the exact value of M
> is not known in advance and an upper bound must be used.

Ldz : Integer [in]
> The leading dimension of the array Z.  LDZ >= 1, and if
> JOBZ = 'V', LDZ >= max(1,N).

Isuppz : Integer Array, Dimension ( 2*max(1,m) ) [out]
> The support of the eigenvectors in Z, i.e., the indices
> indicating the nonzero elements in Z. The i-th eigenvector
> is nonzero only in elements ISUPPZ( 2*i-1 ) through
> ISUPPZ( 2*i ).
> Implemented only for RANGE = 'A' or 'I' and IU - IL = N - 1

Work : Real Array, Dimension (max(1,lwork)) [out]
> On exit, if INFO = 0, WORK(1) returns the optimal (and
> minimal) LWORK.

Lwork : Integer [in]
> The dimension of the array WORK.  LWORK >= 20*N.
> If LWORK = -1, then a workspace query is assumed; the routine
> only calculates the optimal sizes of the WORK and IWORK
> arrays, returns these values as the first entries of the WORK
> and IWORK arrays, and no error message related to LWORK or
> LIWORK is issued by XERBLA.

Iwork : Integer Array, Dimension (max(1,liwork)) [out]
> On exit, if INFO = 0, IWORK(1) returns the optimal (and
> minimal) LIWORK.

Liwork : Integer [in]
> The dimension of the array IWORK.  LIWORK >= 10*N.
> If LIWORK = -1, then a workspace query is assumed; the
> routine only calculates the optimal sizes of the WORK and
> IWORK arrays, returns these values as the first entries of
> the WORK and IWORK arrays, and no error message related to
> LWORK or LIWORK is issued by XERBLA.

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value
> > 0:  Internal error

