```fortran  
subroutine cpocon (  
uplo,  
n,  
a,  
lda,  
anorm,  
rcond,  
work,  
rwork,  
*                          info  
)  
```  
  
CPOCON estimates the reciprocal of the condition number (in the  
1-norm) of a complex Hermitian positive definite matrix using the  
Cholesky factorization A = U**H*U or A = L*L**H computed by CPOTRF.  
  
An estimate is obtained for norm(inv(A)), and the reciprocal of the  
condition number is computed as RCOND = 1 / (ANORM * norm(inv(A))).  
  
## Parameters  
Uplo : Character*1 [in]  
> = 'U':  Upper triangle of A is stored;  
> = 'L':  Lower triangle of A is stored.  
  
N : Integer [in]  
> The order of the matrix A.  N >= 0.  
  
A : Complex Array, Dimension (lda,n) [in]  
> The triangular factor U or L from the Cholesky factorization  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,N).  
  
Anorm : Real [in]  
> The 1-norm (or infinity-norm) of the Hermitian matrix A.  
  
Rcond : Real [out]  
> The reciprocal of the condition number of the matrix A,  
> estimate of the 1-norm of inv(A) computed in this routine.  
  
Work : Complex Array, Dimension (2*n) [out]  
  
Rwork : Real Array, Dimension (n) [out]  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
  
