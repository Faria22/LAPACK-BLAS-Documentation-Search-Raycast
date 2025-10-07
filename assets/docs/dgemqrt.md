```fortran  
subroutine dgemqrt (  
side,  
trans,  
m,  
n,  
k,  
nb,  
v,  
ldv,  
t,  
ldt,  
*                          c,  
ldc,  
work,  
info  
)  
```  
  
DGEMQRT overwrites the general real M-by-N matrix C with  
  
SIDE = 'L'     SIDE = 'R'  
TRANS = 'N':      Q C            C Q  
TRANS = 'T':   Q**T C            C Q**T  
  
where Q is a real orthogonal matrix defined as the product of K  
elementary reflectors:  
  
Q = H(1) H(2) . . . H(K) = I - V T V**T  
  
generated using the compact WY representation as returned by DGEQRT.  
  
Q is of order M if SIDE = 'L' and of order N  if SIDE = 'R'.  
  
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
  
Nb : Integer [in]  
> The block size used for the storage of T.  K >= NB >= 1.  
> This must be the same value of NB used to generate T  
> in DGEQRT.  
  
V : Double Precision Array, Dimension (ldv,k) [in]  
> The i-th column must contain the vector which defines the  
> elementary reflector H(i), for i = 1,2,...,k, as returned by  
> DGEQRT in the first K columns of its array argument A.  
  
Ldv : Integer [in]  
> The leading dimension of the array V.  
> If SIDE = 'L', LDA >= max(1,M);  
> if SIDE = 'R', LDA >= max(1,N).  
  
T : Double Precision Array, Dimension (ldt,k) [in]  
> The upper triangular factors of the block reflectors  
> as returned by DGEQRT, stored as a NB-by-N matrix.  
  
Ldt : Integer [in]  
> The leading dimension of the array T.  LDT >= NB.  
  
C : Double Precision Array, Dimension (ldc,n) [in,out]  
> On entry, the M-by-N matrix C.  
  
Ldc : Integer [in]  
> The leading dimension of the array C. LDC >= max(1,M).  
  
Work : Double Precision Array. The Dimension of [out]  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
  
