```fortran  
subroutine cheevd (  
jobz,  
uplo,  
n,  
a,  
lda,  
w,  
work,  
lwork,  
rwork,  
*                          lrwork,  
iwork,  
liwork,  
info  
)  
```  
  
CHEEVD computes all eigenvalues and, optionally, eigenvectors of a  
complex Hermitian matrix A.  If eigenvectors are desired, it uses a  
divide and conquer algorithm.  
  
  
## Parameters  
Jobz : Character*1 [in]  
> = 'N':  Compute eigenvalues only;  
> = 'V':  Compute eigenvalues and eigenvectors.  
  
Uplo : Character*1 [in]  
> = 'U':  Upper triangle of A is stored;  
> = 'L':  Lower triangle of A is stored.  
  
N : Integer [in]  
> The order of the matrix A.  N >= 0.  
  
A : Complex Array, Dimension (lda, N) [in,out]  
> On entry, the Hermitian matrix A.  If UPLO = 'U', the  
> leading N-by-N upper triangular part of A contains the  
> upper triangular part of the matrix A.  If UPLO = 'L',  
> the leading N-by-N lower triangular part of A contains  
> the lower triangular part of the matrix A.  
> On exit, if JOBZ = 'V', then if INFO = 0, A contains the  
> orthonormal eigenvectors of the matrix A.  
> If JOBZ = 'N', then on exit the lower triangle (if UPLO='L')  
> or the upper triangle (if UPLO='U') of A, including the  
> diagonal, is destroyed.  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,N).  
  
W : Real Array, Dimension (n) [out]  
> If INFO = 0, the eigenvalues in ascending order.  
  
Work : Complex Array, Dimension (max(1,lwork)) [out]  
> On exit, if INFO = 0, WORK(1) returns the optimal LWORK.  
  
Lwork : Integer [in]  
> The length of the array WORK.  
> If N <= 1,                LWORK must be at least 1.  
> If JOBZ  = 'N' and N > 1, LWORK must be at least N + 1.  
> If LWORK = -1, then a workspace query is assumed; the routine  
> only calculates the optimal sizes of the WORK, RWORK and  
> IWORK arrays, returns these values as the first entries of  
> the WORK, RWORK and IWORK arrays, and no error message  
> related to LWORK or LRWORK or LIWORK is issued by XERBLA.  
  
Rwork : Real Array, Dimension (max(1,lrwork)) [out]  
> On exit, if INFO = 0, RWORK(1) returns the optimal LRWORK.  
  
Lrwork : Integer [in]  
> The dimension of the array RWORK.  
> If N <= 1,                LRWORK must be at least 1.  
> If JOBZ  = 'N' and N > 1, LRWORK must be at least N.  
> If JOBZ  = 'V' and N > 1, LRWORK must be at least  
> If LRWORK = -1, then a workspace query is assumed; the  
> routine only calculates the optimal sizes of the WORK, RWORK  
> and IWORK arrays, returns these values as the first entries  
> of the WORK, RWORK and IWORK arrays, and no error message  
> related to LWORK or LRWORK or LIWORK is issued by XERBLA.  
  
Iwork : Integer Array, Dimension (max(1,liwork)) [out]  
> On exit, if INFO = 0, IWORK(1) returns the optimal LIWORK.  
  
Liwork : Integer [in]  
> The dimension of the array IWORK.  
> If N <= 1,                LIWORK must be at least 1.  
> If JOBZ  = 'N' and N > 1, LIWORK must be at least 1.  
> If LIWORK = -1, then a workspace query is assumed; the  
> routine only calculates the optimal sizes of the WORK, RWORK  
> and IWORK arrays, returns these values as the first entries  
> of the WORK, RWORK and IWORK arrays, and no error message  
> related to LWORK or LRWORK or LIWORK is issued by XERBLA.  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
> > 0:  if INFO = i and JOBZ = 'N', then the algorithm failed  
> to converge; i off-diagonal elements of an intermediate  
> tridiagonal form did not converge to zero;  
> if INFO = i and JOBZ = 'V', then the algorithm failed  
> to compute an eigenvalue while working on the submatrix  
> lying in rows and columns INFO/(N+1) through  
> mod(INFO,N+1).  
  
