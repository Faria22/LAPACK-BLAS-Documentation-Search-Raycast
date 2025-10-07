```fortran  
subroutine dgesvd (  
jobu,  
jobvt,  
m,  
n,  
a,  
lda,  
s,  
u,  
ldu,  
vt,  
ldvt,  
*                          work,  
lwork,  
info  
)  
```  
  
DGESVD computes the singular value decomposition (SVD) of a real  
M-by-N matrix A, optionally computing the left and/or right singular  
vectors. The SVD is written  
  
A = U * SIGMA * transpose(V)  
  
where SIGMA is an M-by-N matrix which is zero except for its  
min(m,n) diagonal elements, U is an M-by-M orthogonal matrix, and  
V is an N-by-N orthogonal matrix.  The diagonal elements of SIGMA  
are the singular values of A; they are real and non-negative, and  
are returned in descending order.  The first min(m,n) columns of  
U and V are the left and right singular vectors of A.  
  
Note that the routine returns V**T, not V.  
  
## Parameters  
Jobu : Character*1 [in]  
> Specifies options for computing all or part of the matrix U:  
> = 'A':  all M columns of U are returned in array U:  
> = 'S':  the first min(m,n) columns of U (the left singular  
> vectors) are returned in the array U;  
> = 'O':  the first min(m,n) columns of U (the left singular  
> vectors) are overwritten on the array A;  
> = 'N':  no columns of U (no left singular vectors) are  
> computed.  
  
Jobvt : Character*1 [in]  
> Specifies options for computing all or part of the matrix  
> vectors) are returned in the array VT;  
> vectors) are overwritten on the array A;  
> computed.  
> JOBVT and JOBU cannot both be 'O'.  
  
M : Integer [in]  
> The number of rows of the input matrix A.  M >= 0.  
  
N : Integer [in]  
> The number of columns of the input matrix A.  N >= 0.  
  
A : Double Precision Array, Dimension (lda,n) [in,out]  
> On entry, the M-by-N matrix A.  
> On exit,  
> if JOBU = 'O',  A is overwritten with the first min(m,n)  
> columns of U (the left singular vectors,  
> stored columnwise);  
> if JOBVT = 'O', A is overwritten with the first min(m,n)  
> stored rowwise);  
> if JOBU .ne. 'O' and JOBVT .ne. 'O', the contents of A  
> are destroyed.  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,M).  
  
S : Double Precision Array, Dimension (min(m,n)) [out]  
> The singular values of A, sorted so that S(i) >= S(i+1).  
  
U : Double Precision Array, Dimension (ldu,ucol) [out]  
> (LDU,M) if JOBU = 'A' or (LDU,min(M,N)) if JOBU = 'S'.  
> If JOBU = 'A', U contains the M-by-M orthogonal matrix U;  
> if JOBU = 'S', U contains the first min(m,n) columns of U  
> (the left singular vectors, stored columnwise);  
> if JOBU = 'N' or 'O', U is not referenced.  
  
Ldu : Integer [in]  
> The leading dimension of the array U.  LDU >= 1; if  
> JOBU = 'S' or 'A', LDU >= M.  
  
Vt : Double Precision Array, Dimension (ldvt,n) [out]  
> If JOBVT = 'A', VT contains the N-by-N orthogonal matrix  
> if JOBVT = 'S', VT contains the first min(m,n) rows of  
> if JOBVT = 'N' or 'O', VT is not referenced.  
  
Ldvt : Integer [in]  
> The leading dimension of the array VT.  LDVT >= 1; if  
> JOBVT = 'A', LDVT >= N; if JOBVT = 'S', LDVT >= min(M,N).  
  
Work : Double Precision Array, Dimension (max(1,lwork)) [out]  
> On exit, if INFO = 0, WORK(1) returns the optimal LWORK;  
> if INFO > 0, WORK(2:MIN(M,N)) contains the unconverged  
> superdiagonal elements of an upper bidiagonal matrix B  
> whose diagonal is in S (not necessarily sorted). B  
> as A, and singular vectors related by U and VT.  
  
Lwork : Integer [in]  
> The dimension of the array WORK.  
> - PATH 1  (M much larger than N, JOBU='N')  
> - PATH 1t (N much larger than M, JOBVT='N')  
> For good performance, LWORK should generally be larger.  
> If LWORK = -1, then a workspace query is assumed; the routine  
> only calculates the optimal size of the WORK array, returns  
> this value as the first entry of the WORK array, and no error  
> message related to LWORK is issued by XERBLA.  
  
Info : Integer [out]  
> = 0:  successful exit.  
> < 0:  if INFO = -i, the i-th argument had an illegal value.  
> > 0:  if DBDSQR did not converge, INFO specifies how many  
> superdiagonals of an intermediate bidiagonal form B  
> did not converge to zero. See the description of WORK  
> above for details.  
  
