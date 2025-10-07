```fortran  
subroutine sger (  
integer m,  
integer n,  
real alpha,  
real, dimension(*) x,  
integer incx,  
real, dimension(*) y,  
integer incy,  
real, dimension(lda,*) a,  
integer lda  
)  
```  
  
SGER   performs the rank 1 operation  
  
A := alpha*x*y**T + A,  
  
where alpha is a scalar, x is an m element vector, y is an n element  
vector and A is an m by n matrix.  
  
## Parameters  
M : Integer [in]  
> On entry, M specifies the number of rows of the matrix A.  
> M must be at least zero.  
  
N : Integer [in]  
> On entry, N specifies the number of columns of the matrix A.  
> N must be at least zero.  
  
Alpha : Real [in]  
> On entry, ALPHA specifies the scalar alpha.  
  
X : Real Array, Dimension At Least [in]  
> Before entry, the incremented array X must contain the m  
> element vector x.  
  
Incx : Integer [in]  
> On entry, INCX specifies the increment for the elements of  
> X. INCX must not be zero.  
  
Y : Real Array, Dimension At Least [in]  
> Before entry, the incremented array Y must contain the n  
> element vector y.  
  
Incy : Integer [in]  
> On entry, INCY specifies the increment for the elements of  
> Y. INCY must not be zero.  
  
A : Real Array, Dimension ( Lda, N ) [in,out]  
> Before entry, the leading m by n part of the array A must  
> contain the matrix of coefficients. On exit, A is  
> overwritten by the updated matrix.  
  
Lda : Integer [in]  
> On entry, LDA specifies the first dimension of A as declared  
> in the calling (sub) program. LDA must be at least  
> max( 1, m ).  
  
