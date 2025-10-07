```fortran  
subroutine ztprfb (  
side,  
trans,  
direct,  
storev,  
m,  
n,  
k,  
l,  
*                          v,  
ldv,  
t,  
ldt,  
a,  
lda,  
b,  
ldb,  
work,  
ldwork  
)  
```  
  
ZTPRFB applies a complex "triangular-pentagonal" block reflector H or its  
conjugate transpose H**H to a complex matrix C, which is composed of two  
blocks A and B, either from the left or right.  
  
  
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
> = 'C': Columns  
> = 'R': Rows  
  
M : Integer [in]  
> The number of rows of the matrix B.  
> M >= 0.  
  
N : Integer [in]  
> The number of columns of the matrix B.  
> N >= 0.  
  
K : Integer [in]  
> The order of the matrix T, i.e. the number of elementary  
> reflectors whose product defines the block reflector.  
> K >= 0.  
  
L : Integer [in]  
> The order of the trapezoidal part of V.  
> K >= L >= 0.  See Further Details.  
  
V : Complex*16 Array, Dimension [in]  
> (LDV,K) if STOREV = 'C'  
> (LDV,M) if STOREV = 'R' and SIDE = 'L'  
> (LDV,N) if STOREV = 'R' and SIDE = 'R'  
> The pentagonal matrix V, which contains the elementary reflectors  
> H(1), H(2), ..., H(K).  See Further Details.  
  
Ldv : Integer [in]  
> The leading dimension of the array V.  
> If STOREV = 'C' and SIDE = 'L', LDV >= max(1,M);  
> if STOREV = 'C' and SIDE = 'R', LDV >= max(1,N);  
> if STOREV = 'R', LDV >= K.  
  
T : Complex*16 Array, Dimension (ldt,k) [in]  
> The triangular K-by-K matrix T in the representation of the  
> block reflector.  
  
Ldt : Integer [in]  
> The leading dimension of the array T.  
> LDT >= K.  
  
A : Complex*16 Array, Dimension [in,out]  
> (LDA,N) if SIDE = 'L' or (LDA,K) if SIDE = 'R'  
> On entry, the K-by-N or M-by-K matrix A.  
> On exit, A is overwritten by the corresponding block of  
  
Lda : Integer [in]  
> The leading dimension of the array A.  
> If SIDE = 'L', LDA >= max(1,K);  
> If SIDE = 'R', LDA >= max(1,M).  
  
B : Complex*16 Array, Dimension (ldb,n) [in,out]  
> On entry, the M-by-N matrix B.  
> On exit, B is overwritten by the corresponding block of  
  
Ldb : Integer [in]  
> The leading dimension of the array B.  
> LDB >= max(1,M).  
  
Work : Complex*16 Array, Dimension [out]  
> (LDWORK,N) if SIDE = 'L',  
> (LDWORK,K) if SIDE = 'R'.  
  
Ldwork : Integer [in]  
> The leading dimension of the array WORK.  
> If SIDE = 'L', LDWORK >= K;  
> if SIDE = 'R', LDWORK >= M.  
  
