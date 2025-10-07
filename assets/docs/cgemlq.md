```fortran  
subroutine cgemlq (  
side,  
trans,  
m,  
n,  
k,  
a,  
lda,  
t,  
*     $                   tsize,  
c,  
ldc,  
work,  
lwork,  
info  
)  
```  
  
CGEMLQ overwrites the general real M-by-N matrix C with  
  
SIDE = 'L'     SIDE = 'R'  
TRANS = 'N':      Q * C          C * Q  
TRANS = 'C':      Q**H * C       C * Q**H  
where Q is a complex unitary matrix defined as the product  
of blocked elementary reflectors computed by short wide  
LQ factorization (CGELQ)  
  
  
## Parameters  
Side : Character*1 [in]  
  
Trans : Character*1 [in]  
> = 'N':  No transpose, apply Q;  
  
M : Integer [in]  
> The number of rows of the matrix A.  M >=0.  
  
N : Integer [in]  
> The number of columns of the matrix C. N >= 0.  
  
K : Integer [in]  
> The number of elementary reflectors whose product defines  
> the matrix Q.  
> If SIDE = 'L', M >= K >= 0;  
> if SIDE = 'R', N >= K >= 0.  
  
A : Complex Array, Dimension [in]  
> (LDA,M) if SIDE = 'L',  
> (LDA,N) if SIDE = 'R'  
> Part of the data structure to represent Q as returned by CGELQ.  
  
Lda : Integer [in]  
> The leading dimension of the array A. LDA >= max(1,K).  
  
T : Complex Array, Dimension (max(5,tsize)). [in]  
> Part of the data structure to represent Q as returned by CGELQ.  
  
Tsize : Integer [in]  
> The dimension of the array T. TSIZE >= 5.  
  
C : Complex Array, Dimension (ldc,n) [in,out]  
> On entry, the M-by-N matrix C.  
  
Ldc : Integer [in]  
> The leading dimension of the array C. LDC >= max(1,M).  
  
Work : (workspace) Complex Array, Dimension (max(1,lwork)) [out]  
> On exit, if INFO = 0, WORK(1) returns the minimal LWORK.  
  
Lwork : Integer [in]  
> The dimension of the array WORK. LWORK >= 1.  
> If LWORK = -1, then a workspace query is assumed. The routine  
> only calculates the size of the WORK array, returns this  
> value as WORK(1), and no error message related to WORK  
> is issued by XERBLA.  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
  
