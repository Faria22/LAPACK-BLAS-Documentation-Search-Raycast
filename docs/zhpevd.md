```fortran
subroutine zhpevd (
		jobz,
		uplo,
		n,
		ap,
		w,
		z,
		ldz,
		work,
		lwork,
		*                          rwork,
		lrwork,
		iwork,
		liwork,
		info
)
```

 ZHPEVD computes all the eigenvalues and, optionally, eigenvectors of
 a complex Hermitian matrix A in packed storage.  If eigenvectors are
 desired, it uses a divide and conquer algorithm.


## Parameters
Jobz : Character*1 [in]
> = 'N':  Compute eigenvalues only;
> = 'V':  Compute eigenvalues and eigenvectors.

Uplo : Character*1 [in]
> = 'U':  Upper triangle of A is stored;
> = 'L':  Lower triangle of A is stored.

N : Integer [in]
> The order of the matrix A.  N >= 0.

Ap : Complex*16 Array, Dimension (n*(n+1)/2) [in,out]
> On entry, the upper or lower triangle of the Hermitian matrix
> A, packed columnwise in a linear array.  The j-th column of A
> is stored in the array AP as follows:
> if UPLO = 'U', AP(i + (j-1)*j/2) = A(i,j) for 1<=i<=j;
> if UPLO = 'L', AP(i + (j-1)*(2*n-j)/2) = A(i,j) for j<=i<=n.
> On exit, AP is overwritten by values generated during the
> reduction to tridiagonal form.  If UPLO = 'U', the diagonal
> and first superdiagonal of the tridiagonal matrix T overwrite
> the corresponding elements of A, and if UPLO = 'L', the
> diagonal and first subdiagonal of T overwrite the
> corresponding elements of A.

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
> On exit, if INFO = 0, WORK(1) returns the required LWORK.

Lwork : Integer [in]
> The dimension of array WORK.
> If N <= 1,               LWORK must be at least 1.
> If JOBZ = 'N' and N > 1, LWORK must be at least N.
> If JOBZ = 'V' and N > 1, LWORK must be at least 2*N.
> If LWORK = -1, then a workspace query is assumed; the routine
> only calculates the required sizes of the WORK, RWORK and
> IWORK arrays, returns these values as the first entries of
> the WORK, RWORK and IWORK arrays, and no error message
> related to LWORK or LRWORK or LIWORK is issued by XERBLA.

Rwork : Double Precision Array, Dimension (max(1,lrwork)) [out]
> On exit, if INFO = 0, RWORK(1) returns the required LRWORK.

Lrwork : Integer [in]
> The dimension of array RWORK.
> If N <= 1,               LRWORK must be at least 1.
> If JOBZ = 'N' and N > 1, LRWORK must be at least N.
> If JOBZ = 'V' and N > 1, LRWORK must be at least
> 1 + 5*N + 2*N**2.
> If LRWORK = -1, then a workspace query is assumed; the
> routine only calculates the required sizes of the WORK, RWORK
> and IWORK arrays, returns these values as the first entries
> of the WORK, RWORK and IWORK arrays, and no error message
> related to LWORK or LRWORK or LIWORK is issued by XERBLA.

Iwork : Integer Array, Dimension (max(1,liwork)) [out]
> On exit, if INFO = 0, IWORK(1) returns the required LIWORK.

Liwork : Integer [in]
> The dimension of array IWORK.
> If JOBZ  = 'N' or N <= 1, LIWORK must be at least 1.
> If JOBZ  = 'V' and N > 1, LIWORK must be at least 3 + 5*N.
> If LIWORK = -1, then a workspace query is assumed; the
> routine only calculates the required sizes of the WORK, RWORK
> and IWORK arrays, returns these values as the first entries
> of the WORK, RWORK and IWORK arrays, and no error message
> related to LWORK or LRWORK or LIWORK is issued by XERBLA.

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value.
> > 0:  if INFO = i, the algorithm failed to converge; i
> off-diagonal elements of an intermediate tridiagonal
> form did not converge to zero.

