```fortran  
subroutine zpptrs (  
character uplo,  
integer n,  
integer nrhs,  
complex*16, dimension(*) ap,  
complex*16, dimension(ldb, *) b,  
integer ldb,  
integer info  
)  
```  
  
ZPPTRS solves a system of linear equations A*X = B with a Hermitian  
positive definite matrix A in packed storage using the Cholesky  
factorization A = U**H * U or A = L * L**H computed by ZPPTRF.  
  
## Parameters  
Uplo : Character*1 [in]  
> = 'U':  Upper triangle of A is stored;  
> = 'L':  Lower triangle of A is stored.  
  
N : Integer [in]  
> The order of the matrix A.  N >= 0.  
  
Nrhs : Integer [in]  
> The number of right hand sides, i.e., the number of columns  
> of the matrix B.  NRHS >= 0.  
  
Ap : Complex*16 Array, Dimension (n*(n+1)/2) [in]  
> The triangular factor U or L from the Cholesky factorization  
> array.  The j-th column of U or L is stored in the array AP  
> as follows:  
  
B : Complex*16 Array, Dimension (ldb,nrhs) [in,out]  
> On entry, the right hand side matrix B.  
> On exit, the solution matrix X.  
  
Ldb : Integer [in]  
> The leading dimension of the array B.  LDB >= max(1,N).  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
  
