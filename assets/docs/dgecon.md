```fortran  
subroutine dgecon (  
norm,  
n,  
a,  
lda,  
anorm,  
rcond,  
work,  
iwork,  
*                          info  
)  
```  
  
DGECON estimates the reciprocal of the condition number of a general  
real matrix A, in either the 1-norm or the infinity-norm, using  
the LU factorization computed by DGETRF.  
  
An estimate is obtained for norm(inv(A)), and the reciprocal of the  
condition number is computed as  
RCOND = 1 / ( norm(A) * norm(inv(A)) ).  
  
## Parameters  
Norm : Character*1 [in]  
> Specifies whether the 1-norm condition number or the  
> infinity-norm condition number is required:  
> = '1' or 'O':  1-norm;  
> = 'I':         Infinity-norm.  
  
N : Integer [in]  
> The order of the matrix A.  N >= 0.  
  
A : Double Precision Array, Dimension (lda,n) [in]  
> as computed by DGETRF.  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,N).  
  
Anorm : Double Precision [in]  
> If NORM = '1' or 'O', the 1-norm of the original matrix A.  
> If NORM = 'I', the infinity-norm of the original matrix A.  
  
Rcond : Double Precision [out]  
> The reciprocal of the condition number of the matrix A,  
  
Work : Double Precision Array, Dimension (4*n) [out]  
  
Iwork : Integer Array, Dimension (n) [out]  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value.  
> NaNs are illegal values for ANORM, and they propagate to  
> the output parameter RCOND.  
> Infinity is illegal for ANORM, and it propagates to the output  
> parameter RCOND as 0.  
> = 1:  if RCOND = NaN, or  
> RCOND = Inf, or  
> the computed norm of the inverse of A is 0.  
> In the latter, RCOND = 0 is returned.  
  
