```fortran  
subroutine ssymv (  
character uplo,  
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
  
SSYMV  performs the matrix-vector  operation  
  
y := alpha*A*x + beta*y,  
  
where alpha and beta are scalars, x and y are n element vectors and  
A is an n by n symmetric matrix.  
  
## Parameters  
Uplo : Character*1 [in]  
> On entry, UPLO specifies whether the upper or lower  
> triangular part of the array A is to be referenced as  
> follows:  
> UPLO = 'U' or 'u'   Only the upper triangular part of A  
> is to be referenced.  
> UPLO = 'L' or 'l'   Only the lower triangular part of A  
> is to be referenced.  
  
N : Integer [in]  
> On entry, N specifies the order of the matrix A.  
> N must be at least zero.  
  
Alpha : Real [in]  
> On entry, ALPHA specifies the scalar alpha.  
  
A : Real Array, Dimension ( Lda, N ) [in]  
> Before entry with  UPLO = 'U' or 'u', the leading n by n  
> upper triangular part of the array A must contain the upper  
> triangular part of the symmetric matrix and the strictly  
> lower triangular part of A is not referenced.  
> Before entry with UPLO = 'L' or 'l', the leading n by n  
> lower triangular part of the array A must contain the lower  
> triangular part of the symmetric matrix and the strictly  
> upper triangular part of A is not referenced.  
  
Lda : Integer [in]  
> On entry, LDA specifies the first dimension of A as declared  
> in the calling (sub) program. LDA must be at least  
> max( 1, n ).  
  
X : Real Array, Dimension At Least [in]  
> Before entry, the incremented array X must contain the n  
> element vector x.  
  
Incx : Integer [in]  
> On entry, INCX specifies the increment for the elements of  
> X. INCX must not be zero.  
  
Beta : Real [in]  
> On entry, BETA specifies the scalar beta. When BETA is  
> supplied as zero then Y need not be set on input.  
  
Y : Real Array, Dimension At Least [in,out]  
> Before entry, the incremented array Y must contain the n  
> element vector y. On exit, Y is overwritten by the updated  
> vector y.  
  
Incy : Integer [in]  
> On entry, INCY specifies the increment for the elements of  
> Y. INCY must not be zero.  
  
