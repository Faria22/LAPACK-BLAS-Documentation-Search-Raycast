```fortran  
subroutine dgelqt (  
integer m,  
integer n,  
integer mb,  
double precision, dimension(lda, *) a,  
integer lda,  
double precision, dimension(ldt, *) t,  
integer ldt,  
double precision, dimension(*) work,  
integer info  
)  
```  
  
DGELQT computes a blocked LQ factorization of a real M-by-N matrix A  
using the compact WY representation of Q.  
  
## Parameters  
M : Integer [in]  
> The number of rows of the matrix A.  M >= 0.  
  
N : Integer [in]  
> The number of columns of the matrix A.  N >= 0.  
  
Mb : Integer [in]  
> The block size to be used in the blocked LQ.  MIN(M,N) >= MB >= 1.  
  
A : Double Precision Array, Dimension (lda,n) [in,out]  
> On entry, the M-by-N matrix A.  
> On exit, the elements on and below the diagonal of the array  
> contain the M-by-MIN(M,N) lower trapezoidal matrix L (L is  
> lower triangular if M <= N); the elements above the diagonal  
> are the rows of V.  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,M).  
  
T : Double Precision Array, Dimension (ldt,min(m,n)) [out]  
> The upper triangular block reflectors stored in compact form  
> as a sequence of upper triangular blocks.  See below  
> for further details.  
  
Ldt : Integer [in]  
> The leading dimension of the array T.  LDT >= MB.  
  
Work : Double Precision Array, Dimension (mb*m). [out]  
> recommended value to use.  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
  
