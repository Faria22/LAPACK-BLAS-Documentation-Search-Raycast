```fortran  
subroutine dtpmqrt (  
side,  
trans,  
m,  
n,  
k,  
l,  
nb,  
v,  
ldv,  
t,  
ldt,  
*                           a,  
lda,  
b,  
ldb,  
work,  
info  
)  
```  
  
DTPMQRT applies a real orthogonal matrix Q obtained from a  
"triangular-pentagonal" real block reflector H to a general  
real matrix C, which consists of two blocks A and B.  
  
## Parameters  
Side : Character*1 [in]  
  
Trans : Character*1 [in]  
> = 'N':  No transpose, apply Q;  
  
M : Integer [in]  
> The number of rows of the matrix B. M >= 0.  
  
N : Integer [in]  
> The number of columns of the matrix B. N >= 0.  
  
K : Integer [in]  
> The number of elementary reflectors whose product defines  
> the matrix Q.  
  
L : Integer [in]  
> The order of the trapezoidal part of V.  
> K >= L >= 0.  See Further Details.  
  
Nb : Integer [in]  
> The block size used for the storage of T.  K >= NB >= 1.  
> This must be the same value of NB used to generate T  
> in CTPQRT.  
  
V : Double Precision Array, Dimension (ldv,k) [in]  
> The i-th column must contain the vector which defines the  
> elementary reflector H(i), for i = 1,2,...,k, as returned by  
> CTPQRT in B.  See Further Details.  
  
Ldv : Integer [in]  
> The leading dimension of the array V.  
> If SIDE = 'L', LDV >= max(1,M);  
> if SIDE = 'R', LDV >= max(1,N).  
  
T : Double Precision Array, Dimension (ldt,k) [in]  
> The upper triangular factors of the block reflectors  
> as returned by CTPQRT, stored as a NB-by-K matrix.  
  
Ldt : Integer [in]  
> The leading dimension of the array T.  LDT >= NB.  
  
A : Double Precision Array, Dimension [in,out]  
> (LDA,N) if SIDE = 'L' or  
> (LDA,K) if SIDE = 'R'  
> On entry, the K-by-N or M-by-K matrix A.  
> On exit, A is overwritten by the corresponding block of  
  
Lda : Integer [in]  
> The leading dimension of the array A.  
> If SIDE = 'L', LDC >= max(1,K);  
> If SIDE = 'R', LDC >= max(1,M).  
  
B : Double Precision Array, Dimension (ldb,n) [in,out]  
> On entry, the M-by-N matrix B.  
> On exit, B is overwritten by the corresponding block of  
  
Ldb : Integer [in]  
> The leading dimension of the array B.  
> LDB >= max(1,M).  
  
Work : Double Precision Array. The Dimension of Work is [out]  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
  
