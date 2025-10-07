```fortran  
subroutine dgesdd (  
jobz,  
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
iwork,  
info  
)  
```  
  
DGESDD computes the singular value decomposition (SVD) of a real  
M-by-N matrix A, optionally computing the left and right singular  
vectors.  If singular vectors are desired, it uses a  
divide-and-conquer algorithm.  
  
The SVD is written  
  
A = U * SIGMA * transpose(V)  
  
where SIGMA is an M-by-N matrix which is zero except for its  
min(m,n) diagonal elements, U is an M-by-M orthogonal matrix, and  
V is an N-by-N orthogonal matrix.  The diagonal elements of SIGMA  
are the singular values of A; they are real and non-negative, and  
are returned in descending order.  The first min(m,n) columns of  
U and V are the left and right singular vectors of A.  
  
Note that the routine returns VT = V**T, not V.  
  
  
## Parameters  
Jobz : Character*1 [in]  
> Specifies options for computing all or part of the matrix U:  
> returned in the arrays U and VT;  
> = 'S':  the first min(M,N) columns of U and the first  
> and VT;  
> = 'O':  If M >= N, the first N columns of U are overwritten  
> the array VT;  
> otherwise, all columns of U are returned in the  
> in the array A;  
  
M : Integer [in]  
> The number of rows of the input matrix A.  M >= 0.  
  
N : Integer [in]  
> The number of columns of the input matrix A.  N >= 0.  
  
A : Double Precision Array, Dimension (lda,n) [in,out]  
> On entry, the M-by-N matrix A.  
> On exit,  
> if JOBZ = 'O',  A is overwritten with the first N columns  
> of U (the left singular vectors, stored  
> columnwise) if M >= N;  
> A is overwritten with the first M rows  
> rowwise) otherwise.  
> if JOBZ .ne. 'O', the contents of A are destroyed.  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,M).  
  
S : Double Precision Array, Dimension (min(m,n)) [out]  
> The singular values of A, sorted so that S(i) >= S(i+1).  
  
U : Double Precision Array, Dimension (ldu,ucol) [out]  
> UCOL = M if JOBZ = 'A' or JOBZ = 'O' and M < N;  
> UCOL = min(M,N) if JOBZ = 'S'.  
> If JOBZ = 'A' or JOBZ = 'O' and M < N, U contains the M-by-M  
> orthogonal matrix U;  
> if JOBZ = 'S', U contains the first min(M,N) columns of U  
> (the left singular vectors, stored columnwise);  
> if JOBZ = 'O' and M >= N, or JOBZ = 'N', U is not referenced.  
  
Ldu : Integer [in]  
> The leading dimension of the array U.  LDU >= 1; if  
> JOBZ = 'S' or 'A' or JOBZ = 'O' and M < N, LDU >= M.  
  
Vt : Double Precision Array, Dimension (ldvt,n) [out]  
> If JOBZ = 'A' or JOBZ = 'O' and M >= N, VT contains the  
> if JOBZ = 'S', VT contains the first min(M,N) rows of  
> if JOBZ = 'O' and M < N, or JOBZ = 'N', VT is not referenced.  
  
Ldvt : Integer [in]  
> The leading dimension of the array VT.  LDVT >= 1;  
> if JOBZ = 'A' or JOBZ = 'O' and M >= N, LDVT >= N;  
> if JOBZ = 'S', LDVT >= min(M,N).  
  
Work : Double Precision Array, Dimension (max(1,lwork)) [out]  
> On exit, if INFO = 0, WORK(1) returns the optimal LWORK;  
  
Lwork : Integer [in]  
> The dimension of the array WORK. LWORK >= 1.  
> If LWORK = -1, a workspace query is assumed.  The optimal  
> size for the WORK array is calculated and stored in WORK(1),  
> and no other work except argument checking is performed.  
> Let mx = max(M,N) and mn = min(M,N).  
> These are not tight minimums in all cases; see comments inside code.  
> For good performance, LWORK should generally be larger;  
> a query is recommended.  
  
Iwork : Integer Array, Dimension (8*min(m,n)) [out]  
  
Info : Integer [out]  
> <  0:  if INFO = -i, the i-th argument had an illegal value.  
> = -4:  if A had a NAN entry.  
> >  0:  DBDSDC did not converge, updating process failed.  
> =  0:  successful exit.  
  
