```fortran  
subroutine dpotri (  
character uplo,  
integer n,  
double precision, dimension(lda, *) a,  
integer lda,  
integer info  
)  
```  
  
DPOTRI computes the inverse of a real symmetric positive definite  
matrix A using the Cholesky factorization A = U**T*U or A = L*L**T  
computed by DPOTRF.  
  
## Parameters  
Uplo : Character*1 [in]  
> = 'U':  Upper triangle of A is stored;  
> = 'L':  Lower triangle of A is stored.  
  
N : Integer [in]  
> The order of the matrix A.  N >= 0.  
  
A : Double Precision Array, Dimension (lda,n) [in,out]  
> On entry, the triangular factor U or L from the Cholesky  
> DPOTRF.  
> On exit, the upper or lower triangle of the (symmetric)  
> inverse of A, overwriting the input factor U or L.  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,N).  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
> > 0:  if INFO = i, the (i,i) element of the factor U or L is  
> zero, and the inverse could not be computed.  
  
