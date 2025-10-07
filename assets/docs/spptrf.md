```fortran  
subroutine spptrf (  
character uplo,  
integer n,  
real, dimension(*) ap,  
integer info  
)  
```  
  
SPPTRF computes the Cholesky factorization of a real symmetric  
positive definite matrix A stored in packed format.  
  
The factorization has the form  
A = U**T * U,  if UPLO = 'U', or  
A = L  * L**T,  if UPLO = 'L',  
where U is an upper triangular matrix and L is lower triangular.  
  
## Parameters  
Uplo : Character*1 [in]  
> = 'U':  Upper triangle of A is stored;  
> = 'L':  Lower triangle of A is stored.  
  
N : Integer [in]  
> The order of the matrix A.  N >= 0.  
  
Ap : Real Array, Dimension (n*(n+1)/2) [in,out]  
> On entry, the upper or lower triangle of the symmetric matrix  
> A, packed columnwise in a linear array.  The j-th column of A  
> is stored in the array AP as follows:  
> See below for further details.  
> On exit, if INFO = 0, the triangular factor U or L from the  
> storage format as A.  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
> > 0:  if INFO = i, the leading principal minor of order i  
> is not positive, and the factorization could not be  
> completed.  
  
