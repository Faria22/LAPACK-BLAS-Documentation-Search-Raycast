```fortran  
subroutine chbgvd (  
jobz,  
uplo,  
n,  
ka,  
kb,  
ab,  
ldab,  
bb,  
ldbb,  
w,  
*                          z,  
ldz,  
work,  
lwork,  
rwork,  
lrwork,  
iwork,  
*                          liwork,  
info  
)  
```  
  
CHBGVD computes all the eigenvalues, and optionally, the eigenvectors  
of a complex generalized Hermitian-definite banded eigenproblem, of  
the form A*x=(lambda)*B*x. Here A and B are assumed to be Hermitian  
and banded, and B is also positive definite.  If eigenvectors are  
desired, it uses a divide and conquer algorithm.  
  
  
## Parameters  
Jobz : Character*1 [in]  
> = 'N':  Compute eigenvalues only;  
> = 'V':  Compute eigenvalues and eigenvectors.  
  
Uplo : Character*1 [in]  
> = 'U':  Upper triangles of A and B are stored;  
> = 'L':  Lower triangles of A and B are stored.  
  
N : Integer [in]  
> The order of the matrices A and B.  N >= 0.  
  
Ka : Integer [in]  
> The number of superdiagonals of the matrix A if UPLO = 'U',  
> or the number of subdiagonals if UPLO = 'L'. KA >= 0.  
  
Kb : Integer [in]  
> The number of superdiagonals of the matrix B if UPLO = 'U',  
> or the number of subdiagonals if UPLO = 'L'. KB >= 0.  
  
Ab : Complex Array, Dimension (ldab, N) [in,out]  
> On entry, the upper or lower triangle of the Hermitian band  
> matrix A, stored in the first ka+1 rows of the array.  The  
> j-th column of A is stored in the j-th column of the array AB  
> as follows:  
> if UPLO = 'U', AB(ka+1+i-j,j) = A(i,j) for max(1,j-ka)<=i<=j;  
> if UPLO = 'L', AB(1+i-j,j)    = A(i,j) for j<=i<=min(n,j+ka).  
> On exit, the contents of AB are destroyed.  
  
Ldab : Integer [in]  
> The leading dimension of the array AB.  LDAB >= KA+1.  
  
Bb : Complex Array, Dimension (ldbb, N) [in,out]  
> On entry, the upper or lower triangle of the Hermitian band  
> matrix B, stored in the first kb+1 rows of the array.  The  
> j-th column of B is stored in the j-th column of the array BB  
> as follows:  
> if UPLO = 'U', BB(kb+1+i-j,j) = B(i,j) for max(1,j-kb)<=i<=j;  
> if UPLO = 'L', BB(1+i-j,j)    = B(i,j) for j<=i<=min(n,j+kb).  
> On exit, the factor S from the split Cholesky factorization  
  
Ldbb : Integer [in]  
> The leading dimension of the array BB.  LDBB >= KB+1.  
  
W : Real Array, Dimension (n) [out]  
> If INFO = 0, the eigenvalues in ascending order.  
  
Z : Complex Array, Dimension (ldz, N) [out]  
> If JOBZ = 'V', then if INFO = 0, Z contains the matrix Z of  
> eigenvectors, with the i-th column of Z holding the  
> eigenvector associated with W(i). The eigenvectors are  
> If JOBZ = 'N', then Z is not referenced.  
  
Ldz : Integer [in]  
> The leading dimension of the array Z.  LDZ >= 1, and if  
> JOBZ = 'V', LDZ >= N.  
  
Work : Complex Array, Dimension (max(1,lwork)) [out]  
> On exit, if INFO=0, WORK(1) returns the optimal LWORK.  
  
Lwork : Integer [in]  
> The dimension of the array WORK.  
> If N <= 1,               LWORK >= 1.  
> If JOBZ = 'N' and N > 1, LWORK >= N.  
> If LWORK = -1, then a workspace query is assumed; the routine  
> only calculates the optimal sizes of the WORK, RWORK and  
> IWORK arrays, returns these values as the first entries of  
> the WORK, RWORK and IWORK arrays, and no error message  
> related to LWORK or LRWORK or LIWORK is issued by XERBLA.  
  
Rwork : Real Array, Dimension (max(1,lrwork)) [out]  
> On exit, if INFO=0, RWORK(1) returns the optimal LRWORK.  
  
Lrwork : Integer [in]  
> The dimension of array RWORK.  
> If N <= 1,               LRWORK >= 1.  
> If JOBZ = 'N' and N > 1, LRWORK >= N.  
> If LRWORK = -1, then a workspace query is assumed; the  
> routine only calculates the optimal sizes of the WORK, RWORK  
> and IWORK arrays, returns these values as the first entries  
> of the WORK, RWORK and IWORK arrays, and no error message  
> related to LWORK or LRWORK or LIWORK is issued by XERBLA.  
  
Iwork : Integer Array, Dimension (max(1,liwork)) [out]  
> On exit, if INFO=0, IWORK(1) returns the optimal LIWORK.  
  
Liwork : Integer [in]  
> The dimension of array IWORK.  
> If JOBZ = 'N' or N <= 1, LIWORK >= 1.  
> If LIWORK = -1, then a workspace query is assumed; the  
> routine only calculates the optimal sizes of the WORK, RWORK  
> and IWORK arrays, returns these values as the first entries  
> of the WORK, RWORK and IWORK arrays, and no error message  
> related to LWORK or LRWORK or LIWORK is issued by XERBLA.  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
> > 0:  if INFO = i, and i is:  
> <= N:  the algorithm failed to converge:  
> i off-diagonal elements of an intermediate  
> tridiagonal form did not converge to zero;  
> > N:   if INFO = N + i, for 1 <= i <= N, then CPBSTF  
> returned INFO = i: B is not positive definite.  
> The factorization of B could not be completed and  
> no eigenvalues or eigenvectors were computed.  
  
