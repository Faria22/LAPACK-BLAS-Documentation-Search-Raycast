```fortran  
subroutine stfttr (  
character transr,  
character uplo,  
integer n,  
real, dimension(0: *) arf,  
real, dimension(0: lda-1, 0: *) a,  
integer lda,  
integer info  
)  
```  
  
STFTTR copies a triangular matrix A from rectangular full packed  
format (TF) to standard full format (TR).  
  
## Parameters  
Transr : Character*1 [in]  
> = 'N':  ARF is in Normal format;  
> = 'T':  ARF is in Transpose format.  
  
Uplo : Character*1 [in]  
> = 'U':  A is upper triangular;  
> = 'L':  A is lower triangular.  
  
N : Integer [in]  
> The order of the matrices ARF and A. N >= 0.  
  
Arf : Real Array, Dimension (n*(n+1)/2). [in]  
> On entry, the upper (if UPLO = 'U') or lower (if UPLO = 'L')  
> matrix A in RFP format. See the "Notes" below for more  
> details.  
  
A : Real Array, Dimension (lda,n) [out]  
> On exit, the triangular matrix A.  If UPLO = 'U', the  
> leading N-by-N upper triangular part of the array A contains  
> the upper triangular matrix, and the strictly lower  
> triangular part of A is not referenced.  If UPLO = 'L', the  
> leading N-by-N lower triangular part of the array A contains  
> the lower triangular matrix, and the strictly upper  
> triangular part of A is not referenced.  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,N).  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
  
