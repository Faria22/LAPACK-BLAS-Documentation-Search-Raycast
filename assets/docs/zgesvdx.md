```fortran  
subroutine zgesvdx (  
jobu,  
jobvt,  
range,  
m,  
n,  
a,  
lda,  
vl,  
vu,  
*    $                    il,  
iu,  
ns,  
s,  
u,  
ldu,  
vt,  
ldvt,  
work,  
*    $                    lwork,  
rwork,  
iwork,  
info  
)  
```  
  
ZGESVDX computes the singular value decomposition (SVD) of a complex  
M-by-N matrix A, optionally computing the left and/or right singular  
vectors. The SVD is written  
  
A = U * SIGMA * transpose(V)  
  
where SIGMA is an M-by-N matrix which is zero except for its  
min(m,n) diagonal elements, U is an M-by-M unitary matrix, and  
V is an N-by-N unitary matrix.  The diagonal elements of SIGMA  
are the singular values of A; they are real and non-negative, and  
are returned in descending order.  The first min(m,n) columns of  
U and V are the left and right singular vectors of A.  
  
ZGESVDX uses an eigenvalue problem for obtaining the SVD, which  
allows for the computation of a subset of singular values and  
vectors. See DBDSVDX for details.  
  
Note that the routine returns V**T, not V.  
  
## Parameters  
Jobu : Character*1 [in]  
> Specifies options for computing all or part of the matrix U:  
> = 'V':  the first min(m,n) columns of U (the left singular  
> vectors) or as specified by RANGE are returned in  
> the array U;  
> = 'N':  no columns of U (no left singular vectors) are  
> computed.  
  
Jobvt : Character*1 [in]  
> Specifies options for computing all or part of the matrix  
> vectors) or as specified by RANGE are returned in  
> the array VT;  
> computed.  
  
Range : Character*1 [in]  
> = 'A': all singular values will be found.  
> = 'V': all singular values in the half-open interval (VL,VU]  
> will be found.  
> = 'I': the IL-th through IU-th singular values will be found.  
  
M : Integer [in]  
> The number of rows of the input matrix A.  M >= 0.  
  
N : Integer [in]  
> The number of columns of the input matrix A.  N >= 0.  
  
A : Complex*16 Array, Dimension (lda,n) [in,out]  
> On entry, the M-by-N matrix A.  
> On exit, the contents of A are destroyed.  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,M).  
  
Vl : Double Precision [in]  
> If RANGE='V', the lower bound of the interval to  
> be searched for singular values. VU > VL.  
> Not referenced if RANGE = 'A' or 'I'.  
  
Vu : Double Precision [in]  
> If RANGE='V', the upper bound of the interval to  
> be searched for singular values. VU > VL.  
> Not referenced if RANGE = 'A' or 'I'.  
  
Il : Integer [in]  
> If RANGE='I', the index of the  
> smallest singular value to be returned.  
> 1 <= IL <= IU <= min(M,N), if min(M,N) > 0.  
> Not referenced if RANGE = 'A' or 'V'.  
  
Iu : Integer [in]  
> If RANGE='I', the index of the  
> largest singular value to be returned.  
> 1 <= IL <= IU <= min(M,N), if min(M,N) > 0.  
> Not referenced if RANGE = 'A' or 'V'.  
  
Ns : Integer [out]  
> The total number of singular values found,  
> 0 <= NS <= min(M,N).  
> If RANGE = 'A', NS = min(M,N); if RANGE = 'I', NS = IU-IL+1.  
  
S : Double Precision Array, Dimension (min(m,n)) [out]  
> The singular values of A, sorted so that S(i) >= S(i+1).  
  
U : Complex*16 Array, Dimension (ldu,ucol) [out]  
> If JOBU = 'V', U contains columns of U (the left singular  
> vectors, stored columnwise) as specified by RANGE; if  
> JOBU = 'N', U is not referenced.  
> Note: The user must ensure that UCOL >= NS; if RANGE = 'V',  
> the exact value of NS is not known in advance and an upper  
> bound must be used.  
  
Ldu : Integer [in]  
> The leading dimension of the array U.  LDU >= 1; if  
> JOBU = 'V', LDU >= M.  
  
Vt : Complex*16 Array, Dimension (ldvt,n) [out]  
> vectors, stored rowwise) as specified by RANGE; if JOBVT = 'N',  
> VT is not referenced.  
> Note: The user must ensure that LDVT >= NS; if RANGE = 'V',  
> the exact value of NS is not known in advance and an upper  
> bound must be used.  
  
Ldvt : Integer [in]  
> The leading dimension of the array VT.  LDVT >= 1; if  
> JOBVT = 'V', LDVT >= NS (see above).  
  
Work : Complex*16 Array, Dimension (max(1,lwork)) [out]  
> On exit, if INFO = 0, WORK(1) returns the optimal LWORK;  
  
Lwork : Integer [in]  
> The dimension of the array WORK.  
> comments inside the code):  
> - PATH 1  (M much larger than N)  
> - PATH 1t (N much larger than M)  
> For good performance, LWORK should generally be larger.  
> If LWORK = -1, then a workspace query is assumed; the routine  
> only calculates the optimal size of the WORK array, returns  
> this value as the first entry of the WORK array, and no error  
> message related to LWORK is issued by XERBLA.  
  
Rwork : Double Precision Array, Dimension (max(1,lrwork)) [out]  
  
Iwork : Integer Array, Dimension (12*min(m,n)) [out]  
> If INFO = 0, the first NS elements of IWORK are zero. If INFO > 0,  
> then IWORK contains the indices of the eigenvectors that failed  
> to converge in DBDSVDX/DSTEVX.  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
> > 0:  if INFO = i, then i eigenvectors failed to converge  
> in DBDSVDX/DSTEVX.  
> DBDSVDX  
  
