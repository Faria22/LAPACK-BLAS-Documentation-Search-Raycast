```fortran  
subroutine zungrq (  
integer m,  
integer n,  
integer k,  
complex*16, dimension(lda, *) a,  
integer lda,  
complex*16, dimension(*) tau,  
complex*16, dimension(*) work,  
integer lwork,  
integer info  
)  
```  
  
ZUNGRQ generates an M-by-N complex matrix Q with orthonormal rows,  
which is defined as the last M rows of a product of K elementary  
reflectors of order N  
  
Q  =  H(1)**H H(2)**H . . . H(k)**H  
  
as returned by ZGERQF.  
  
## Parameters  
M : Integer [in]  
> The number of rows of the matrix Q. M >= 0.  
  
N : Integer [in]  
> The number of columns of the matrix Q. N >= M.  
  
K : Integer [in]  
> The number of elementary reflectors whose product defines the  
> matrix Q. M >= K >= 0.  
  
A : Complex*16 Array, Dimension (lda,n) [in,out]  
> On entry, the (m-k+i)-th row must contain the vector which  
> defines the elementary reflector H(i), for i = 1,2,...,k, as  
> returned by ZGERQF in the last k rows of its array argument  
> A.  
> On exit, the M-by-N matrix Q.  
  
Lda : Integer [in]  
> The first dimension of the array A. LDA >= max(1,M).  
  
Tau : Complex*16 Array, Dimension (k) [in]  
> TAU(i) must contain the scalar factor of the elementary  
> reflector H(i), as returned by ZGERQF.  
  
Work : Complex*16 Array, Dimension (max(1,lwork)) [out]  
> On exit, if INFO = 0, WORK(1) returns the optimal LWORK.  
  
Lwork : Integer [in]  
> The dimension of the array WORK. LWORK >= max(1,M).  
> optimal blocksize.  
> If LWORK = -1, then a workspace query is assumed; the routine  
> only calculates the optimal size of the WORK array, returns  
> this value as the first entry of the WORK array, and no error  
> message related to LWORK is issued by XERBLA.  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument has an illegal value  
  
