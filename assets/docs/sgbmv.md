```fortran  
subroutine sgbmv (  
character trans,  
integer m,  
integer n,  
integer kl,  
integer ku,  
real alpha,  
real, dimension(lda,*) a,  
integer lda,  
real, dimension(*) x,  
integer incx,  
real beta,  
real, dimension(*) y,  
integer incy  
)  
```  
  
SGBMV  performs one of the matrix-vector operations  
  
y := alpha*A*x + beta*y,   or   y := alpha*A**T*x + beta*y,  
  
where alpha and beta are scalars, x and y are vectors and A is an  
m by n band matrix, with kl sub-diagonals and ku super-diagonals.  
  
## Parameters  
Trans : Character*1 [in]  
> On entry, TRANS specifies the operation to be performed as  
> follows:  
  
M : Integer [in]  
> On entry, M specifies the number of rows of the matrix A.  
> M must be at least zero.  
  
N : Integer [in]  
> On entry, N specifies the number of columns of the matrix A.  
> N must be at least zero.  
  
Kl : Integer [in]  
> On entry, KL specifies the number of sub-diagonals of the  
> matrix A. KL must satisfy  0 .le. KL.  
  
Ku : Integer [in]  
> On entry, KU specifies the number of super-diagonals of the  
> matrix A. KU must satisfy  0 .le. KU.  
  
Alpha : Real [in]  
> On entry, ALPHA specifies the scalar alpha.  
  
A : Real Array, Dimension ( Lda, N ) [in]  
> Before entry, the leading ( kl + ku + 1 ) by n part of the  
> array A must contain the matrix of coefficients, supplied  
> column by column, with the leading diagonal of the matrix in  
> row ( ku + 1 ) of the array, the first super-diagonal  
> starting at position 2 in row ku, the first sub-diagonal  
> starting at position 1 in row ( ku + 2 ), and so on.  
> Elements in the array A that do not correspond to elements  
> in the band matrix (such as the top left ku by ku triangle)  
> are not referenced.  
> The following program segment will transfer a band matrix  
> from conventional full matrix storage to band storage:  
> DO 20, J = 1, N  
> K = KU + 1 - J  
> DO 10, I = MAX( 1, J - KU ), MIN( M, J + KL )  
> A( K + I, J ) = matrix( I, J )  
> 10    CONTINUE  
> 20 CONTINUE  
  
Lda : Integer [in]  
> On entry, LDA specifies the first dimension of A as declared  
> in the calling (sub) program. LDA must be at least  
> ( kl + ku + 1 ).  
  
X : Real Array, Dimension At Least [in]  
> and at least  
> Before entry, the incremented array X must contain the  
> vector x.  
  
Incx : Integer [in]  
> On entry, INCX specifies the increment for the elements of  
> X. INCX must not be zero.  
  
Beta : Real [in]  
> On entry, BETA specifies the scalar beta. When BETA is  
> supplied as zero then Y need not be set on input.  
  
Y : Real Array, Dimension At Least [in,out]  
> and at least  
> Before entry, the incremented array Y must contain the  
> vector y. On exit, Y is overwritten by the updated vector y.  
> If either m or n is zero, then Y not referenced and the function  
> performs a quick return.  
  
Incy : Integer [in]  
> On entry, INCY specifies the increment for the elements of  
> Y. INCY must not be zero.  
  
