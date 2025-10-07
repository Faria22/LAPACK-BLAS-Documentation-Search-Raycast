```fortran  
subroutine cstegr (  
jobz,  
range,  
n,  
d,  
e,  
vl,  
vu,  
il,  
iu,  
*                  abstol,  
m,  
w,  
z,  
ldz,  
isuppz,  
work,  
lwork,  
iwork,  
*                  liwork,  
info  
)  
```  
  
CSTEGR computes selected eigenvalues and, optionally, eigenvectors  
of a real symmetric tridiagonal matrix T. Any such unreduced matrix has  
a well defined set of pairwise different real eigenvalues, the corresponding  
real eigenvectors are pairwise orthogonal.  
  
The spectrum may be computed either completely or partially by specifying  
either an interval (VL,VU] or a range of indices IL:IU for the desired  
eigenvalues.  
  
CSTEGR is a compatibility wrapper around the improved CSTEMR routine.  
See SSTEMR for further details.  
  
One important change is that the ABSTOL parameter no longer provides any  
benefit and hence is no longer used.  
  
Note : CSTEGR and CSTEMR work only on machines which follow  
IEEE-754 floating-point standard in their handling of infinities and  
NaNs.  Normal execution may create these exceptional values and hence  
may abort due to a floating point exception in environments which  
do not conform to the IEEE-754 standard.  
  
## Parameters  
Jobz : Character*1 [in]  
> = 'N':  Compute eigenvalues only;  
> = 'V':  Compute eigenvalues and eigenvectors.  
  
Range : Character*1 [in]  
> = 'A': all eigenvalues will be found.  
> = 'V': all eigenvalues in the half-open interval (VL,VU]  
> will be found.  
> = 'I': the IL-th through IU-th eigenvalues will be found.  
  
N : Integer [in]  
> The order of the matrix.  N >= 0.  
  
D : Real Array, Dimension (n) [in,out]  
> On entry, the N diagonal elements of the tridiagonal matrix  
> T. On exit, D is overwritten.  
  
E : Real Array, Dimension (n) [in,out]  
> On entry, the (N-1) subdiagonal elements of the tridiagonal  
> matrix T in elements 1 to N-1 of E. E(N) need not be set on  
> input, but is used internally as workspace.  
> On exit, E is overwritten.  
  
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
> 1 <= IL <= IU <= N, if N > 0.  
> Not referenced if RANGE = 'A' or 'V'.  
  
Iu : Integer [in]  
> If RANGE='I', the index of the  
> largest eigenvalue to be returned.  
> 1 <= IL <= IU <= N, if N > 0.  
> Not referenced if RANGE = 'A' or 'V'.  
  
Abstol : Real [in]  
> Unused.  Was the absolute error tolerance for the  
> eigenvalues/eigenvectors in previous versions.  
  
M : Integer [out]  
> The total number of eigenvalues found.  0 <= M <= N.  
> If RANGE = 'A', M = N, and if RANGE = 'I', M = IU-IL+1.  
  
W : Real Array, Dimension (n) [out]  
> The first M elements contain the selected eigenvalues in  
> ascending order.  
  
Z : Complex Array, Dimension (ldz, Max(1,m) ) [out]  
> If JOBZ = 'V', and if INFO = 0, then the first M columns of Z  
> contain the orthonormal eigenvectors of the matrix T  
> corresponding to the selected eigenvalues, with the i-th  
> column of Z holding the eigenvector associated with W(i).  
> If JOBZ = 'N', then Z is not referenced.  
> Note: the user must ensure that at least max(1,M) columns are  
> supplied in the array Z; if RANGE = 'V', the exact value of M  
> is not known in advance and an upper bound must be used.  
> Supplying N columns is always safe.  
  
Ldz : Integer [in]  
> The leading dimension of the array Z.  LDZ >= 1, and if  
> JOBZ = 'V', then LDZ >= max(1,N).  
  
Isuppz : Integer Array, Dimension ( 2*max(1,m) ) [out]  
> The support of the eigenvectors in Z, i.e., the indices  
> indicating the nonzero elements in Z. The i-th computed eigenvector  
> is split. ISUPPZ is only accessed when JOBZ is 'V' and N > 0.  
  
Work : Real Array, Dimension (lwork) [out]  
> On exit, if INFO = 0, WORK(1) returns the optimal  
> (and minimal) LWORK.  
  
Lwork : Integer [in]  
> If LWORK = -1, then a workspace query is assumed; the routine  
> only calculates the optimal size of the WORK array, returns  
> this value as the first entry of the WORK array, and no error  
> message related to LWORK is issued by XERBLA.  
  
Iwork : Integer Array, Dimension (liwork) [out]  
> On exit, if INFO = 0, IWORK(1) returns the optimal LIWORK.  
  
Liwork : Integer [in]  
> if only the eigenvalues are to be computed.  
> If LIWORK = -1, then a workspace query is assumed; the  
> routine only calculates the optimal size of the IWORK array,  
> returns this value as the first entry of the IWORK array, and  
> no error message related to LIWORK is issued by XERBLA.  
  
Info : Integer [out]  
> On exit, INFO  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
> > 0:  if INFO = 1X, internal error in SLARRE,  
> if INFO = 2X, internal error in CLARRV.  
> Here, the digit X = ABS( IINFO ) < 10, where IINFO is  
> the nonzero error code returned by SLARRE or  
> CLARRV, respectively.  
  
