```fortran  
subroutine ztrcon (  
norm,  
uplo,  
diag,  
n,  
a,  
lda,  
rcond,  
work,  
*                          rwork,  
info  
)  
```  
  
ZTRCON estimates the reciprocal of the condition number of a  
triangular matrix A, in either the 1-norm or the infinity-norm.  
  
The norm of A is computed and an estimate is obtained for  
norm(inv(A)), then the reciprocal of the condition number is  
computed as  
RCOND = 1 / ( norm(A) * norm(inv(A)) ).  
  
## Parameters  
Norm : Character*1 [in]  
> Specifies whether the 1-norm condition number or the  
> infinity-norm condition number is required:  
> = '1' or 'O':  1-norm;  
> = 'I':         Infinity-norm.  
  
Uplo : Character*1 [in]  
> = 'U':  A is upper triangular;  
> = 'L':  A is lower triangular.  
  
Diag : Character*1 [in]  
> = 'N':  A is non-unit triangular;  
> = 'U':  A is unit triangular.  
  
N : Integer [in]  
> The order of the matrix A.  N >= 0.  
  
A : Complex*16 Array, Dimension (lda,n) [in]  
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
  
Rcond : Double Precision [out]  
> The reciprocal of the condition number of the matrix A,  
  
Work : Complex*16 Array, Dimension (2*n) [out]  
  
Rwork : Double Precision Array, Dimension (n) [out]  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
  
