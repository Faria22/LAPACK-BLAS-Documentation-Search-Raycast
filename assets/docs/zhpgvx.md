```fortran  
subroutine zhpgvx (  
itype,  
jobz,  
range,  
uplo,  
n,  
ap,  
bp,  
vl,  
vu,  
*                          il,  
iu,  
abstol,  
m,  
w,  
z,  
ldz,  
work,  
rwork,  
*                          iwork,  
ifail,  
info  
)  
```  
  
ZHPGVX computes selected eigenvalues and, optionally, eigenvectors  
of a complex generalized Hermitian-definite eigenproblem, of the form  
A*x=(lambda)*B*x,  A*Bx=(lambda)*x,  or B*A*x=(lambda)*x.  Here A and  
B are assumed to be Hermitian, stored in packed format, and B is also  
positive definite.  Eigenvalues and eigenvectors can be selected by  
specifying either a range of values or a range of indices for the  
desired eigenvalues.  
  
## Parameters  
Itype : Integer [in]  
> Specifies the problem type to be solved:  
  
Jobz : Character*1 [in]  
> = 'N':  Compute eigenvalues only;  
> = 'V':  Compute eigenvalues and eigenvectors.  
  
Range : Character*1 [in]  
> = 'A': all eigenvalues will be found;  
> = 'V': all eigenvalues in the half-open interval (VL,VU]  
> will be found;  
> = 'I': the IL-th through IU-th eigenvalues will be found.  
  
Uplo : Character*1 [in]  
> = 'U':  Upper triangles of A and B are stored;  
> = 'L':  Lower triangles of A and B are stored.  
  
N : Integer [in]  
> The order of the matrices A and B.  N >= 0.  
  
Ap : Complex*16 Array, Dimension (n*(n+1)/2) [in,out]  
> On entry, the upper or lower triangle of the Hermitian matrix  
> A, packed columnwise in a linear array.  The j-th column of A  
> is stored in the array AP as follows:  
> On exit, the contents of AP are destroyed.  
  
Bp : Complex*16 Array, Dimension (n*(n+1)/2) [in,out]  
> On entry, the upper or lower triangle of the Hermitian matrix  
> B, packed columnwise in a linear array.  The j-th column of B  
> is stored in the array BP as follows:  
> On exit, the triangular factor U or L from the Cholesky  
> format as B.  
  
Vl : Double Precision [in]  
> If RANGE='V', the lower bound of the interval to  
> be searched for eigenvalues. VL < VU.  
> Not referenced if RANGE = 'A' or 'I'.  
  
Vu : Double Precision [in]  
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
  
Abstol : Double Precision [in]  
> The absolute error tolerance for the eigenvalues.  
> An approximate eigenvalue is accepted as converged  
> when it is determined to lie in an interval [a,b]  
> of width less than or equal to  
> where EPS is the machine precision.  If ABSTOL is less than  
> where |T| is the 1-norm of the tridiagonal matrix obtained  
> by reducing AP to tridiagonal form.  
> Eigenvalues will be computed most accurately when ABSTOL is  
> If this routine returns with INFO>0, indicating that some  
> eigenvectors did not converge, try setting ABSTOL to  
  
M : Integer [out]  
> The total number of eigenvalues found.  0 <= M <= N.  
> If RANGE = 'A', M = N, and if RANGE = 'I', M = IU-IL+1.  
  
W : Double Precision Array, Dimension (n) [out]  
> On normal exit, the first M elements contain the selected  
> eigenvalues in ascending order.  
  
Z : Complex*16 Array, Dimension (ldz, N) [out]  
> If JOBZ = 'N', then Z is not referenced.  
> If JOBZ = 'V', then if INFO = 0, the first M columns of Z  
> contain the orthonormal eigenvectors of the matrix A  
> corresponding to the selected eigenvalues, with the i-th  
> column of Z holding the eigenvector associated with W(i).  
> The eigenvectors are normalized as follows:  
> If an eigenvector fails to converge, then that column of Z  
> contains the latest approximation to the eigenvector, and the  
> index of the eigenvector is returned in IFAIL.  
> Note: the user must ensure that at least max(1,M) columns are  
> supplied in the array Z; if RANGE = 'V', the exact value of M  
> is not known in advance and an upper bound must be used.  
  
Ldz : Integer [in]  
> The leading dimension of the array Z.  LDZ >= 1, and if  
> JOBZ = 'V', LDZ >= max(1,N).  
  
Work : Complex*16 Array, Dimension (2*n) [out]  
  
Rwork : Double Precision Array, Dimension (7*n) [out]  
  
Iwork : Integer Array, Dimension (5*n) [out]  
  
Ifail : Integer Array, Dimension (n) [out]  
> If JOBZ = 'V', then if INFO = 0, the first M elements of  
> IFAIL are zero.  If INFO > 0, then IFAIL contains the  
> indices of the eigenvectors that failed to converge.  
> If JOBZ = 'N', then IFAIL is not referenced.  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
> > 0:  ZPPTRF or ZHPEVX returned an error code:  
> <= N:  if INFO = i, ZHPEVX failed to converge;  
> i eigenvectors failed to converge.  Their indices  
> are stored in array IFAIL.  
> > N:   if INFO = N + i, for 1 <= i <= n, then the leading  
> principal minor of order i of B is not positive.  
> The factorization of B could not be completed and  
> no eigenvalues or eigenvectors were computed.  
  
