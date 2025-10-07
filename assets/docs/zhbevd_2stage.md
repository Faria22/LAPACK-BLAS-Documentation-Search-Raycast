```fortran
subroutine zhbevd_2stage (
		jobz,
		uplo,
		n,
		kd,
		ab,
		ldab,
		w,
		z,
		ldz,
		*                                 work,
		lwork,
		rwork,
		lrwork,
		iwork,
		*                                 liwork,
		info
)
```

 ZHBEVD_2STAGE computes all the eigenvalues and, optionally, eigenvectors of
 a complex Hermitian band matrix A using the 2stage technique for
 the reduction to tridiagonal.  If eigenvectors are desired, it
 uses a divide and conquer algorithm.


## Parameters
Jobz : Character*1 [in]
> = 'N':  Compute eigenvalues only;
> = 'V':  Compute eigenvalues and eigenvectors.
> Not available in this release.

Uplo : Character*1 [in]
> = 'U':  Upper triangle of A is stored;
> = 'L':  Lower triangle of A is stored.

N : Integer [in]
> The order of the matrix A.  N >= 0.

Kd : Integer [in]
> The number of superdiagonals of the matrix A if UPLO = 'U',
> or the number of subdiagonals if UPLO = 'L'.  KD >= 0.

Ab : Complex*16 Array, Dimension (ldab, N) [in,out]
> On entry, the upper or lower triangle of the Hermitian band
> matrix A, stored in the first KD+1 rows of the array.  The
> j-th column of A is stored in the j-th column of the array AB
> as follows:
> if UPLO = 'U', AB(kd+1+i-j,j) = A(i,j) for max(1,j-kd)<=i<=j;
> if UPLO = 'L', AB(1+i-j,j)    = A(i,j) for j<=i<=min(n,j+kd).
> On exit, AB is overwritten by values generated during the
> reduction to tridiagonal form.  If UPLO = 'U', the first
> superdiagonal and the diagonal of the tridiagonal matrix T
> are returned in rows KD and KD+1 of AB, and if UPLO = 'L',
> the diagonal and first subdiagonal of T are returned in the
> first two rows of AB.

Ldab : Integer [in]
> The leading dimension of the array AB.  LDAB >= KD + 1.

W : Double Precision Array, Dimension (n) [out]
> If INFO = 0, the eigenvalues in ascending order.

Z : Complex*16 Array, Dimension (ldz, N) [out]
> If JOBZ = 'V', then if INFO = 0, Z contains the orthonormal
> eigenvectors of the matrix A, with the i-th column of Z
> holding the eigenvector associated with W(i).
> If JOBZ = 'N', then Z is not referenced.

Ldz : Integer [in]
> The leading dimension of the array Z.  LDZ >= 1, and if
> JOBZ = 'V', LDZ >= max(1,N).

Work : Complex*16 Array, Dimension (max(1,lwork)) [out]
> On exit, if INFO = 0, WORK(1) returns the optimal LWORK.

Lwork : Integer [in]
> The length of the array WORK. LWORK >= 1, when N <= 1;
> otherwise
> If JOBZ = 'N' and N > 1, LWORK must be queried.
> LWORK = MAX(1, dimension) where
> dimension = (2KD+1)*N + KD*NTHREADS
> where KD is the size of the band.
> NTHREADS is the number of threads used when
> openMP compilation is enabled, otherwise =1.
> If JOBZ = 'V' and N > 1, LWORK must be queried. Not yet available.
> If LWORK = -1, then a workspace query is assumed; the routine
> only calculates the optimal sizes of the WORK, RWORK and
> IWORK arrays, returns these values as the first entries of
> the WORK, RWORK and IWORK arrays, and no error message
> related to LWORK or LRWORK or LIWORK is issued by XERBLA.

Rwork : Double Precision Array, [out]
> dimension (LRWORK)
> On exit, if INFO = 0, RWORK(1) returns the optimal LRWORK.

Lrwork : Integer [in]
> The dimension of array RWORK.
> If N <= 1,               LRWORK must be at least 1.
> If JOBZ = 'N' and N > 1, LRWORK must be at least N.
> If JOBZ = 'V' and N > 1, LRWORK must be at least
> 1 + 5*N + 2*N**2.
> If LRWORK = -1, then a workspace query is assumed; the
> routine only calculates the optimal sizes of the WORK, RWORK
> and IWORK arrays, returns these values as the first entries
> of the WORK, RWORK and IWORK arrays, and no error message
> related to LWORK or LRWORK or LIWORK is issued by XERBLA.

Iwork : Integer Array, Dimension (max(1,liwork)) [out]
> On exit, if INFO = 0, IWORK(1) returns the optimal LIWORK.

Liwork : Integer [in]
> The dimension of array IWORK.
> If JOBZ = 'N' or N <= 1, LIWORK must be at least 1.
> If JOBZ = 'V' and N > 1, LIWORK must be at least 3 + 5*N .
> If LIWORK = -1, then a workspace query is assumed; the
> routine only calculates the optimal sizes of the WORK, RWORK
> and IWORK arrays, returns these values as the first entries
> of the WORK, RWORK and IWORK arrays, and no error message
> related to LWORK or LRWORK or LIWORK is issued by XERBLA.

Info : Integer [out]
> = 0:  successful exit.
> < 0:  if INFO = -i, the i-th argument had an illegal value.
> > 0:  if INFO = i, the algorithm failed to converge; i
> off-diagonal elements of an intermediate tridiagonal
> form did not converge to zero.

