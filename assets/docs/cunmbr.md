```fortran  
subroutine cunmbr (  
vect,  
side,  
trans,  
m,  
n,  
k,  
a,  
lda,  
tau,  
c,  
*                          ldc,  
work,  
lwork,  
info  
)  
```  
  
If VECT = 'Q', CUNMBR overwrites the general complex M-by-N matrix C  
with  
SIDE = 'L'     SIDE = 'R'  
TRANS = 'N':      Q * C          C * Q  
TRANS = 'C':      Q**H * C       C * Q**H  
  
If VECT = 'P', CUNMBR overwrites the general complex M-by-N matrix C  
with  
SIDE = 'L'     SIDE = 'R'  
TRANS = 'N':      P * C          C * P  
TRANS = 'C':      P**H * C       C * P**H  
  
Here Q and P**H are the unitary matrices determined by CGEBRD when  
reducing a complex matrix A to bidiagonal form: A = Q * B * P**H. Q  
and P**H are defined as products of elementary reflectors H(i) and  
G(i) respectively.  
  
Let nq = m if SIDE = 'L' and nq = n if SIDE = 'R'. Thus nq is the  
order of the unitary matrix Q or P**H that is applied.  
  
If VECT = 'Q', A is assumed to have been an NQ-by-K matrix:  
if nq >= k, Q = H(1) H(2) . . . H(k);  
if nq < k, Q = H(1) H(2) . . . H(nq-1).  
  
If VECT = 'P', A is assumed to have been a K-by-NQ matrix:  
if k < nq, P = G(1) G(2) . . . G(k);  
if k >= nq, P = G(1) G(2) . . . G(nq-1).  
  
## Parameters  
Vect : Character*1 [in]  
  
Side : Character*1 [in]  
  
Trans : Character*1 [in]  
> = 'N':  No transpose, apply Q or P;  
  
M : Integer [in]  
> The number of rows of the matrix C. M >= 0.  
  
N : Integer [in]  
> The number of columns of the matrix C. N >= 0.  
  
K : Integer [in]  
> If VECT = 'Q', the number of columns in the original  
> matrix reduced by CGEBRD.  
> If VECT = 'P', the number of rows in the original  
> matrix reduced by CGEBRD.  
> K >= 0.  
  
A : Complex Array, Dimension [in]  
> (LDA,min(nq,K)) if VECT = 'Q'  
> (LDA,nq)        if VECT = 'P'  
> The vectors which define the elementary reflectors H(i) and  
> G(i), whose products determine the matrices Q and P, as  
> returned by CGEBRD.  
  
Lda : Integer [in]  
> The leading dimension of the array A.  
> If VECT = 'Q', LDA >= max(1,nq);  
> if VECT = 'P', LDA >= max(1,min(nq,K)).  
  
Tau : Complex Array, Dimension (min(nq,k)) [in]  
> TAU(i) must contain the scalar factor of the elementary  
> reflector H(i) or G(i) which determines Q or P, as returned  
> by CGEBRD in the array argument TAUQ or TAUP.  
  
C : Complex Array, Dimension (ldc,n) [in,out]  
> On entry, the M-by-N matrix C.  
  
Ldc : Integer [in]  
> The leading dimension of the array C. LDC >= max(1,M).  
  
Work : Complex Array, Dimension (max(1,lwork)) [out]  
> On exit, if INFO = 0, WORK(1) returns the optimal LWORK.  
  
Lwork : Integer [in]  
> The dimension of the array WORK.  
> If SIDE = 'L', LWORK >= max(1,N);  
> if SIDE = 'R', LWORK >= max(1,M);  
> if N = 0 or M = 0, LWORK >= 1.  
> optimal blocksize. (NB = 0 if M = 0 or N = 0.)  
> If LWORK = -1, then a workspace query is assumed; the routine  
> only calculates the optimal size of the WORK array, returns  
> this value as the first entry of the WORK array, and no error  
> message related to LWORK is issued by XERBLA.  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
  
