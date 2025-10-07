```fortran  
subroutine zgttrs (  
trans,  
n,  
nrhs,  
dl,  
d,  
du,  
du2,  
ipiv,  
b,  
ldb,  
*                          info  
)  
```  
  
ZGTTRS solves one of the systems of equations  
A * X = B,  A**T * X = B,  or  A**H * X = B,  
with a tridiagonal matrix A using the LU factorization computed  
by ZGTTRF.  
  
## Parameters  
Trans : Character*1 [in]  
> Specifies the form of the system of equations.  
  
N : Integer [in]  
> The order of the matrix A.  
  
Nrhs : Integer [in]  
> The number of right hand sides, i.e., the number of columns  
> of the matrix B.  NRHS >= 0.  
  
Dl : Complex*16 Array, Dimension (n-1) [in]  
> The (n-1) multipliers that define the matrix L from the  
> LU factorization of A.  
  
D : Complex*16 Array, Dimension (n) [in]  
> The n diagonal elements of the upper triangular matrix U from  
> the LU factorization of A.  
  
Du : Complex*16 Array, Dimension (n-1) [in]  
> The (n-1) elements of the first super-diagonal of U.  
  
Du2 : Complex*16 Array, Dimension (n-2) [in]  
> The (n-2) elements of the second super-diagonal of U.  
  
Ipiv : Integer Array, Dimension (n) [in]  
> The pivot indices; for 1 <= i <= n, row i of the matrix was  
> interchanged with row IPIV(i).  IPIV(i) will always be either  
> i or i+1; IPIV(i) = i indicates a row interchange was not  
> required.  
  
B : Complex*16 Array, Dimension (ldb,nrhs) [in,out]  
> On entry, the matrix of right hand side vectors B.  
> On exit, B is overwritten by the solution vectors X.  
  
Ldb : Integer [in]  
> The leading dimension of the array B.  LDB >= max(1,N).  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -k, the k-th argument had an illegal value  
  
