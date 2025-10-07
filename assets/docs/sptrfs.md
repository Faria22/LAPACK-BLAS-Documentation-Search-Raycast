```fortran  
subroutine sptrfs (  
n,  
nrhs,  
d,  
e,  
df,  
ef,  
b,  
ldb,  
x,  
ldx,  
ferr,  
*                          berr,  
work,  
info  
)  
```  
  
SPTRFS improves the computed solution to a system of linear  
equations when the coefficient matrix is symmetric positive definite  
and tridiagonal, and provides error bounds and backward error  
estimates for the solution.  
  
## Parameters  
N : Integer [in]  
> The order of the matrix A.  N >= 0.  
  
Nrhs : Integer [in]  
> The number of right hand sides, i.e., the number of columns  
> of the matrix B.  NRHS >= 0.  
  
D : Real Array, Dimension (n) [in]  
> The n diagonal elements of the tridiagonal matrix A.  
  
E : Real Array, Dimension (n-1) [in]  
> The (n-1) subdiagonal elements of the tridiagonal matrix A.  
  
Df : Real Array, Dimension (n) [in]  
> The n diagonal elements of the diagonal matrix D from the  
> factorization computed by SPTTRF.  
  
Ef : Real Array, Dimension (n-1) [in]  
> The (n-1) subdiagonal elements of the unit bidiagonal factor  
> L from the factorization computed by SPTTRF.  
  
B : Real Array, Dimension (ldb,nrhs) [in]  
> The right hand side matrix B.  
  
Ldb : Integer [in]  
> The leading dimension of the array B.  LDB >= max(1,N).  
  
X : Real Array, Dimension (ldx,nrhs) [in,out]  
> On entry, the solution matrix X, as computed by SPTTRS.  
> On exit, the improved solution matrix X.  
  
Ldx : Integer [in]  
> The leading dimension of the array X.  LDX >= max(1,N).  
  
Ferr : Real Array, Dimension (nrhs) [out]  
> The forward error bound for each solution vector  
> X(j) (the j-th column of the solution matrix X).  
> If XTRUE is the true solution corresponding to X(j), FERR(j)  
> is an estimated upper bound for the magnitude of the largest  
> element in (X(j) - XTRUE) divided by the magnitude of the  
> largest element in X(j).  
  
Berr : Real Array, Dimension (nrhs) [out]  
> The componentwise relative backward error of each solution  
> vector X(j) (i.e., the smallest relative change in  
> any element of A or B that makes X(j) an exact solution).  
  
Work : Real Array, Dimension (2*n) [out]  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
  
