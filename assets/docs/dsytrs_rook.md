```fortran  
subroutine dsytrs_rook (  
character uplo,  
integer n,  
integer nrhs,  
double precision, dimension(lda, *) a,  
integer lda,  
integer, dimension(*) ipiv,  
double precision, dimension(ldb, *) b,  
integer ldb,  
integer info  
)  
```  
  
DSYTRS_ROOK solves a system of linear equations A*X = B with  
a real symmetric matrix A using the factorization A = U*D*U**T or  
A = L*D*L**T computed by DSYTRF_ROOK.  
  
## Parameters  
Uplo : Character*1 [in]  
> Specifies whether the details of the factorization are stored  
> as an upper or lower triangular matrix.  
  
N : Integer [in]  
> The order of the matrix A.  N >= 0.  
  
Nrhs : Integer [in]  
> The number of right hand sides, i.e., the number of columns  
> of the matrix B.  NRHS >= 0.  
  
A : Double Precision Array, Dimension (lda,n) [in]  
> The block diagonal matrix D and the multipliers used to  
> obtain the factor U or L as computed by DSYTRF_ROOK.  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,N).  
  
Ipiv : Integer Array, Dimension (n) [in]  
> Details of the interchanges and the block structure of D  
> as determined by DSYTRF_ROOK.  
  
B : Double Precision Array, Dimension (ldb,nrhs) [in,out]  
> On entry, the right hand side matrix B.  
> On exit, the solution matrix X.  
  
Ldb : Integer [in]  
> The leading dimension of the array B.  LDB >= max(1,N).  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
  
