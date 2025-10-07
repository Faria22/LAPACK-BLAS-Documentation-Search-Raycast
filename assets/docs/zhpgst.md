```fortran  
subroutine zhpgst (  
integer itype,  
character uplo,  
integer n,  
complex*16, dimension(*) ap,  
complex*16, dimension(*) bp,  
integer info  
)  
```  
  
ZHPGST reduces a complex Hermitian-definite generalized  
eigenproblem to standard form, using packed storage.  
  
If ITYPE = 1, the problem is A*x = lambda*B*x,  
and A is overwritten by inv(U**H)*A*inv(U) or inv(L)*A*inv(L**H)  
  
If ITYPE = 2 or 3, the problem is A*B*x = lambda*x or  
B*A*x = lambda*x, and A is overwritten by U*A*U**H or L**H*A*L.  
  
B must have been previously factorized as U**H*U or L*L**H by ZPPTRF.  
  
## Parameters  
Itype : Integer [in]  
  
Uplo : Character*1 [in]  
> = 'U':  Upper triangle of A is stored and B is factored as  
> = 'L':  Lower triangle of A is stored and B is factored as  
  
N : Integer [in]  
> The order of the matrices A and B.  N >= 0.  
  
Ap : Complex*16 Array, Dimension (n*(n+1)/2) [in,out]  
> On entry, the upper or lower triangle of the Hermitian matrix  
> A, packed columnwise in a linear array.  The j-th column of A  
> is stored in the array AP as follows:  
> On exit, if INFO = 0, the transformed matrix, stored in the  
> same format as A.  
  
Bp : Complex*16 Array, Dimension (n*(n+1)/2) [in]  
> The triangular factor from the Cholesky factorization of B,  
> stored in the same format as A, as returned by ZPPTRF.  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
  
