```fortran  
subroutine sgemv (  
character trans,  
integer m,  
integer n,  
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
  
SGEMV  performs one of the matrix-vector operations  
  
y := alpha*A*x + beta*y,   or   y := alpha*A**T*x + beta*y,  
  
where alpha and beta are scalars, x and y are vectors and A is an  
m by n matrix.  
  
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
  
Alpha : Real [in]  
> On entry, ALPHA specifies the scalar alpha.  
  
A : Real Array, Dimension ( Lda, N ) [in]  
> Before entry, the leading m by n part of the array A must  
> contain the matrix of coefficients.  
  
Lda : Integer [in]  
> On entry, LDA specifies the first dimension of A as declared  
> in the calling (sub) program. LDA must be at least  
> max( 1, m ).  
  
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
> Before entry with BETA non-zero, the incremented array Y  
> must contain the vector y. On exit, Y is overwritten by the  
> updated vector y.  
> If either m or n is zero, then Y not referenced and the function  
> performs a quick return.  
  
Incy : Integer [in]  
> On entry, INCY specifies the increment for the elements of  
> Y. INCY must not be zero.  
  
