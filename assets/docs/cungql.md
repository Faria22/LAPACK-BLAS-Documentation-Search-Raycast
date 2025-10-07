```fortran  
subroutine cungql (  
integer m,  
integer n,  
integer k,  
complex, dimension(lda, *) a,  
integer lda,  
complex, dimension(*) tau,  
complex, dimension(*) work,  
integer lwork,  
integer info  
)  
```  
  
CUNGQL generates an M-by-N complex matrix Q with orthonormal columns,  
which is defined as the last N columns of a product of K elementary  
reflectors of order M  
  
Q  =  H(k) . . . H(2) H(1)  
  
as returned by CGEQLF.  
  
## Parameters  
M : Integer [in]  
> The number of rows of the matrix Q. M >= 0.  
  
N : Integer [in]  
> The number of columns of the matrix Q. M >= N >= 0.  
  
K : Integer [in]  
> The number of elementary reflectors whose product defines the  
> matrix Q. N >= K >= 0.  
  
A : Complex Array, Dimension (lda,n) [in,out]  
> On entry, the (n-k+i)-th column must contain the vector which  
> defines the elementary reflector H(i), for i = 1,2,...,k, as  
> returned by CGEQLF in the last k columns of its array  
> argument A.  
> On exit, the M-by-N matrix Q.  
  
Lda : Integer [in]  
> The first dimension of the array A. LDA >= max(1,M).  
  
Tau : Complex Array, Dimension (k) [in]  
> TAU(i) must contain the scalar factor of the elementary  
> reflector H(i), as returned by CGEQLF.  
  
Work : Complex Array, Dimension (max(1,lwork)) [out]  
> On exit, if INFO = 0, WORK(1) returns the optimal LWORK.  
  
Lwork : Integer [in]  
> The dimension of the array WORK. LWORK >= max(1,N).  
> optimal blocksize.  
> If LWORK = -1, then a workspace query is assumed; the routine  
> only calculates the optimal size of the WORK array, returns  
> this value as the first entry of the WORK array, and no error  
> message related to LWORK is issued by XERBLA.  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument has an illegal value  
  
