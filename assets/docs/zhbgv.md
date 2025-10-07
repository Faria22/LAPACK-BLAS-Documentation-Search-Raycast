```fortran  
subroutine zhbgv (  
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
z,  
*                         ldz,  
work,  
rwork,  
info  
)  
```  
  
ZHBGV computes all the eigenvalues, and optionally, the eigenvectors  
of a complex generalized Hermitian-definite banded eigenproblem, of  
the form A*x=(lambda)*B*x. Here A and B are assumed to be Hermitian  
and banded, and B is also positive definite.  
  
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
  
Ab : Complex*16 Array, Dimension (ldab, N) [in,out]  
> On entry, the upper or lower triangle of the Hermitian band  
> matrix A, stored in the first ka+1 rows of the array.  The  
> j-th column of A is stored in the j-th column of the array AB  
> as follows:  
> if UPLO = 'U', AB(ka+1+i-j,j) = A(i,j) for max(1,j-ka)<=i<=j;  
> if UPLO = 'L', AB(1+i-j,j)    = A(i,j) for j<=i<=min(n,j+ka).  
> On exit, the contents of AB are destroyed.  
  
Ldab : Integer [in]  
> The leading dimension of the array AB.  LDAB >= KA+1.  
  
Bb : Complex*16 Array, Dimension (ldbb, N) [in,out]  
> On entry, the upper or lower triangle of the Hermitian band  
> matrix B, stored in the first kb+1 rows of the array.  The  
> j-th column of B is stored in the j-th column of the array BB  
> as follows:  
> if UPLO = 'U', BB(kb+1+i-j,j) = B(i,j) for max(1,j-kb)<=i<=j;  
> if UPLO = 'L', BB(1+i-j,j)    = B(i,j) for j<=i<=min(n,j+kb).  
> On exit, the factor S from the split Cholesky factorization  
  
Ldbb : Integer [in]  
> The leading dimension of the array BB.  LDBB >= KB+1.  
  
W : Double Precision Array, Dimension (n) [out]  
> If INFO = 0, the eigenvalues in ascending order.  
  
Z : Complex*16 Array, Dimension (ldz, N) [out]  
> If JOBZ = 'V', then if INFO = 0, Z contains the matrix Z of  
> eigenvectors, with the i-th column of Z holding the  
> eigenvector associated with W(i). The eigenvectors are  
> If JOBZ = 'N', then Z is not referenced.  
  
Ldz : Integer [in]  
> The leading dimension of the array Z.  LDZ >= 1, and if  
> JOBZ = 'V', LDZ >= N.  
  
Work : Complex*16 Array, Dimension (n) [out]  
  
Rwork : Double Precision Array, Dimension (3*n) [out]  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
> > 0:  if INFO = i, and i is:  
> <= N:  the algorithm failed to converge:  
> i off-diagonal elements of an intermediate  
> tridiagonal form did not converge to zero;  
> > N:   if INFO = N + i, for 1 <= i <= N, then ZPBSTF  
> returned INFO = i: B is not positive definite.  
> The factorization of B could not be completed and  
> no eigenvalues or eigenvectors were computed.  
  
