```fortran  
subroutine dgtcon (  
norm,  
n,  
dl,  
d,  
du,  
du2,  
ipiv,  
anorm,  
rcond,  
*                          work,  
iwork,  
info  
)  
```  
  
DGTCON estimates the reciprocal of the condition number of a real  
tridiagonal matrix A using the LU factorization as computed by  
DGTTRF.  
  
An estimate is obtained for norm(inv(A)), and the reciprocal of the  
condition number is computed as RCOND = 1 / (ANORM * norm(inv(A))).  
  
## Parameters  
Norm : Character*1 [in]  
> Specifies whether the 1-norm condition number or the  
> infinity-norm condition number is required:  
> = '1' or 'O':  1-norm;  
> = 'I':         Infinity-norm.  
  
N : Integer [in]  
> The order of the matrix A.  N >= 0.  
  
Dl : Double Precision Array, Dimension (n-1) [in]  
> The (n-1) multipliers that define the matrix L from the  
> LU factorization of A as computed by DGTTRF.  
  
D : Double Precision Array, Dimension (n) [in]  
> The n diagonal elements of the upper triangular matrix U from  
> the LU factorization of A.  
  
Du : Double Precision Array, Dimension (n-1) [in]  
> The (n-1) elements of the first superdiagonal of U.  
  
Du2 : Double Precision Array, Dimension (n-2) [in]  
> The (n-2) elements of the second superdiagonal of U.  
  
Ipiv : Integer Array, Dimension (n) [in]  
> The pivot indices; for 1 <= i <= n, row i of the matrix was  
> interchanged with row IPIV(i).  IPIV(i) will always be either  
> i or i+1; IPIV(i) = i indicates a row interchange was not  
> required.  
  
Anorm : Double Precision [in]  
> If NORM = '1' or 'O', the 1-norm of the original matrix A.  
> If NORM = 'I', the infinity-norm of the original matrix A.  
  
Rcond : Double Precision [out]  
> The reciprocal of the condition number of the matrix A,  
> estimate of the 1-norm of inv(A) computed in this routine.  
  
Work : Double Precision Array, Dimension (2*n) [out]  
  
Iwork : Integer Array, Dimension (n) [out]  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
  
