```fortran  
subroutine zhpev (  
jobz,  
uplo,  
n,  
ap,  
w,  
z,  
ldz,  
work,  
rwork,  
*                         info  
)  
```  
  
ZHPEV computes all the eigenvalues and, optionally, eigenvectors of a  
complex Hermitian matrix in packed storage.  
  
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
  
Work : Complex*16 Array, Dimension (max(1, 2*n-1)) [out]  
  
Rwork : Double Precision Array, Dimension (max(1, 3*n-2)) [out]  
  
Info : Integer [out]  
> = 0:  successful exit.  
> < 0:  if INFO = -i, the i-th argument had an illegal value.  
> > 0:  if INFO = i, the algorithm failed to converge; i  
> off-diagonal elements of an intermediate tridiagonal  
> form did not converge to zero.  
  
