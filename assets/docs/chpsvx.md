```fortran  
subroutine chpsvx (  
fact,  
uplo,  
n,  
nrhs,  
ap,  
afp,  
ipiv,  
b,  
ldb,  
x,  
*                          ldx,  
rcond,  
ferr,  
berr,  
work,  
rwork,  
info  
)  
```  
  
CHPSVX uses the diagonal pivoting factorization A = U*D*U**H or  
A = L*D*L**H to compute the solution to a complex system of linear  
equations A * X = B, where A is an N-by-N Hermitian matrix stored  
in packed format and X and B are N-by-NRHS matrices.  
  
Error bounds on the solution and a condition estimate are also  
provided.  
  
## Parameters  
Fact : Character*1 [in]  
> Specifies whether or not the factored form of A has been  
> supplied on entry.  
> = 'F':  On entry, AFP and IPIV contain the factored form of  
> A.  AFP and IPIV will not be modified.  
> = 'N':  The matrix A will be copied to AFP and factored.  
  
Uplo : Character*1 [in]  
> = 'U':  Upper triangle of A is stored;  
> = 'L':  Lower triangle of A is stored.  
  
N : Integer [in]  
> The number of linear equations, i.e., the order of the  
> matrix A.  N >= 0.  
  
Nrhs : Integer [in]  
> The number of right hand sides, i.e., the number of columns  
> of the matrices B and X.  NRHS >= 0.  
  
Ap : Complex Array, Dimension (n*(n+1)/2) [in]  
> The upper or lower triangle of the Hermitian matrix A, packed  
> columnwise in a linear array.  The j-th column of A is stored  
> in the array AP as follows:  
> See below for further details.  
  
Afp : Complex Array, Dimension (n*(n+1)/2) [in,out]  
> If FACT = 'F', then AFP is an input argument and on entry  
> contains the block diagonal matrix D and the multipliers used  
> to obtain the factor U or L from the factorization  
> a packed triangular matrix in the same storage format as A.  
> If FACT = 'N', then AFP is an output argument and on exit  
> contains the block diagonal matrix D and the multipliers used  
> to obtain the factor U or L from the factorization  
> a packed triangular matrix in the same storage format as A.  
  
Ipiv : Integer Array, Dimension (n) [in,out]  
> If FACT = 'F', then IPIV is an input argument and on entry  
> contains details of the interchanges and the block structure  
> of D, as determined by CHPTRF.  
> If IPIV(k) > 0, then rows and columns k and IPIV(k) were  
> interchanged and D(k,k) is a 1-by-1 diagonal block.  
> If UPLO = 'U' and IPIV(k) = IPIV(k-1) < 0, then rows and  
> columns k-1 and -IPIV(k) were interchanged and D(k-1:k,k-1:k)  
> is a 2-by-2 diagonal block.  If UPLO = 'L' and IPIV(k) =  
> IPIV(k+1) < 0, then rows and columns k+1 and -IPIV(k) were  
> interchanged and D(k:k+1,k:k+1) is a 2-by-2 diagonal block.  
> If FACT = 'N', then IPIV is an output argument and on exit  
> contains details of the interchanges and the block structure  
> of D, as determined by CHPTRF.  
  
B : Complex Array, Dimension (ldb,nrhs) [in]  
> The N-by-NRHS right hand side matrix B.  
  
Ldb : Integer [in]  
> The leading dimension of the array B.  LDB >= max(1,N).  
  
X : Complex Array, Dimension (ldx,nrhs) [out]  
> If INFO = 0 or INFO = N+1, the N-by-NRHS solution matrix X.  
  
Ldx : Integer [in]  
> The leading dimension of the array X.  LDX >= max(1,N).  
  
Rcond : Real [out]  
> The estimate of the reciprocal condition number of the matrix  
> A.  If RCOND is less than the machine precision (in  
> particular, if RCOND = 0), the matrix is singular to working  
> precision.  This condition is indicated by a return code of  
> INFO > 0.  
  
Ferr : Real Array, Dimension (nrhs) [out]  
> The estimated forward error bound for each solution vector  
> X(j) (the j-th column of the solution matrix X).  
> If XTRUE is the true solution corresponding to X(j), FERR(j)  
> is an estimated upper bound for the magnitude of the largest  
> element in (X(j) - XTRUE) divided by the magnitude of the  
> largest element in X(j).  The estimate is as reliable as  
> the estimate for RCOND, and is almost always a slight  
> overestimate of the true error.  
  
Berr : Real Array, Dimension (nrhs) [out]  
> The componentwise relative backward error of each solution  
> vector X(j) (i.e., the smallest relative change in  
> any element of A or B that makes X(j) an exact solution).  
  
Work : Complex Array, Dimension (2*n) [out]  
  
Rwork : Real Array, Dimension (n) [out]  
  
Info : Integer [out]  
> = 0: successful exit  
> < 0: if INFO = -i, the i-th argument had an illegal value  
> > 0:  if INFO = i, and i is  
> <= N:  D(i,i) is exactly zero.  The factorization  
> has been completed but the factor D is exactly  
> singular, so the solution and error bounds could  
> not be computed. RCOND = 0 is returned.  
> = N+1: D is nonsingular, but RCOND is less than machine  
> precision, meaning that the matrix is singular  
> to working precision.  Nevertheless, the  
> solution and error bounds are computed because  
> there are a number of situations where the  
> computed solution can be more accurate than the  
> value of RCOND would suggest.  
  
