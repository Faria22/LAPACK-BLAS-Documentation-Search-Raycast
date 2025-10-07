```fortran  
subroutine cpttrs (  
character uplo,  
integer n,  
integer nrhs,  
real, dimension(*) d,  
complex, dimension(*) e,  
complex, dimension(ldb, *) b,  
integer ldb,  
integer info  
)  
```  
  
CPTTRS solves a tridiagonal system of the form  
A * X = B  
using the factorization A = U**H*D*U or A = L*D*L**H computed by CPTTRF.  
D is a diagonal matrix specified in the vector D, U (or L) is a unit  
bidiagonal matrix whose superdiagonal (subdiagonal) is specified in  
the vector E, and X and B are N by NRHS matrices.  
  
## Parameters  
Uplo : Character*1 [in]  
> Specifies the form of the factorization and whether the  
> vector E is the superdiagonal of the upper bidiagonal factor  
> U or the subdiagonal of the lower bidiagonal factor L.  
  
N : Integer [in]  
> The order of the tridiagonal matrix A.  N >= 0.  
  
Nrhs : Integer [in]  
> The number of right hand sides, i.e., the number of columns  
> of the matrix B.  NRHS >= 0.  
  
D : Real Array, Dimension (n) [in]  
> The n diagonal elements of the diagonal matrix D from the  
  
E : Complex Array, Dimension (n-1) [in]  
> If UPLO = 'U', the (n-1) superdiagonal elements of the unit  
> If UPLO = 'L', the (n-1) subdiagonal elements of the unit  
  
B : Complex Array, Dimension (ldb,nrhs) [in,out]  
> On entry, the right hand side vectors B for the system of  
> linear equations.  
> On exit, the solution vectors, X.  
  
Ldb : Integer [in]  
> The leading dimension of the array B.  LDB >= max(1,N).  
  
Info : Integer [out]  
> = 0: successful exit  
> < 0: if INFO = -k, the k-th argument had an illegal value  
  
