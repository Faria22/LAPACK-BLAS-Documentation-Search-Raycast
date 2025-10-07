```fortran  
subroutine ctrttp (  
character uplo,  
integer n,  
complex, dimension(lda, *) a,  
integer lda,  
complex, dimension(*) ap,  
integer info  
)  
```  
  
CTRTTP copies a triangular matrix A from full format (TR) to standard  
packed format (TP).  
  
## Parameters  
Uplo : Character*1 [in]  
> = 'U':  A is upper triangular;  
> = 'L':  A is lower triangular.  
  
N : Integer [in]  
> The order of the matrices AP and A.  N >= 0.  
  
A : Complex Array, Dimension (lda,n) [in]  
> On entry, the triangular matrix A.  If UPLO = 'U', the leading  
> N-by-N upper triangular part of A contains the upper  
> triangular part of the matrix A, and the strictly lower  
> triangular part of A is not referenced.  If UPLO = 'L', the  
> leading N-by-N lower triangular part of A contains the lower  
> triangular part of the matrix A, and the strictly upper  
> triangular part of A is not referenced.  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,N).  
  
Ap : Complex Array, Dimension ( N*(n+1)/2 ), [out]  
> On exit, the upper or lower triangular matrix A, packed  
> columnwise in a linear array. The j-th column of A is stored  
> in the array AP as follows:  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
  
