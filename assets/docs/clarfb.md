```fortran  
subroutine clarfb (  
side,  
trans,  
direct,  
storev,  
m,  
n,  
k,  
v,  
ldv,  
*                          t,  
ldt,  
c,  
ldc,  
work,  
ldwork  
)  
```  
  
CLARFB applies a complex block reflector H or its transpose H**H to a  
complex M-by-N matrix C, from either the left or the right.  
  
## Parameters  
Side : Character*1 [in]  
  
Trans : Character*1 [in]  
> = 'N': apply H (No transpose)  
  
Direct : Character*1 [in]  
> Indicates how H is formed from a product of elementary  
> reflectors  
> = 'F': H = H(1) H(2) . . . H(k) (Forward)  
> = 'B': H = H(k) . . . H(2) H(1) (Backward)  
  
Storev : Character*1 [in]  
> Indicates how the vectors which define the elementary  
> reflectors are stored:  
> = 'C': Columnwise  
> = 'R': Rowwise  
  
M : Integer [in]  
> The number of rows of the matrix C.  
  
N : Integer [in]  
> The number of columns of the matrix C.  
  
K : Integer [in]  
> The order of the matrix T (= the number of elementary  
> reflectors whose product defines the block reflector).  
> If SIDE = 'L', M >= K >= 0;  
> if SIDE = 'R', N >= K >= 0.  
  
V : Complex Array, Dimension [in]  
> (LDV,K) if STOREV = 'C'  
> (LDV,M) if STOREV = 'R' and SIDE = 'L'  
> (LDV,N) if STOREV = 'R' and SIDE = 'R'  
> The matrix V. See Further Details.  
  
Ldv : Integer [in]  
> The leading dimension of the array V.  
> If STOREV = 'C' and SIDE = 'L', LDV >= max(1,M);  
> if STOREV = 'C' and SIDE = 'R', LDV >= max(1,N);  
> if STOREV = 'R', LDV >= K.  
  
T : Complex Array, Dimension (ldt,k) [in]  
> The triangular K-by-K matrix T in the representation of the  
> block reflector.  
  
Ldt : Integer [in]  
> The leading dimension of the array T. LDT >= K.  
  
C : Complex Array, Dimension (ldc,n) [in,out]  
> On entry, the M-by-N matrix C.  
  
Ldc : Integer [in]  
> The leading dimension of the array C. LDC >= max(1,M).  
  
Work : Complex Array, Dimension (ldwork,k) [out]  
  
Ldwork : Integer [in]  
> The leading dimension of the array WORK.  
> If SIDE = 'L', LDWORK >= max(1,N);  
> if SIDE = 'R', LDWORK >= max(1,M).  
  
