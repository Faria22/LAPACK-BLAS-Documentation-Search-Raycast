```fortran  
subroutine zhetrs_aa_2stage (  
uplo,  
n,  
nrhs,  
a,  
lda,  
tb,  
ltb,  
ipiv,  
*                                   ipiv2,  
b,  
ldb,  
info  
)  
```  
  
ZHETRS_AA_2STAGE solves a system of linear equations A*X = B with a  
hermitian matrix A using the factorization A = U**H*T*U or  
A = L*T*L**H computed by ZHETRF_AA_2STAGE.  
  
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
> Details of factors computed by ZHETRF_AA_2STAGE.  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,N).  
  
Tb : Complex*16 Array, Dimension (ltb) [out]  
> Details of factors computed by ZHETRF_AA_2STAGE.  
  
Ltb : Integer [in]  
  
Ipiv : Integer Array, Dimension (n) [in]  
> Details of the interchanges as computed by  
> ZHETRF_AA_2STAGE.  
  
Ipiv2 : Integer Array, Dimension (n) [in]  
> Details of the interchanges as computed by  
> ZHETRF_AA_2STAGE.  
  
B : Complex*16 Array, Dimension (ldb,nrhs) [in,out]  
> On entry, the right hand side matrix B.  
> On exit, the solution matrix X.  
  
Ldb : Integer [in]  
> The leading dimension of the array B.  LDB >= max(1,N).  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
  
