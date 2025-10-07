```fortran  
subroutine sposv (  
character uplo,  
integer n,  
integer nrhs,  
real, dimension(lda, *) a,  
integer lda,  
real, dimension(ldb, *) b,  
integer ldb,  
integer info  
)  
```  
  
SPOSV computes the solution to a real system of linear equations  
A * X = B,  
where A is an N-by-N symmetric positive definite matrix and X and B  
are N-by-NRHS matrices.  
  
The Cholesky decomposition is used to factor A as  
A = U**T* U,  if UPLO = 'U', or  
A = L * L**T,  if UPLO = 'L',  
where U is an upper triangular matrix and L is a lower triangular  
matrix.  The factored form of A is then used to solve the system of  
equations A * X = B.  
  
## Parameters  
Uplo : Character*1 [in]  
> = 'U':  Upper triangle of A is stored;  
> = 'L':  Lower triangle of A is stored.  
  
N : Integer [in]  
> The number of linear equations, i.e., the order of the  
> matrix A.  N >= 0.  
  
Nrhs : Integer [in]  
> The number of right hand sides, i.e., the number of columns  
> of the matrix B.  NRHS >= 0.  
  
A : Real Array, Dimension (lda,n) [in,out]  
> On entry, the symmetric matrix A.  If UPLO = 'U', the leading  
> N-by-N upper triangular part of A contains the upper  
> triangular part of the matrix A, and the strictly lower  
> triangular part of A is not referenced.  If UPLO = 'L', the  
> leading N-by-N lower triangular part of A contains the lower  
> triangular part of the matrix A, and the strictly upper  
> triangular part of A is not referenced.  
> On exit, if INFO = 0, the factor U or L from the Cholesky  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,N).  
  
B : Real Array, Dimension (ldb,nrhs) [in,out]  
> On entry, the N-by-NRHS right hand side matrix B.  
> On exit, if INFO = 0, the N-by-NRHS solution matrix X.  
  
Ldb : Integer [in]  
> The leading dimension of the array B.  LDB >= max(1,N).  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
> > 0:  if INFO = i, the leading principal minor of order i  
> of A is not positive, so the factorization could not  
> be completed, and the solution has not been computed.  
  
