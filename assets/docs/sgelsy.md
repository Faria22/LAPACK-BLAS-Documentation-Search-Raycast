```fortran  
subroutine sgelsy (  
m,  
n,  
nrhs,  
a,  
lda,  
b,  
ldb,  
jpvt,  
rcond,  
rank,  
*                          work,  
lwork,  
info  
)  
```  
  
SGELSY computes the minimum-norm solution to a real linear least  
squares problem:  
minimize || A * X - B ||  
using a complete orthogonal factorization of A.  A is an M-by-N  
matrix which may be rank-deficient.  
  
Several right hand side vectors b and solution vectors x can be  
handled in a single call; they are stored as the columns of the  
M-by-NRHS right hand side matrix B and the N-by-NRHS solution  
matrix X.  
  
The routine first computes a QR factorization with column pivoting:  
A * P = Q * [ R11 R12 ]  
[  0  R22 ]  
with R11 defined as the largest leading submatrix whose estimated  
condition number is less than 1/RCOND.  The order of R11, RANK,  
is the effective rank of A.  
  
Then, R22 is considered to be negligible, and R12 is annihilated  
by orthogonal transformations from the right, arriving at the  
complete orthogonal factorization:  
A * P = Q * [ T11 0 ] * Z  
[  0  0 ]  
The minimum-norm solution is then  
X = P * Z**T [ inv(T11)*Q1**T*B ]  
[        0         ]  
where Q1 consists of the first RANK columns of Q.  
  
This routine is basically identical to the original xGELSX except  
three differences:  
o The call to the subroutine xGEQPF has been substituted by the  
the call to the subroutine xGEQP3. This subroutine is a Blas-3  
version of the QR factorization with column pivoting.  
o Matrix B (the right hand side) is updated with Blas-3.  
o The permutation of matrix B (the right hand side) is faster and  
more simple.  
  
## Parameters  
M : Integer [in]  
> The number of rows of the matrix A.  M >= 0.  
  
N : Integer [in]  
> The number of columns of the matrix A.  N >= 0.  
  
Nrhs : Integer [in]  
> The number of right hand sides, i.e., the number of  
> columns of matrices B and X. NRHS >= 0.  
  
A : Real Array, Dimension (lda,n) [in,out]  
> On entry, the M-by-N matrix A.  
> On exit, A has been overwritten by details of its  
> complete orthogonal factorization.  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,M).  
  
B : Real Array, Dimension (ldb,nrhs) [in,out]  
> On entry, the M-by-NRHS right hand side matrix B.  
> On exit, the N-by-NRHS solution matrix X.  
> If M = 0 or N = 0, B is not referenced.  
  
Ldb : Integer [in]  
> The leading dimension of the array B. LDB >= max(1,M,N).  
  
Jpvt : Integer Array, Dimension (n) [in,out]  
> On entry, if JPVT(i) .ne. 0, the i-th column of A is permuted  
> to the front of AP, otherwise column i is a free column.  
> On exit, if JPVT(i) = k, then the i-th column of AP  
> was the k-th column of A.  
  
Rcond : Real [in]  
> RCOND is used to determine the effective rank of A, which  
> is defined as the order of the largest leading triangular  
> submatrix R11 in the QR factorization with pivoting of A,  
> whose estimated condition number < 1/RCOND.  
  
Rank : Integer [out]  
> The effective rank of A, i.e., the order of the submatrix  
> R11.  This is the same as the order of the submatrix T11  
> in the complete orthogonal factorization of A.  
> If NRHS = 0, RANK = 0 on output.  
  
Work : Real Array, Dimension (max(1,lwork)) [out]  
> On exit, if INFO = 0, WORK(1) returns the optimal LWORK.  
  
Lwork : Integer [in]  
> The dimension of the array WORK.  
> The unblocked strategy requires that:  
> where MN = min( M, N ).  
> The block algorithm requires that:  
> where NB is an upper bound on the blocksize returned  
> by ILAENV for the routines SGEQP3, STZRZF, STZRQF, SORMQR,  
> and SORMRZ.  
> If LWORK = -1, then a workspace query is assumed; the routine  
> only calculates the optimal size of the WORK array, returns  
> this value as the first entry of the WORK array, and no error  
> message related to LWORK is issued by XERBLA.  
  
Info : Integer [out]  
> = 0: successful exit  
> < 0: If INFO = -i, the i-th argument had an illegal value.  
  
