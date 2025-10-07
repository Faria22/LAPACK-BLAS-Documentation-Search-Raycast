```fortran  
subroutine zpptri (  
character uplo,  
integer n,  
complex*16, dimension(*) ap,  
integer info  
)  
```  
  
ZPPTRI computes the inverse of a complex Hermitian positive definite  
matrix A using the Cholesky factorization A = U**H*U or A = L*L**H  
computed by ZPPTRF.  
  
## Parameters  
Uplo : Character*1 [in]  
> = 'U':  Upper triangular factor is stored in AP;  
> = 'L':  Lower triangular factor is stored in AP.  
  
N : Integer [in]  
> The order of the matrix A.  N >= 0.  
  
Ap : Complex*16 Array, Dimension (n*(n+1)/2) [in,out]  
> On entry, the triangular factor U or L from the Cholesky  
> a linear array.  The j-th column of U or L is stored in the  
> array AP as follows:  
> On exit, the upper or lower triangle of the (Hermitian)  
> inverse of A, overwriting the input factor U or L.  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
> > 0:  if INFO = i, the (i,i) element of the factor U or L is  
> zero, and the inverse could not be computed.  
  
