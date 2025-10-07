```fortran  
subroutine zgeqrt (  
integer m,  
integer n,  
integer nb,  
complex*16, dimension(lda, *) a,  
integer lda,  
complex*16, dimension(ldt, *) t,  
integer ldt,  
complex*16, dimension(*) work,  
integer info  
)  
```  
  
ZGEQRT computes a blocked QR factorization of a complex M-by-N matrix A  
using the compact WY representation of Q.  
  
## Parameters  
M : Integer [in]  
> The number of rows of the matrix A.  M >= 0.  
  
N : Integer [in]  
> The number of columns of the matrix A.  N >= 0.  
  
Nb : Integer [in]  
> The block size to be used in the blocked QR.  MIN(M,N) >= NB >= 1.  
  
A : Complex*16 Array, Dimension (lda,n) [in,out]  
> On entry, the M-by-N matrix A.  
> On exit, the elements on and above the diagonal of the array  
> contain the min(M,N)-by-N upper trapezoidal matrix R (R is  
> upper triangular if M >= N); the elements below the diagonal  
> are the columns of V.  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,M).  
  
T : Complex*16 Array, Dimension (ldt,min(m,n)) [out]  
> The upper triangular block reflectors stored in compact form  
> as a sequence of upper triangular blocks.  See below  
> for further details.  
  
Ldt : Integer [in]  
> The leading dimension of the array T.  LDT >= NB.  
  
Work : Complex*16 Array, Dimension (nb*n) [out]  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
  
