```fortran  
subroutine csptrs (  
character uplo,  
integer n,  
integer nrhs,  
complex, dimension(*) ap,  
integer, dimension(*) ipiv,  
complex, dimension(ldb, *) b,  
integer ldb,  
integer info  
)  
```  
  
CSPTRS solves a system of linear equations A*X = B with a complex  
symmetric matrix A stored in packed format using the factorization  
A = U*D*U**T or A = L*D*L**T computed by CSPTRF.  
  
## Parameters  
Uplo : Character*1 [in]  
> Specifies whether the details of the factorization are stored  
> as an upper or lower triangular matrix.  
  
N : Integer [in]  
> The order of the matrix A.  N >= 0.  
  
Nrhs : Integer [in]  
> The number of right hand sides, i.e., the number of columns  
> of the matrix B.  NRHS >= 0.  
  
Ap : Complex Array, Dimension (n*(n+1)/2) [in]  
> The block diagonal matrix D and the multipliers used to  
> obtain the factor U or L as computed by CSPTRF, stored as a  
> packed triangular matrix.  
  
Ipiv : Integer Array, Dimension (n) [in]  
> Details of the interchanges and the block structure of D  
> as determined by CSPTRF.  
  
B : Complex Array, Dimension (ldb,nrhs) [in,out]  
> On entry, the right hand side matrix B.  
> On exit, the solution matrix X.  
  
Ldb : Integer [in]  
> The leading dimension of the array B.  LDB >= max(1,N).  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0: if INFO = -i, the i-th argument had an illegal value  
  
