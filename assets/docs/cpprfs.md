```fortran  
subroutine cpprfs (  
uplo,  
n,  
nrhs,  
ap,  
afp,  
b,  
ldb,  
x,  
ldx,  
ferr,  
*                          berr,  
work,  
rwork,  
info  
)  
```  
  
CPPRFS improves the computed solution to a system of linear  
equations when the coefficient matrix is Hermitian positive definite  
and packed, and provides error bounds and backward error estimates  
for the solution.  
  
## Parameters  
Uplo : Character*1 [in]  
> = 'U':  Upper triangle of A is stored;  
> = 'L':  Lower triangle of A is stored.  
  
N : Integer [in]  
> The order of the matrix A.  N >= 0.  
  
Nrhs : Integer [in]  
> The number of right hand sides, i.e., the number of columns  
> of the matrices B and X.  NRHS >= 0.  
  
Ap : Complex Array, Dimension (n*(n+1)/2) [in]  
> The upper or lower triangle of the Hermitian matrix A, packed  
> columnwise in a linear array.  The j-th column of A is stored  
> in the array AP as follows:  
  
Afp : Complex Array, Dimension (n*(n+1)/2) [in]  
> The triangular factor U or L from the Cholesky factorization  
> packed columnwise in a linear array in the same format as A  
> (see AP).  
  
B : Complex Array, Dimension (ldb,nrhs) [in]  
> The right hand side matrix B.  
  
Ldb : Integer [in]  
> The leading dimension of the array B.  LDB >= max(1,N).  
  
X : Complex Array, Dimension (ldx,nrhs) [in,out]  
> On entry, the solution matrix X, as computed by CPPTRS.  
> On exit, the improved solution matrix X.  
  
Ldx : Integer [in]  
> The leading dimension of the array X.  LDX >= max(1,N).  
  
Ferr : Real Array, Dimension (nrhs) [out]  
> The estimated forward error bound for each solution vector  
> X(j) (the j-th column of the solution matrix X).  
> If XTRUE is the true solution corresponding to X(j), FERR(j)  
> is an estimated upper bound for the magnitude of the largest  
> element in (X(j) - XTRUE) divided by the magnitude of the  
> largest element in X(j).  The estimate is as reliable as  
> the estimate for RCOND, and is almost always a slight  
> overestimate of the true error.  
  
Berr : Real Array, Dimension (nrhs) [out]  
> The componentwise relative backward error of each solution  
> vector X(j) (i.e., the smallest relative change in  
> any element of A or B that makes X(j) an exact solution).  
  
Work : Complex Array, Dimension (2*n) [out]  
  
Rwork : Real Array, Dimension (n) [out]  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
  
