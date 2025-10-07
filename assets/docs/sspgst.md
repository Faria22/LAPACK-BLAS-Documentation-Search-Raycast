```fortran  
subroutine sspgst (  
integer itype,  
character uplo,  
integer n,  
real, dimension(*) ap,  
real, dimension(*) bp,  
integer info  
)  
```  
  
SSPGST reduces a real symmetric-definite generalized eigenproblem  
to standard form, using packed storage.  
  
If ITYPE = 1, the problem is A*x = lambda*B*x,  
and A is overwritten by inv(U**T)*A*inv(U) or inv(L)*A*inv(L**T)  
  
If ITYPE = 2 or 3, the problem is A*B*x = lambda*x or  
B*A*x = lambda*x, and A is overwritten by U*A*U**T or L**T*A*L.  
  
B must have been previously factorized as U**T*U or L*L**T by SPPTRF.  
  
## Parameters  
Itype : Integer [in]  
  
Uplo : Character*1 [in]  
> = 'U':  Upper triangle of A is stored and B is factored as  
> = 'L':  Lower triangle of A is stored and B is factored as  
  
N : Integer [in]  
> The order of the matrices A and B.  N >= 0.  
  
Ap : Real Array, Dimension (n*(n+1)/2) [in,out]  
> On entry, the upper or lower triangle of the symmetric matrix  
> A, packed columnwise in a linear array.  The j-th column of A  
> is stored in the array AP as follows:  
> On exit, if INFO = 0, the transformed matrix, stored in the  
> same format as A.  
  
Bp : Real Array, Dimension (n*(n+1)/2) [in]  
> The triangular factor from the Cholesky factorization of B,  
> stored in the same format as A, as returned by SPPTRF.  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
  
