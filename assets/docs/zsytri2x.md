```fortran  
subroutine zsytri2x (  
character uplo,  
integer n,  
complex*16, dimension(lda, *) a,  
integer lda,  
integer, dimension(*) ipiv,  
complex*16, dimension(n+nb+1,*) work,  
integer nb,  
integer info  
)  
```  
  
ZSYTRI2X computes the inverse of a complex symmetric indefinite matrix  
A using the factorization A = U*D*U**T or A = L*D*L**T computed by  
ZSYTRF.  
  
## Parameters  
Uplo : Character*1 [in]  
> Specifies whether the details of the factorization are stored  
> as an upper or lower triangular matrix.  
  
N : Integer [in]  
> The order of the matrix A.  N >= 0.  
  
A : Complex*16 Array, Dimension (lda,n) [in,out]  
> On entry, the NNB diagonal matrix D and the multipliers  
> used to obtain the factor U or L as computed by ZSYTRF.  
> On exit, if INFO = 0, the (symmetric) inverse of the original  
> matrix.  If UPLO = 'U', the upper triangular part of the  
> inverse is formed and the part of A below the diagonal is not  
> referenced; if UPLO = 'L' the lower triangular part of the  
> inverse is formed and the part of A above the diagonal is  
> not referenced.  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,N).  
  
Ipiv : Integer Array, Dimension (n) [in]  
> Details of the interchanges and the NNB structure of D  
> as determined by ZSYTRF.  
  
Work : Complex*16 Array, Dimension (n+nb+1,nb+3) [out]  
  
Nb : Integer [in]  
> Block size  
  
Info : Integer [out]  
> = 0: successful exit  
> < 0: if INFO = -i, the i-th argument had an illegal value  
> > 0: if INFO = i, D(i,i) = 0; the matrix is singular and its  
> inverse could not be computed.  
  
