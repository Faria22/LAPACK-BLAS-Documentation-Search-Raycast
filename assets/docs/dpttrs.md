```fortran  
subroutine dpttrs (  
integer n,  
integer nrhs,  
double precision, dimension(*) d,  
double precision, dimension(*) e,  
double precision, dimension(ldb, *) b,  
integer ldb,  
integer info  
)  
```  
  
DPTTRS solves a tridiagonal system of the form  
A * X = B  
using the L*D*L**T factorization of A computed by DPTTRF.  D is a  
diagonal matrix specified in the vector D, L is a unit bidiagonal  
matrix whose subdiagonal is specified in the vector E, and X and B  
are N by NRHS matrices.  
  
## Parameters  
N : Integer [in]  
> The order of the tridiagonal matrix A.  N >= 0.  
  
Nrhs : Integer [in]  
> The number of right hand sides, i.e., the number of columns  
> of the matrix B.  NRHS >= 0.  
  
D : Double Precision Array, Dimension (n) [in]  
> The n diagonal elements of the diagonal matrix D from the  
  
E : Double Precision Array, Dimension (n-1) [in]  
> The (n-1) subdiagonal elements of the unit bidiagonal factor  
> as the superdiagonal of the unit bidiagonal factor U from the  
  
B : Double Precision Array, Dimension (ldb,nrhs) [in,out]  
> On entry, the right hand side vectors B for the system of  
> linear equations.  
> On exit, the solution vectors, X.  
  
Ldb : Integer [in]  
> The leading dimension of the array B.  LDB >= max(1,N).  
  
Info : Integer [out]  
> = 0: successful exit  
> < 0: if INFO = -k, the k-th argument had an illegal value  
  
