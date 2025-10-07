```fortran  
subroutine zhetrs_aa (  
uplo,  
n,  
nrhs,  
a,  
lda,  
ipiv,  
b,  
ldb,  
*                             work,  
lwork,  
info  
)  
```  
  
ZHETRS_AA solves a system of linear equations A*X = B with a complex  
hermitian matrix A using the factorization A = U**H*T*U or  
A = L*T*L**H computed by ZHETRF_AA.  
  
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
> Details of factors computed by ZHETRF_AA.  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,N).  
  
Ipiv : Integer Array, Dimension (n) [in]  
> Details of the interchanges as computed by ZHETRF_AA.  
  
B : Complex*16 Array, Dimension (ldb,nrhs) [in,out]  
> On entry, the right hand side matrix B.  
> On exit, the solution matrix X.  
  
Ldb : Integer [in]  
> The leading dimension of the array B.  LDB >= max(1,N).  
  
Work : Complex*16 Array, Dimension (max(1,lwork)) [out]  
  
Lwork : Integer [in]  
> The dimension of the array WORK.  
> If LWORK = -1, then a workspace query is assumed; the routine  
> only calculates the minimal size of the WORK array, returns  
> this value as the first entry of the WORK array, and no error  
> message related to LWORK is issued by XERBLA.  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
  
