```fortran  
subroutine dgetrs (  
character trans,  
integer n,  
integer nrhs,  
double precision, dimension(lda, *) a,  
integer lda,  
integer, dimension(*) ipiv,  
double precision, dimension(ldb, *) b,  
integer ldb,  
integer info  
)  
```  
  
DGETRS solves a system of linear equations  
A * X = B  or  A**T * X = B  
with a general N-by-N matrix A using the LU factorization computed  
by DGETRF.  
  
## Parameters  
Trans : Character*1 [in]  
> Specifies the form of the system of equations:  
  
N : Integer [in]  
> The order of the matrix A.  N >= 0.  
  
Nrhs : Integer [in]  
> The number of right hand sides, i.e., the number of columns  
> of the matrix B.  NRHS >= 0.  
  
A : Double Precision Array, Dimension (lda,n) [in]  
> as computed by DGETRF.  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,N).  
  
Ipiv : Integer Array, Dimension (n) [in]  
> The pivot indices from DGETRF; for 1<=i<=N, row i of the  
> matrix was interchanged with row IPIV(i).  
  
B : Double Precision Array, Dimension (ldb,nrhs) [in,out]  
> On entry, the right hand side matrix B.  
> On exit, the solution matrix X.  
  
Ldb : Integer [in]  
> The leading dimension of the array B.  LDB >= max(1,N).  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
  
