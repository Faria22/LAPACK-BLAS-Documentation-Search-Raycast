```fortran  
subroutine cppcon (  
character uplo,  
integer n,  
complex, dimension(*) ap,  
real anorm,  
real rcond,  
complex, dimension(*) work,  
real, dimension(*) rwork,  
integer info  
)  
```  
  
CPPCON estimates the reciprocal of the condition number (in the  
1-norm) of a complex Hermitian positive definite packed matrix using  
the Cholesky factorization A = U**H*U or A = L*L**H computed by  
CPPTRF.  
  
An estimate is obtained for norm(inv(A)), and the reciprocal of the  
condition number is computed as RCOND = 1 / (ANORM * norm(inv(A))).  
  
## Parameters  
Uplo : Character*1 [in]  
> = 'U':  Upper triangle of A is stored;  
> = 'L':  Lower triangle of A is stored.  
  
N : Integer [in]  
> The order of the matrix A.  N >= 0.  
  
Ap : Complex Array, Dimension (n*(n+1)/2) [in]  
> The triangular factor U or L from the Cholesky factorization  
> array.  The j-th column of U or L is stored in the array AP  
> as follows:  
  
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
  
