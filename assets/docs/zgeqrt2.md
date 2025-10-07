```fortran  
subroutine zgeqrt2 (  
integer m,  
integer n,  
complex*16, dimension(lda, *) a,  
integer lda,  
complex*16, dimension(ldt, *) t,  
integer ldt,  
integer info  
)  
```  
  
ZGEQRT2 computes a QR factorization of a complex M-by-N matrix A,  
using the compact WY representation of Q.  
  
## Parameters  
M : Integer [in]  
> The number of rows of the matrix A.  M >= N.  
  
N : Integer [in]  
> The number of columns of the matrix A.  N >= 0.  
  
A : Complex*16 Array, Dimension (lda,n) [in,out]  
> On entry, the complex M-by-N matrix A.  On exit, the elements on and  
> above the diagonal contain the N-by-N upper triangular matrix R; the  
> elements below the diagonal are the columns of V.  See below for  
> further details.  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,M).  
  
T : Complex*16 Array, Dimension (ldt,n) [out]  
> The N-by-N upper triangular factor of the block reflector.  
> The elements on and above the diagonal contain the block  
> reflector T; the elements below the diagonal are not used.  
> See below for further details.  
  
Ldt : Integer [in]  
> The leading dimension of the array T.  LDT >= max(1,N).  
  
Info : Integer [out]  
> = 0: successful exit  
> < 0: if INFO = -i, the i-th argument had an illegal value  
  
