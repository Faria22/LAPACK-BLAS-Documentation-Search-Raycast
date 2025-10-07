```fortran  
subroutine checon (  
uplo,  
n,  
a,  
lda,  
ipiv,  
anorm,  
rcond,  
work,  
*                          info  
)  
```  
  
CHECON estimates the reciprocal of the condition number of a complex  
Hermitian matrix A using the factorization A = U*D*U**H or  
A = L*D*L**H computed by CHETRF.  
  
An estimate is obtained for norm(inv(A)), and the reciprocal of the  
condition number is computed as RCOND = 1 / (ANORM * norm(inv(A))).  
  
## Parameters  
Uplo : Character*1 [in]  
> Specifies whether the details of the factorization are stored  
> as an upper or lower triangular matrix.  
  
N : Integer [in]  
> The order of the matrix A.  N >= 0.  
  
A : Complex Array, Dimension (lda,n) [in]  
> The block diagonal matrix D and the multipliers used to  
> obtain the factor U or L as computed by CHETRF.  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,N).  
  
Ipiv : Integer Array, Dimension (n) [in]  
> Details of the interchanges and the block structure of D  
> as determined by CHETRF.  
  
Anorm : Real [in]  
> The 1-norm of the original matrix A.  
  
Rcond : Real [out]  
> The reciprocal of the condition number of the matrix A,  
> estimate of the 1-norm of inv(A) computed in this routine.  
  
Work : Complex Array, Dimension (2*n) [out]  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
  
