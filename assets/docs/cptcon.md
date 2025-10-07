```fortran  
subroutine cptcon (  
integer n,  
real, dimension(*) d,  
complex, dimension(*) e,  
real anorm,  
real rcond,  
real, dimension(*) rwork,  
integer info  
)  
```  
  
CPTCON computes the reciprocal of the condition number (in the  
1-norm) of a complex Hermitian positive definite tridiagonal matrix  
using the factorization A = L*D*L**H or A = U**H*D*U computed by  
CPTTRF.  
  
Norm(inv(A)) is computed by a direct method, and the reciprocal of  
the condition number is computed as  
RCOND = 1 / (ANORM * norm(inv(A))).  
  
## Parameters  
N : Integer [in]  
> The order of the matrix A.  N >= 0.  
  
D : Real Array, Dimension (n) [in]  
> The n diagonal elements of the diagonal matrix D from the  
> factorization of A, as computed by CPTTRF.  
  
E : Complex Array, Dimension (n-1) [in]  
> The (n-1) off-diagonal elements of the unit bidiagonal factor  
> U or L from the factorization of A, as computed by CPTTRF.  
  
Anorm : Real [in]  
> The 1-norm of the original matrix A.  
  
Rcond : Real [out]  
> The reciprocal of the condition number of the matrix A,  
> 1-norm of inv(A) computed in this routine.  
  
Rwork : Real Array, Dimension (n) [out]  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
  
