```fortran  
subroutine ctbcon (  
norm,  
uplo,  
diag,  
n,  
kd,  
ab,  
ldab,  
rcond,  
work,  
*                          rwork,  
info  
)  
```  
  
CTBCON estimates the reciprocal of the condition number of a  
triangular band matrix A, in either the 1-norm or the infinity-norm.  
  
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
  
Kd : Integer [in]  
> The number of superdiagonals or subdiagonals of the  
> triangular band matrix A.  KD >= 0.  
  
Ab : Complex Array, Dimension (ldab,n) [in]  
> The upper or lower triangular band matrix A, stored in the  
> first kd+1 rows of the array. The j-th column of A is stored  
> in the j-th column of the array AB as follows:  
> if UPLO = 'U', AB(kd+1+i-j,j) = A(i,j) for max(1,j-kd)<=i<=j;  
> if UPLO = 'L', AB(1+i-j,j)    = A(i,j) for j<=i<=min(n,j+kd).  
> If DIAG = 'U', the diagonal elements of A are not referenced  
> and are assumed to be 1.  
  
Ldab : Integer [in]  
> The leading dimension of the array AB.  LDAB >= KD+1.  
  
Rcond : Real [out]  
> The reciprocal of the condition number of the matrix A,  
  
Work : Complex Array, Dimension (2*n) [out]  
  
Rwork : Real Array, Dimension (n) [out]  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
  
