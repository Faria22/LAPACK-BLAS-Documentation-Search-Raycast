```fortran  
subroutine dggsvp3 (  
jobu,  
jobv,  
jobq,  
m,  
p,  
n,  
a,  
lda,  
b,  
ldb,  
*                           tola,  
tolb,  
k,  
l,  
u,  
ldu,  
v,  
ldv,  
q,  
ldq,  
*                           iwork,  
tau,  
work,  
lwork,  
info  
)  
```  
  
DGGSVP3 computes orthogonal matrices U, V and Q such that  
  
N-K-L  K    L  
U**T*A*Q =     K ( 0    A12  A13 )  if M-K-L >= 0;  
L ( 0     0   A23 )  
M-K-L ( 0     0    0  )  
  
N-K-L  K    L  
=     K ( 0    A12  A13 )  if M-K-L < 0;  
M-K ( 0     0   A23 )  
  
N-K-L  K    L  
V**T*B*Q =   L ( 0     0   B13 )  
P-L ( 0     0    0  )  
  
where the K-by-K matrix A12 and L-by-L matrix B13 are nonsingular  
upper triangular; A23 is L-by-L upper triangular if M-K-L >= 0,  
otherwise A23 is (M-K)-by-L upper trapezoidal.  K+L = the effective  
numerical rank of the (M+P)-by-N matrix (A**T,B**T)**T.  
  
This decomposition is the preprocessing step for computing the  
Generalized Singular Value Decomposition (GSVD), see subroutine  
DGGSVD3.  
  
## Parameters  
Jobu : Character*1 [in]  
> = 'U':  Orthogonal matrix U is computed;  
> = 'N':  U is not computed.  
  
Jobv : Character*1 [in]  
> = 'V':  Orthogonal matrix V is computed;  
> = 'N':  V is not computed.  
  
Jobq : Character*1 [in]  
> = 'Q':  Orthogonal matrix Q is computed;  
> = 'N':  Q is not computed.  
  
M : Integer [in]  
> The number of rows of the matrix A.  M >= 0.  
  
P : Integer [in]  
> The number of rows of the matrix B.  P >= 0.  
  
N : Integer [in]  
> The number of columns of the matrices A and B.  N >= 0.  
  
A : Double Precision Array, Dimension (lda,n) [in,out]  
> On entry, the M-by-N matrix A.  
> On exit, A contains the triangular (or trapezoidal) matrix  
> described in the Purpose section.  
  
Lda : Integer [in]  
> The leading dimension of the array A. LDA >= max(1,M).  
  
B : Double Precision Array, Dimension (ldb,n) [in,out]  
> On entry, the P-by-N matrix B.  
> On exit, B contains the triangular matrix described in  
> the Purpose section.  
  
Ldb : Integer [in]  
> The leading dimension of the array B. LDB >= max(1,P).  
  
Tola : Double Precision [in]  
  
Tolb : Double Precision [in]  
> TOLA and TOLB are the thresholds to determine the effective  
> numerical rank of matrix B and a subblock of A. Generally,  
> they are set to  
> The size of TOLA and TOLB may affect the size of backward  
> errors of the decomposition.  
  
K : Integer [out]  
  
L : Integer [out]  
> On exit, K and L specify the dimension of the subblocks  
> described in Purpose section.  
  
U : Double Precision Array, Dimension (ldu,m) [out]  
> If JOBU = 'U', U contains the orthogonal matrix U.  
> If JOBU = 'N', U is not referenced.  
  
Ldu : Integer [in]  
> The leading dimension of the array U. LDU >= max(1,M) if  
> JOBU = 'U'; LDU >= 1 otherwise.  
  
V : Double Precision Array, Dimension (ldv,p) [out]  
> If JOBV = 'V', V contains the orthogonal matrix V.  
> If JOBV = 'N', V is not referenced.  
  
Ldv : Integer [in]  
> The leading dimension of the array V. LDV >= max(1,P) if  
> JOBV = 'V'; LDV >= 1 otherwise.  
  
Q : Double Precision Array, Dimension (ldq,n) [out]  
> If JOBQ = 'Q', Q contains the orthogonal matrix Q.  
> If JOBQ = 'N', Q is not referenced.  
  
Ldq : Integer [in]  
> The leading dimension of the array Q. LDQ >= max(1,N) if  
> JOBQ = 'Q'; LDQ >= 1 otherwise.  
  
Iwork : Integer Array, Dimension (n) [out]  
  
Tau : Double Precision Array, Dimension (n) [out]  
  
Work : Double Precision Array, Dimension (max(1,lwork)) [out]  
> On exit, if INFO = 0, WORK(1) returns the optimal LWORK.  
  
Lwork : Integer [in]  
> The dimension of the array WORK. LWORK >= 1.  
> If LWORK = -1, then a workspace query is assumed; the routine  
> only calculates the optimal size of the WORK array, returns  
> this value as the first entry of the WORK array, and no error  
> message related to LWORK is issued by XERBLA.  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value.  
  
