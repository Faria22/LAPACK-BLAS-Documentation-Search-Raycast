```fortran  
subroutine sormtr (  
side,  
uplo,  
trans,  
m,  
n,  
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
  
SORMTR overwrites the general real M-by-N matrix C with  
  
SIDE = 'L'     SIDE = 'R'  
TRANS = 'N':      Q * C          C * Q  
TRANS = 'T':      Q**T * C       C * Q**T  
  
where Q is a real orthogonal matrix of order nq, with nq = m if  
SIDE = 'L' and nq = n if SIDE = 'R'. Q is defined as the product of  
nq-1 elementary reflectors, as returned by SSYTRD:  
  
if UPLO = 'U', Q = H(nq-1) . . . H(2) H(1);  
  
if UPLO = 'L', Q = H(1) H(2) . . . H(nq-1).  
  
## Parameters  
Side : Character*1 [in]  
  
Uplo : Character*1 [in]  
> = 'U': Upper triangle of A contains elementary reflectors  
> from SSYTRD;  
> = 'L': Lower triangle of A contains elementary reflectors  
> from SSYTRD.  
  
Trans : Character*1 [in]  
> = 'N':  No transpose, apply Q;  
  
M : Integer [in]  
> The number of rows of the matrix C. M >= 0.  
  
N : Integer [in]  
> The number of columns of the matrix C. N >= 0.  
  
A : Real Array, Dimension [in]  
> (LDA,M) if SIDE = 'L'  
> (LDA,N) if SIDE = 'R'  
> The vectors which define the elementary reflectors, as  
> returned by SSYTRD.  
  
Lda : Integer [in]  
> The leading dimension of the array A.  
> LDA >= max(1,M) if SIDE = 'L'; LDA >= max(1,N) if SIDE = 'R'.  
  
Tau : Real Array, Dimension [in]  
> (M-1) if SIDE = 'L'  
> (N-1) if SIDE = 'R'  
> TAU(i) must contain the scalar factor of the elementary  
> reflector H(i), as returned by SSYTRD.  
  
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
> blocksize.  
> If LWORK = -1, then a workspace query is assumed; the routine  
> only calculates the optimal size of the WORK array, returns  
> this value as the first entry of the WORK array, and no error  
> message related to LWORK is issued by XERBLA.  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
  
