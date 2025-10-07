```fortran  
subroutine sgemlqt (  
side,  
trans,  
m,  
n,  
k,  
mb,  
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
  
SGEMLQT overwrites the general real M-by-N matrix C with  
  
SIDE = 'L'     SIDE = 'R'  
TRANS = 'N':      Q C            C Q  
TRANS = 'T':   Q**T C            C Q**T  
  
where Q is a real orthogonal matrix defined as the product of K  
elementary reflectors:  
  
Q = H(1) H(2) . . . H(K) = I - V T V**T  
  
generated using the compact WY representation as returned by SGELQT.  
  
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
  
Mb : Integer [in]  
> The block size used for the storage of T.  K >= MB >= 1.  
> This must be the same value of MB used to generate T  
> in SGELQT.  
  
V : Real Array, Dimension [in]  
> (LDV,M) if SIDE = 'L',  
> (LDV,N) if SIDE = 'R'  
> The i-th row must contain the vector which defines the  
> elementary reflector H(i), for i = 1,2,...,k, as returned by  
> SGELQT in the first K rows of its array argument A.  
  
Ldv : Integer [in]  
> The leading dimension of the array V. LDV >= max(1,K).  
  
T : Real Array, Dimension (ldt,k) [in]  
> The upper triangular factors of the block reflectors  
> as returned by SGELQT, stored as a MB-by-K matrix.  
  
Ldt : Integer [in]  
> The leading dimension of the array T.  LDT >= MB.  
  
C : Real Array, Dimension (ldc,n) [in,out]  
> On entry, the M-by-N matrix C.  
  
Ldc : Integer [in]  
> The leading dimension of the array C. LDC >= max(1,M).  
  
Work : Real Array. The Dimension of [out]  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
  
