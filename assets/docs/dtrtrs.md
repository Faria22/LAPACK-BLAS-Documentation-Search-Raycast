```fortran  
subroutine dtrtrs (  
uplo,  
trans,  
diag,  
n,  
nrhs,  
a,  
lda,  
b,  
ldb,  
*                          info  
)  
```  
  
DTRTRS solves a triangular system of the form  
  
A * X = B  or  A**T * X = B,  
  
where A is a triangular matrix of order N, and B is an N-by-NRHS matrix.  
  
This subroutine verifies that A is nonsingular, but callers should note that only exact  
singularity is detected. It is conceivable for one or more diagonal elements of A to be  
subnormally tiny numbers without this subroutine signalling an error.  
  
If a possible loss of numerical precision due to near-singular matrices is a concern, the  
caller should verify that A is nonsingular within some tolerance before calling this subroutine.  
  
## Parameters  
Uplo : Character*1 [in]  
> = 'U':  A is upper triangular;  
> = 'L':  A is lower triangular.  
  
Trans : Character*1 [in]  
> Specifies the form of the system of equations:  
  
Diag : Character*1 [in]  
> = 'N':  A is non-unit triangular;  
> = 'U':  A is unit triangular.  
  
N : Integer [in]  
> The order of the matrix A.  N >= 0.  
  
Nrhs : Integer [in]  
> The number of right hand sides, i.e., the number of columns  
> of the matrix B.  NRHS >= 0.  
  
A : Double Precision Array, Dimension (lda,n) [in]  
> The triangular matrix A.  If UPLO = 'U', the leading N-by-N  
> upper triangular part of the array A contains the upper  
> triangular matrix, and the strictly lower triangular part of  
> A is not referenced.  If UPLO = 'L', the leading N-by-N lower  
> triangular part of the array A contains the lower triangular  
> matrix, and the strictly upper triangular part of A is not  
> referenced.  If DIAG = 'U', the diagonal elements of A are  
> also not referenced and are assumed to be 1.  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,N).  
  
B : Double Precision Array, Dimension (ldb,nrhs) [in,out]  
> On entry, the right hand side matrix B.  
> On exit, if INFO = 0, the solution matrix X.  
  
Ldb : Integer [in]  
> The leading dimension of the array B.  LDB >= max(1,N).  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0: if INFO = -i, the i-th argument had an illegal value  
> > 0:  if INFO = i, the i-th diagonal element of A is exactly zero,  
> indicating that the matrix is singular and the solutions  
> X have not been computed.  
  
