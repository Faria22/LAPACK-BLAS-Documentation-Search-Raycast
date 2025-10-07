```fortran  
subroutine sgtsv (  
integer n,  
integer nrhs,  
real, dimension(*) dl,  
real, dimension(*) d,  
real, dimension(*) du,  
real, dimension(ldb, *) b,  
integer ldb,  
integer info  
)  
```  
  
SGTSV  solves the equation  
  
A*X = B,  
  
where A is an n by n tridiagonal matrix, by Gaussian elimination with  
partial pivoting.  
  
Note that the equation  A**T*X = B  may be solved by interchanging the  
order of the arguments DU and DL.  
  
## Parameters  
N : Integer [in]  
> The order of the matrix A.  N >= 0.  
  
Nrhs : Integer [in]  
> The number of right hand sides, i.e., the number of columns  
> of the matrix B.  NRHS >= 0.  
  
Dl : Real Array, Dimension (n-1) [in,out]  
> On entry, DL must contain the (n-1) sub-diagonal elements of  
> A.  
> On exit, DL is overwritten by the (n-2) elements of the  
> second super-diagonal of the upper triangular matrix U from  
> the LU factorization of A, in DL(1), ..., DL(n-2).  
  
D : Real Array, Dimension (n) [in,out]  
> On entry, D must contain the diagonal elements of A.  
> On exit, D is overwritten by the n diagonal elements of U.  
  
Du : Real Array, Dimension (n-1) [in,out]  
> On entry, DU must contain the (n-1) super-diagonal elements  
> of A.  
> On exit, DU is overwritten by the (n-1) elements of the first  
> super-diagonal of U.  
  
B : Real Array, Dimension (ldb,nrhs) [in,out]  
> On entry, the N by NRHS matrix of right hand side matrix B.  
> On exit, if INFO = 0, the N by NRHS solution matrix X.  
  
Ldb : Integer [in]  
> The leading dimension of the array B.  LDB >= max(1,N).  
  
Info : Integer [out]  
> = 0: successful exit  
> < 0: if INFO = -i, the i-th argument had an illegal value  
> > 0: if INFO = i, U(i,i) is exactly zero, and the solution  
> has not been computed.  The factorization has not been  
> completed unless i = N.  
  
