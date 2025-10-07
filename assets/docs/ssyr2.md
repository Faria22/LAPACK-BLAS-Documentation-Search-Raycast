```fortran  
subroutine ssyr2 (  
character uplo,  
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
  
SSYR2  performs the symmetric rank 2 operation  
  
A := alpha*x*y**T + alpha*y*x**T + A,  
  
where alpha is a scalar, x and y are n element vectors and A is an n  
by n symmetric matrix.  
  
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
  
X : Real Array, Dimension At Least [in]  
> Before entry, the incremented array X must contain the n  
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
> Before entry with  UPLO = 'U' or 'u', the leading n by n  
> upper triangular part of the array A must contain the upper  
> triangular part of the symmetric matrix and the strictly  
> lower triangular part of A is not referenced. On exit, the  
> upper triangular part of the array A is overwritten by the  
> upper triangular part of the updated matrix.  
> Before entry with UPLO = 'L' or 'l', the leading n by n  
> lower triangular part of the array A must contain the lower  
> triangular part of the symmetric matrix and the strictly  
> upper triangular part of A is not referenced. On exit, the  
> lower triangular part of the array A is overwritten by the  
> lower triangular part of the updated matrix.  
  
Lda : Integer [in]  
> On entry, LDA specifies the first dimension of A as declared  
> in the calling (sub) program. LDA must be at least  
> max( 1, n ).  
  
