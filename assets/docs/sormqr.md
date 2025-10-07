```fortran  
subroutine sormqr (  
side,  
trans,  
m,  
n,  
k,  
a,  
lda,  
tau,  
c,  
ldc,  
*                          work,  
lwork,  
info  
)  
```  
  
SORMQR overwrites the general real M-by-N matrix C with  
  
SIDE = 'L'     SIDE = 'R'  
TRANS = 'N':      Q * C          C * Q  
TRANS = 'T':      Q**T * C       C * Q**T  
  
where Q is a real orthogonal matrix defined as the product of k  
elementary reflectors  
  
Q = H(1) H(2) . . . H(k)  
  
as returned by SGEQRF. Q is of order M if SIDE = 'L' and of order N  
if SIDE = 'R'.  
  
## Parameters  
Side : Character*1 [in]  
  
Trans : Character*1 [in]  
> = 'N':  No transpose, apply Q;  
  
M : Integer [in]  
> The number of rows of the matrix C. M >= 0.  
  
N : Integer [in]  
> The number of columns of the matrix C. N >= 0.  
  
K : Integer [in]  
> The number of elementary reflectors whose product defines  
> the matrix Q.  
> If SIDE = 'L', M >= K >= 0;  
> if SIDE = 'R', N >= K >= 0.  
  
A : Real Array, Dimension (lda,k) [in]  
> The i-th column must contain the vector which defines the  
> elementary reflector H(i), for i = 1,2,...,k, as returned by  
> SGEQRF in the first k columns of its array argument A.  
  
Lda : Integer [in]  
> The leading dimension of the array A.  
> If SIDE = 'L', LDA >= max(1,M);  
> if SIDE = 'R', LDA >= max(1,N).  
  
Tau : Real Array, Dimension (k) [in]  
> TAU(i) must contain the scalar factor of the elementary  
> reflector H(i), as returned by SGEQRF.  
  
C : Real Array, Dimension (ldc,n) [in,out]  
> On entry, the M-by-N matrix C.  
  
Ldc : Integer [in]  
> The leading dimension of the array C. LDC >= max(1,M).  
  
Work : Real Array, Dimension (max(1,lwork)) [out]  
> On exit, if INFO = 0, WORK(1) returns the optimal LWORK.  
  
Lwork : Integer [in]  
> The dimension of the array WORK.  
> If SIDE = 'L', LWORK >= max(1,N);  
> if SIDE = 'R', LWORK >= max(1,M).  
> For good performance, LWORK should generally be larger.  
> If LWORK = -1, then a workspace query is assumed; the routine  
> only calculates the optimal size of the WORK array, returns  
> this value as the first entry of the WORK array, and no error  
> message related to LWORK is issued by XERBLA.  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
  
