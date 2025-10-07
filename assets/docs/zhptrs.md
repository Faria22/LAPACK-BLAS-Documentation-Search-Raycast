```fortran  
subroutine zhptrs (  
character uplo,  
integer n,  
integer nrhs,  
complex*16, dimension(*) ap,  
integer, dimension(*) ipiv,  
complex*16, dimension(ldb, *) b,  
integer ldb,  
integer info  
)  
```  
  
ZHPTRS solves a system of linear equations A*X = B with a complex  
Hermitian matrix A stored in packed format using the factorization  
A = U*D*U**H or A = L*D*L**H computed by ZHPTRF.  
  
## Parameters  
Uplo : Character*1 [in]  
> Specifies whether the details of the factorization are stored  
> as an upper or lower triangular matrix.  
  
N : Integer [in]  
> The order of the matrix A.  N >= 0.  
  
Nrhs : Integer [in]  
> The number of right hand sides, i.e., the number of columns  
> of the matrix B.  NRHS >= 0.  
  
Ap : Complex*16 Array, Dimension (n*(n+1)/2) [in]  
> The block diagonal matrix D and the multipliers used to  
> obtain the factor U or L as computed by ZHPTRF, stored as a  
> packed triangular matrix.  
  
Ipiv : Integer Array, Dimension (n) [in]  
> Details of the interchanges and the block structure of D  
> as determined by ZHPTRF.  
  
B : Complex*16 Array, Dimension (ldb,nrhs) [in,out]  
> On entry, the right hand side matrix B.  
> On exit, the solution matrix X.  
  
Ldb : Integer [in]  
> The leading dimension of the array B.  LDB >= max(1,N).  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0: if INFO = -i, the i-th argument had an illegal value  
  
