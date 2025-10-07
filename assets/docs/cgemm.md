```fortran  
subroutine cgemm (  
character transa,  
character transb,  
integer m,  
integer n,  
integer k,  
complex alpha,  
complex, dimension(lda,*) a,  
integer lda,  
complex, dimension(ldb,*) b,  
integer ldb,  
complex beta,  
complex, dimension(ldc,*) c,  
integer ldc  
)  
```  
  
CGEMM  performs one of the matrix-matrix operations  
  
C := alpha*op( A )*op( B ) + beta*C,  
  
where  op( X ) is one of  
  
op( X ) = X   or   op( X ) = X**T   or   op( X ) = X**H,  
  
alpha and beta are scalars, and A, B and C are matrices, with op( A )  
an m by k matrix,  op( B )  a  k by n matrix and  C an m by n matrix.  
  
Note: if alpha and/or beta is zero, some parts of the matrix-matrix  
operations are not performed. This results in the following NaN/Inf  
propagation quirks:  
  
1. If alpha is zero, NaNs or Infs in A or B do not affect the result.  
2. If both alpha and beta are zero, then a zero matrix is returned in C,  
irrespective of any NaNs or Infs in A, B or C.  
3. If only beta is zero, alpha*op( A )*op( B ) is returned, irrespective  
of any NaNs or Infs in C.  
  
## Parameters  
Transa : Character*1 [in]  
> On entry, TRANSA specifies the form of op( A ) to be used in  
> the matrix multiplication as follows:  
> TRANSA = 'N' or 'n',  op( A ) = A.  
  
Transb : Character*1 [in]  
> On entry, TRANSB specifies the form of op( B ) to be used in  
> the matrix multiplication as follows:  
> TRANSB = 'N' or 'n',  op( B ) = B.  
  
M : Integer [in]  
> On entry,  M  specifies  the number  of rows  of the  matrix  
> op( A )  and of the  matrix  C.  M  must  be at least  zero.  
  
N : Integer [in]  
> On entry,  N  specifies the number  of columns of the matrix  
> op( B ) and the number of columns of the matrix C. N must be  
> at least zero.  
  
K : Integer [in]  
> On entry,  K  specifies  the number of columns of the matrix  
> op( A ) and the number of rows of the matrix op( B ). K must  
> be at least  zero.  
  
Alpha : Complex [in]  
> On entry, ALPHA specifies the scalar alpha. If ALPHA is zero the  
> values in A and B do not affect the result. This also means that  
> NaN/Inf propagation from A and B is inhibited if ALPHA is zero.  
  
A : Complex Array, Dimension ( Lda, Ka ), Where Ka is [in]  
> k  when  TRANSA = 'N' or 'n',  and is  m  otherwise.  
> Before entry with  TRANSA = 'N' or 'n',  the leading  m by k  
> part of the array  A  must contain the matrix  A,  otherwise  
> the leading  k by m  part of the array  A  must contain  the  
> matrix A, except if ALPHA is zero.  
> If ALPHA is zero, none of the values in A affect the result, even  
> if they are NaN/Inf. This also implies that if ALPHA is zero,  
> the matrix elements of A need not be initialized by the caller.  
  
Lda : Integer [in]  
> On entry, LDA specifies the first dimension of A as declared  
> in the calling (sub) program. When  TRANSA = 'N' or 'n' then  
> LDA must be at least  max( 1, m ), otherwise  LDA must be at  
> least  max( 1, k ).  
  
B : Complex Array, Dimension ( Ldb, Kb ), Where Kb is [in]  
> n  when  TRANSB = 'N' or 'n',  and is  k  otherwise.  
> Before entry with  TRANSB = 'N' or 'n',  the leading  k by n  
> part of the array  B  must contain the matrix  B,  otherwise  
> the leading  n by k  part of the array  B  must contain  the  
> matrix B, except if ALPHA is zero.  
> If ALPHA is zero, none of the values in B affect the result, even  
> if they are NaN/Inf. This also implies that if ALPHA is zero,  
> the matrix elements of B need not be initialized by the caller.  
  
Ldb : Integer [in]  
> On entry, LDB specifies the first dimension of B as declared  
> in the calling (sub) program. When  TRANSB = 'N' or 'n' then  
> LDB must be at least  max( 1, k ), otherwise  LDB must be at  
> least  max( 1, n ).  
  
Beta : Complex [in]  
> On entry,  BETA  specifies the scalar  beta. If BETA is zero the  
> values in C do not affect the result. This also means that  
> NaN/Inf propagation from C is inhibited if BETA is zero.  
  
C : Complex Array, Dimension ( Ldc, N ) [in,out]  
> Before entry, the leading  m by n  part of the array  C must  
> contain the matrix  C, except if beta is zero.  
> If beta is zero, none of the values in C affect the result, even  
> if they are NaN/Inf. This also implies that if beta is zero,  
> the matrix elements of C need not be initialized by the caller.  
> On exit, the array  C  is overwritten by the  m by n  matrix  
  
Ldc : Integer [in]  
> On entry, LDC specifies the first dimension of C as declared  
> in  the  calling  (sub)  program.   LDC  must  be  at  least  
> max( 1, m ).  
  
