```fortran  
subroutine csysv_aa_2stage (  
uplo,  
n,  
nrhs,  
a,  
lda,  
tb,  
ltb,  
*                                  ipiv,  
ipiv2,  
b,  
ldb,  
work,  
lwork,  
*                                  info  
)  
```  
  
CSYSV_AA_2STAGE computes the solution to a complex system of  
linear equations  
A * X = B,  
where A is an N-by-N symmetric matrix and X and B are N-by-NRHS  
matrices.  
  
Aasen's 2-stage algorithm is used to factor A as  
A = U**T * T * U,  if UPLO = 'U', or  
A = L * T * L**T,  if UPLO = 'L',  
where U (or L) is a product of permutation and unit upper (lower)  
triangular matrices, and T is symmetric and band. The matrix T is  
then LU-factored with partial pivoting. The factored form of A  
is then used to solve the system of equations A * X = B.  
  
This is the blocked version of the algorithm, calling Level 3 BLAS.  
  
## Parameters  
Uplo : Character*1 [in]  
> = 'U':  Upper triangle of A is stored;  
> = 'L':  Lower triangle of A is stored.  
  
N : Integer [in]  
> The order of the matrix A.  N >= 0.  
  
Nrhs : Integer [in]  
> The number of right hand sides, i.e., the number of columns  
> of the matrix B.  NRHS >= 0.  
  
A : Complex Array, Dimension (lda,n) [in,out]  
> On entry, the symmetric matrix A.  If UPLO = 'U', the leading  
> N-by-N upper triangular part of A contains the upper  
> triangular part of the matrix A, and the strictly lower  
> triangular part of A is not referenced.  If UPLO = 'L', the  
> leading N-by-N lower triangular part of A contains the lower  
> triangular part of the matrix A, and the strictly upper  
> triangular part of A is not referenced.  
> On exit, L is stored below (or above) the subdiagonal blocks,  
> when UPLO  is 'L' (or 'U').  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,N).  
  
Tb : Complex Array, Dimension (ltb) [out]  
> On exit, details of the LU factorization of the band matrix.  
  
Ltb : Integer [in]  
> If LTB = -1, then a workspace query is assumed; the  
> routine only calculates the optimal size of LTB,  
> returns this value as the first entry of TB, and  
> no error message related to LTB is issued by XERBLA.  
  
Ipiv : Integer Array, Dimension (n) [out]  
> On exit, it contains the details of the interchanges, i.e.,  
> the row and column k of A were interchanged with the  
> row and column IPIV(k).  
  
Ipiv2 : Integer Array, Dimension (n) [out]  
> On exit, it contains the details of the interchanges, i.e.,  
> the row and column k of T were interchanged with the  
> row and column IPIV(k).  
  
B : Complex Array, Dimension (ldb,nrhs) [in,out]  
> On entry, the right hand side matrix B.  
> On exit, the solution matrix X.  
  
Ldb : Integer [in]  
> The leading dimension of the array B.  LDB >= max(1,N).  
  
Work : Complex Workspace of Size Lwork [out]  
  
Lwork : Integer [in]  
> The size of WORK. LWORK >= N, internally used to select NB  
> If LWORK = -1, then a workspace query is assumed; the  
> routine only calculates the optimal size of the WORK array,  
> returns this value as the first entry of the WORK array, and  
> no error message related to LWORK is issued by XERBLA.  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value.  
> > 0:  if INFO = i, band LU factorization failed on i-th column  
  
