```fortran  
subroutine dgels (  
trans,  
m,  
n,  
nrhs,  
a,  
lda,  
b,  
ldb,  
work,  
lwork,  
*                         info  
)  
```  
  
DGELS solves overdetermined or underdetermined real linear systems  
involving an M-by-N matrix A, or its transpose, using a QR or LQ  
factorization of A.  
  
It is assumed that A has full rank, and only a rudimentary protection  
against rank-deficient matrices is provided. This subroutine only detects  
exact rank-deficiency, where a diagonal element of the triangular factor  
of A is exactly zero.  
  
It is conceivable for one (or more) of the diagonal elements of the triangular  
factor of A to be subnormally tiny numbers without this subroutine signalling  
an error. The solutions computed for such almost-rank-deficient matrices may  
be less accurate due to a loss of numerical precision.  
  
The following options are provided:  
  
1. If TRANS = 'N' and m >= n:  find the least squares solution of  
an overdetermined system, i.e., solve the least squares problem  
minimize || B - A*X ||.  
  
2. If TRANS = 'N' and m < n:  find the minimum norm solution of  
an underdetermined system A * X = B.  
  
3. If TRANS = 'T' and m >= n:  find the minimum norm solution of  
an underdetermined system A**T * X = B.  
  
4. If TRANS = 'T' and m < n:  find the least squares solution of  
an overdetermined system, i.e., solve the least squares problem  
minimize || B - A**T * X ||.  
  
Several right hand side vectors b and solution vectors x can be  
handled in a single call; they are stored as the columns of the  
M-by-NRHS right hand side matrix B and the N-by-NRHS solution  
matrix X.  
  
## Parameters  
Trans : Character*1 [in]  
> = 'N': the linear system involves A;  
  
M : Integer [in]  
> The number of rows of the matrix A.  M >= 0.  
  
N : Integer [in]  
> The number of columns of the matrix A.  N >= 0.  
  
Nrhs : Integer [in]  
> The number of right hand sides, i.e., the number of  
> columns of the matrices B and X. NRHS >=0.  
  
A : Double Precision Array, Dimension (lda,n) [in,out]  
> On entry, the M-by-N matrix A.  
> On exit,  
> if M >= N, A is overwritten by details of its QR  
> factorization as returned by DGEQRF;  
> if M <  N, A is overwritten by details of its LQ  
> factorization as returned by DGELQF.  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,M).  
  
B : Double Precision Array, Dimension (ldb,nrhs) [in,out]  
> On entry, the matrix B of right hand side vectors, stored  
> columnwise; B is M-by-NRHS if TRANS = 'N', or N-by-NRHS  
> if TRANS = 'T'.  
> On exit, if INFO = 0, B is overwritten by the solution  
> vectors, stored columnwise:  
> if TRANS = 'N' and m >= n, rows 1 to n of B contain the least  
> squares solution vectors; the residual sum of squares for the  
> solution in each column is given by the sum of squares of  
> elements N+1 to M in that column;  
> if TRANS = 'N' and m < n, rows 1 to N of B contain the  
> minimum norm solution vectors;  
> if TRANS = 'T' and m >= n, rows 1 to M of B contain the  
> minimum norm solution vectors;  
> if TRANS = 'T' and m < n, rows 1 to M of B contain the  
> least squares solution vectors; the residual sum of squares  
> for the solution in each column is given by the sum of  
> squares of elements M+1 to N in that column.  
  
Ldb : Integer [in]  
> The leading dimension of the array B. LDB >= MAX(1,M,N).  
  
Work : Double Precision Array, Dimension (max(1,lwork)) [out]  
> On exit, if INFO = 0, WORK(1) returns the optimal LWORK.  
  
Lwork : Integer [in]  
> The dimension of the array WORK.  
> LWORK >= max( 1, MN + max( MN, NRHS ) ).  
> For optimal performance,  
> where MN = min(M,N) and NB is the optimum block size.  
> If LWORK = -1, then a workspace query is assumed; the routine  
> only calculates the optimal size of the WORK array, returns  
> this value as the first entry of the WORK array, and no error  
> message related to LWORK is issued by XERBLA.  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
> > 0:  if INFO =  i, the i-th diagonal element of the  
> triangular factor of A is exactly zero, so that A does not have  
> full rank; the least squares solution could not be  
> computed.  
  
