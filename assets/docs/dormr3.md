```fortran  
subroutine dormr3 (  
side,  
trans,  
m,  
n,  
k,  
l,  
a,  
lda,  
tau,  
c,  
ldc,  
*                          work,  
info  
)  
```  
  
DORMR3 overwrites the general real m by n matrix C with  
  
Q * C  if SIDE = 'L' and TRANS = 'N', or  
  
Q**T* C  if SIDE = 'L' and TRANS = 'C', or  
  
C * Q  if SIDE = 'R' and TRANS = 'N', or  
  
C * Q**T if SIDE = 'R' and TRANS = 'C',  
  
where Q is a real orthogonal matrix defined as the product of k  
elementary reflectors  
  
Q = H(1) H(2) . . . H(k)  
  
as returned by DTZRZF. Q is of order m if SIDE = 'L' and of order n  
if SIDE = 'R'.  
  
## Parameters  
Side : Character*1 [in]  
  
Trans : Character*1 [in]  
> = 'N': apply Q  (No transpose)  
  
M : Integer [in]  
> The number of rows of the matrix C. M >= 0.  
  
N : Integer [in]  
> The number of columns of the matrix C. N >= 0.  
  
K : Integer [in]  
> The number of elementary reflectors whose product defines  
> the matrix Q.  
> If SIDE = 'L', M >= K >= 0;  
> if SIDE = 'R', N >= K >= 0.  
  
L : Integer [in]  
> The number of columns of the matrix A containing  
> the meaningful part of the Householder reflectors.  
> If SIDE = 'L', M >= L >= 0, if SIDE = 'R', N >= L >= 0.  
  
A : Double Precision Array, Dimension [in]  
> (LDA,M) if SIDE = 'L',  
> (LDA,N) if SIDE = 'R'  
> The i-th row must contain the vector which defines the  
> elementary reflector H(i), for i = 1,2,...,k, as returned by  
> DTZRZF in the last k rows of its array argument A.  
> A is modified by the routine but restored on exit.  
  
Lda : Integer [in]  
> The leading dimension of the array A. LDA >= max(1,K).  
  
Tau : Double Precision Array, Dimension (k) [in]  
> TAU(i) must contain the scalar factor of the elementary  
> reflector H(i), as returned by DTZRZF.  
  
C : Double Precision Array, Dimension (ldc,n) [in,out]  
> On entry, the m-by-n matrix C.  
  
Ldc : Integer [in]  
> The leading dimension of the array C. LDC >= max(1,M).  
  
Work : Double Precision Array, Dimension [out]  
> (N) if SIDE = 'L',  
> (M) if SIDE = 'R'  
  
Info : Integer [out]  
> = 0: successful exit  
> < 0: if INFO = -i, the i-th argument had an illegal value  
  
