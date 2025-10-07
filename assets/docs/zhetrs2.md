```fortran  
subroutine zhetrs2 (  
uplo,  
n,  
nrhs,  
a,  
lda,  
ipiv,  
b,  
ldb,  
*                           work,  
info  
)  
```  
  
ZHETRS2 solves a system of linear equations A*X = B with a complex  
Hermitian matrix A using the factorization A = U*D*U**H or  
A = L*D*L**H computed by ZHETRF and converted by ZSYCONV.  
  
## Parameters  
Uplo : Character*1 [in]  
> Specifies whether the details of the factorization are stored  
> as an upper or lower triangular matrix.  
  
N : Integer [in]  
> The order of the matrix A.  N >= 0.  
  
Nrhs : Integer [in]  
> The number of right hand sides, i.e., the number of columns  
> of the matrix B.  NRHS >= 0.  
  
A : Complex*16 Array, Dimension (lda,n) [in]  
> The block diagonal matrix D and the multipliers used to  
> obtain the factor U or L as computed by ZHETRF.  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,N).  
  
Ipiv : Integer Array, Dimension (n) [in]  
> Details of the interchanges and the block structure of D  
> as determined by ZHETRF.  
  
B : Complex*16 Array, Dimension (ldb,nrhs) [in,out]  
> On entry, the right hand side matrix B.  
> On exit, the solution matrix X.  
  
Ldb : Integer [in]  
> The leading dimension of the array B.  LDB >= max(1,N).  
  
Work : Complex*16 Array, Dimension (n) [out]  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
  
