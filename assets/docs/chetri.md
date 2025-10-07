```fortran  
subroutine chetri (  
character uplo,  
integer n,  
complex, dimension(lda, *) a,  
integer lda,  
integer, dimension(*) ipiv,  
complex, dimension(*) work,  
integer info  
)  
```  
  
CHETRI computes the inverse of a complex Hermitian indefinite matrix  
A using the factorization A = U*D*U**H or A = L*D*L**H computed by  
CHETRF.  
  
## Parameters  
Uplo : Character*1 [in]  
> Specifies whether the details of the factorization are stored  
> as an upper or lower triangular matrix.  
  
N : Integer [in]  
> The order of the matrix A.  N >= 0.  
  
A : Complex Array, Dimension (lda,n) [in,out]  
> On entry, the block diagonal matrix D and the multipliers  
> used to obtain the factor U or L as computed by CHETRF.  
> On exit, if INFO = 0, the (Hermitian) inverse of the original  
> matrix.  If UPLO = 'U', the upper triangular part of the  
> inverse is formed and the part of A below the diagonal is not  
> referenced; if UPLO = 'L' the lower triangular part of the  
> inverse is formed and the part of A above the diagonal is  
> not referenced.  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,N).  
  
Ipiv : Integer Array, Dimension (n) [in]  
> Details of the interchanges and the block structure of D  
> as determined by CHETRF.  
  
Work : Complex Array, Dimension (n) [out]  
  
Info : Integer [out]  
> = 0: successful exit  
> < 0: if INFO = -i, the i-th argument had an illegal value  
> > 0: if INFO = i, D(i,i) = 0; the matrix is singular and its  
> inverse could not be computed.  
  
