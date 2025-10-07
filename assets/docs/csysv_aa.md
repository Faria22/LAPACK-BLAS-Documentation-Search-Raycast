```fortran  
subroutine csysv_aa (  
uplo,  
n,  
nrhs,  
a,  
lda,  
ipiv,  
b,  
ldb,  
work,  
*                            lwork,  
info  
)  
```  
  
CSYSV computes the solution to a complex system of linear equations  
A * X = B,  
where A is an N-by-N symmetric matrix and X and B are N-by-NRHS  
matrices.  
  
Aasen's algorithm is used to factor A as  
A = U**T * T * U,  if UPLO = 'U', or  
A = L * T * L**T,  if UPLO = 'L',  
where U (or L) is a product of permutation and unit upper (lower)  
triangular matrices, and T is symmetric tridiagonal. The factored  
form of A is then used to solve the system of equations A * X = B.  
  
## Parameters  
Uplo : Character*1 [in]  
> = 'U':  Upper triangle of A is stored;  
> = 'L':  Lower triangle of A is stored.  
  
N : Integer [in]  
> The number of linear equations, i.e., the order of the  
> matrix A.  N >= 0.  
  
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
> On exit, if INFO = 0, the tridiagonal matrix T and the  
> multipliers used to obtain the factor U or L from the  
> CSYTRF.  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,N).  
  
Ipiv : Integer Array, Dimension (n) [out]  
> On exit, it contains the details of the interchanges, i.e.,  
> the row and column k of A were interchanged with the  
> row and column IPIV(k).  
  
B : Complex Array, Dimension (ldb,nrhs) [in,out]  
> On entry, the N-by-NRHS right hand side matrix B.  
> On exit, if INFO = 0, the N-by-NRHS solution matrix X.  
  
Ldb : Integer [in]  
> The leading dimension of the array B.  LDB >= max(1,N).  
  
Work : Complex Array, Dimension (max(1,lwork)) [out]  
> On exit, if INFO = 0, WORK(1) returns the optimal LWORK.  
  
Lwork : Integer [in]  
> the optimal blocksize for CSYTRF_AA.  
> If LWORK = -1, then a workspace query is assumed; the routine  
> only calculates the optimal size of the WORK array, returns  
> this value as the first entry of the WORK array, and no error  
> message related to LWORK is issued by XERBLA.  
  
Info : Integer [out]  
> = 0: successful exit  
> < 0: if INFO = -i, the i-th argument had an illegal value  
> > 0: if INFO = i, D(i,i) is exactly zero.  The factorization  
> has been completed, but the block diagonal matrix D is  
> exactly singular, so the solution could not be computed.  
  
