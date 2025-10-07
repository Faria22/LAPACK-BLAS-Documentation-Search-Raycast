```fortran  
subroutine dpftrs (  
character transr,  
character uplo,  
integer n,  
integer nrhs,  
double precision, dimension(0: *) a,  
double precision, dimension(ldb, *) b,  
integer ldb,  
integer info  
)  
```  
  
DPFTRS solves a system of linear equations A*X = B with a symmetric  
positive definite matrix A using the Cholesky factorization  
A = U**T*U or A = L*L**T computed by DPFTRF.  
  
## Parameters  
Transr : Character*1 [in]  
> = 'N':  The Normal TRANSR of RFP A is stored;  
> = 'T':  The Transpose TRANSR of RFP A is stored.  
  
Uplo : Character*1 [in]  
> = 'U':  Upper triangle of RFP A is stored;  
> = 'L':  Lower triangle of RFP A is stored.  
  
N : Integer [in]  
> The order of the matrix A.  N >= 0.  
  
Nrhs : Integer [in]  
> The number of right hand sides, i.e., the number of columns  
> of the matrix B.  NRHS >= 0.  
  
A : Double Precision Array, Dimension ( N*(n+1)/2 ). [in]  
> The triangular factor U or L from the Cholesky factorization  
> See note below for more details about RFP A.  
  
B : Double Precision Array, Dimension (ldb,nrhs) [in,out]  
> On entry, the right hand side matrix B.  
> On exit, the solution matrix X.  
  
Ldb : Integer [in]  
> The leading dimension of the array B.  LDB >= max(1,N).  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
  
