```fortran  
subroutine ssfrk (  
transr,  
uplo,  
trans,  
n,  
k,  
alpha,  
a,  
lda,  
beta,  
*                         c  
)  
```  
  
Level 3 BLAS like routine for C in RFP Format.  
  
SSFRK performs one of the symmetric rank--k operations  
  
C := alpha*A*A**T + beta*C,  
  
or  
  
C := alpha*A**T*A + beta*C,  
  
where alpha and beta are real scalars, C is an n--by--n symmetric  
matrix and A is an n--by--k matrix in the first case and a k--by--n  
matrix in the second case.  
  
## Parameters  
Transr : Character*1 [in]  
> = 'N':  The Normal Form of RFP A is stored;  
> = 'T':  The Transpose Form of RFP A is stored.  
  
Uplo : Character*1 [in]  
> On  entry, UPLO specifies whether the upper or lower  
> triangular part of the array C is to be referenced as  
> follows:  
> UPLO = 'U' or 'u'   Only the upper triangular part of C  
> is to be referenced.  
> UPLO = 'L' or 'l'   Only the lower triangular part of C  
> is to be referenced.  
> Unchanged on exit.  
  
Trans : Character*1 [in]  
> On entry, TRANS specifies the operation to be performed as  
> follows:  
> Unchanged on exit.  
  
N : Integer [in]  
> On entry, N specifies the order of the matrix C. N must be  
> at least zero.  
> Unchanged on exit.  
  
K : Integer [in]  
> On entry with TRANS = 'N' or 'n', K specifies the number  
> of  columns of the matrix A, and on entry with TRANS = 'T'  
> or 't', K specifies the number of rows of the matrix A. K  
> must be at least zero.  
> Unchanged on exit.  
  
Alpha : Real [in]  
> On entry, ALPHA specifies the scalar alpha.  
> Unchanged on exit.  
  
A : Real Array, Dimension (lda,ka) [in]  
> where KA  
> is K  when TRANS = 'N' or 'n', and is N otherwise. Before  
> entry with TRANS = 'N' or 'n', the leading N--by--K part of  
> the array A must contain the matrix A, otherwise the leading  
> K--by--N part of the array A must contain the matrix A.  
> Unchanged on exit.  
  
Lda : Integer [in]  
> On entry, LDA specifies the first dimension of A as declared  
> in  the  calling  (sub)  program.   When  TRANS = 'N' or 'n'  
> then  LDA must be at least  max( 1, n ), otherwise  LDA must  
> be at least  max( 1, k ).  
> Unchanged on exit.  
  
Beta : Real [in]  
> On entry, BETA specifies the scalar beta.  
> Unchanged on exit.  
  
C : Real Array, Dimension (nt) [in,out]  
> Format. RFP Format is described by TRANSR, UPLO and N.  
  
