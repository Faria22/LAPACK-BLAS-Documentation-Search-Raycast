```fortran  
subroutine dlaed0 (  
icompq,  
qsiz,  
n,  
d,  
e,  
q,  
ldq,  
qstore,  
ldqs,  
*                          work,  
iwork,  
info  
)  
```  
  
DLAED0 computes all eigenvalues and corresponding eigenvectors of a  
symmetric tridiagonal matrix using the divide and conquer method.  
  
## Parameters  
Icompq : Integer [in]  
> = 0:  Compute eigenvalues only.  
> = 1:  Compute eigenvectors of original dense symmetric matrix  
> also.  On entry, Q contains the orthogonal matrix used  
> to reduce the original matrix to tridiagonal form.  
> = 2:  Compute eigenvalues and eigenvectors of tridiagonal  
> matrix.  
  
Qsiz : Integer [in]  
> The dimension of the orthogonal matrix used to reduce  
> the full matrix to tridiagonal form.  QSIZ >= N if ICOMPQ = 1.  
  
N : Integer [in]  
> The dimension of the symmetric tridiagonal matrix.  N >= 0.  
  
D : Double Precision Array, Dimension (n) [in,out]  
> On entry, the main diagonal of the tridiagonal matrix.  
> On exit, its eigenvalues.  
  
E : Double Precision Array, Dimension (n-1) [in]  
> The off-diagonal elements of the tridiagonal matrix.  
> On exit, E has been destroyed.  
  
Q : Double Precision Array, Dimension (ldq, N) [in,out]  
> On entry, Q must contain an N-by-N orthogonal matrix.  
> If ICOMPQ = 0    Q is not referenced.  
> If ICOMPQ = 1    On entry, Q is a subset of the columns of the  
> orthogonal matrix used to reduce the full  
> matrix to tridiagonal form corresponding to  
> the subset of the full matrix which is being  
> decomposed at this time.  
> If ICOMPQ = 2    On entry, Q will be the identity matrix.  
> On exit, Q contains the eigenvectors of the  
> tridiagonal matrix.  
  
Ldq : Integer [in]  
> The leading dimension of the array Q.  If eigenvectors are  
> desired, then  LDQ >= max(1,N).  In any case,  LDQ >= 1.  
  
Qstore : Double Precision Array, Dimension (ldqs, N) [out]  
> Referenced only when ICOMPQ = 1.  Used to store parts of  
> the eigenvector matrix when the updating matrix multiplies  
> take place.  
  
Ldqs : Integer [in]  
> The leading dimension of the array QSTORE.  If ICOMPQ = 1,  
> then  LDQS >= max(1,N).  In any case,  LDQS >= 1.  
  
Work : Double Precision Array, [out]  
> If ICOMPQ = 0 or 1, the dimension of WORK must be at least  
> ( lg( N ) = smallest integer k  
> such that 2^k >= N )  
> If ICOMPQ = 2, the dimension of WORK must be at least  
  
Iwork : Integer Array, [out]  
> If ICOMPQ = 0 or 1, the dimension of IWORK must be at least  
> ( lg( N ) = smallest integer k  
> such that 2^k >= N )  
> If ICOMPQ = 2, the dimension of IWORK must be at least  
  
Info : Integer [out]  
> = 0:  successful exit.  
> < 0:  if INFO = -i, the i-th argument had an illegal value.  
> > 0:  The algorithm failed to compute an eigenvalue while  
> working on the submatrix lying in rows and columns  
> INFO/(N+1) through mod(INFO,N+1).  
  
