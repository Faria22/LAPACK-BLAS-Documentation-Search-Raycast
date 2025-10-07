```fortran  
subroutine zgelss (  
m,  
n,  
nrhs,  
a,  
lda,  
b,  
ldb,  
s,  
rcond,  
rank,  
*                          work,  
lwork,  
rwork,  
info  
)  
```  
  
ZGELSS computes the minimum norm solution to a complex linear  
least squares problem:  
  
Minimize 2-norm(| b - A*x |).  
  
using the singular value decomposition (SVD) of A. A is an M-by-N  
matrix which may be rank-deficient.  
  
Several right hand side vectors b and solution vectors x can be  
handled in a single call; they are stored as the columns of the  
M-by-NRHS right hand side matrix B and the N-by-NRHS solution matrix  
X.  
  
The effective rank of A is determined by treating as zero those  
singular values which are less than RCOND times the largest singular  
value.  
  
## Parameters  
M : Integer [in]  
> The number of rows of the matrix A. M >= 0.  
  
N : Integer [in]  
> The number of columns of the matrix A. N >= 0.  
  
Nrhs : Integer [in]  
> The number of right hand sides, i.e., the number of columns  
> of the matrices B and X. NRHS >= 0.  
  
A : Complex*16 Array, Dimension (lda,n) [in,out]  
> On entry, the M-by-N matrix A.  
> On exit, the first min(m,n) rows of A are overwritten with  
> its right singular vectors, stored rowwise.  
  
Lda : Integer [in]  
> The leading dimension of the array A. LDA >= max(1,M).  
  
B : Complex*16 Array, Dimension (ldb,nrhs) [in,out]  
> On entry, the M-by-NRHS right hand side matrix B.  
> On exit, B is overwritten by the N-by-NRHS solution matrix X.  
> If m >= n and RANK = n, the residual sum-of-squares for  
> the solution in the i-th column is given by the sum of  
> squares of the modulus of elements n+1:m in that column.  
  
Ldb : Integer [in]  
> The leading dimension of the array B.  LDB >= max(1,M,N).  
  
S : Double Precision Array, Dimension (min(m,n)) [out]  
> The singular values of A in decreasing order.  
> The condition number of A in the 2-norm = S(1)/S(min(m,n)).  
  
Rcond : Double Precision [in]  
> RCOND is used to determine the effective rank of A.  
> If RCOND < 0, machine precision is used instead.  
  
Rank : Integer [out]  
> The effective rank of A, i.e., the number of singular values  
  
Work : Complex*16 Array, Dimension (max(1,lwork)) [out]  
> On exit, if INFO = 0, WORK(1) returns the optimal LWORK.  
  
Lwork : Integer [in]  
> The dimension of the array WORK. LWORK >= 1, and also:  
> For good performance, LWORK should generally be larger.  
> If LWORK = -1, then a workspace query is assumed; the routine  
> only calculates the optimal size of the WORK array, returns  
> this value as the first entry of the WORK array, and no error  
> message related to LWORK is issued by XERBLA.  
  
Rwork : Double Precision Array, Dimension (5*min(m,n)) [out]  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value.  
> > 0:  the algorithm for computing the SVD failed to converge;  
> if INFO = i, i off-diagonal elements of an intermediate  
> bidiagonal form did not converge to zero.  
  
