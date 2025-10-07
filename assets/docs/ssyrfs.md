```fortran  
subroutine ssyrfs (  
uplo,  
n,  
nrhs,  
a,  
lda,  
af,  
ldaf,  
ipiv,  
b,  
ldb,  
*                          x,  
ldx,  
ferr,  
berr,  
work,  
iwork,  
info  
)  
```  
  
SSYRFS improves the computed solution to a system of linear  
equations when the coefficient matrix is symmetric indefinite, and  
provides error bounds and backward error estimates for the solution.  
  
## Parameters  
Uplo : Character*1 [in]  
> = 'U':  Upper triangle of A is stored;  
> = 'L':  Lower triangle of A is stored.  
  
N : Integer [in]  
> The order of the matrix A.  N >= 0.  
  
Nrhs : Integer [in]  
> The number of right hand sides, i.e., the number of columns  
> of the matrices B and X.  NRHS >= 0.  
  
A : Real Array, Dimension (lda,n) [in]  
> The symmetric matrix A.  If UPLO = 'U', the leading N-by-N  
> upper triangular part of A contains the upper triangular part  
> of the matrix A, and the strictly lower triangular part of A  
> is not referenced.  If UPLO = 'L', the leading N-by-N lower  
> triangular part of A contains the lower triangular part of  
> the matrix A, and the strictly upper triangular part of A is  
> not referenced.  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,N).  
  
Af : Real Array, Dimension (ldaf,n) [in]  
> The factored form of the matrix A.  AF contains the block  
> diagonal matrix D and the multipliers used to obtain the  
  
Ldaf : Integer [in]  
> The leading dimension of the array AF.  LDAF >= max(1,N).  
  
Ipiv : Integer Array, Dimension (n) [in]  
> Details of the interchanges and the block structure of D  
> as determined by SSYTRF.  
  
B : Real Array, Dimension (ldb,nrhs) [in]  
> The right hand side matrix B.  
  
Ldb : Integer [in]  
> The leading dimension of the array B.  LDB >= max(1,N).  
  
X : Real Array, Dimension (ldx,nrhs) [in,out]  
> On entry, the solution matrix X, as computed by SSYTRS.  
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
  
Work : Real Array, Dimension (3*n) [out]  
  
Iwork : Integer Array, Dimension (n) [out]  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
  
