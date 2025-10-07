```fortran  
subroutine ssytri2 (  
character uplo,  
integer n,  
real, dimension(lda, *) a,  
integer lda,  
integer, dimension(*) ipiv,  
real, dimension(*) work,  
integer lwork,  
integer info  
)  
```  
  
SSYTRI2 computes the inverse of a REAL symmetric indefinite matrix  
A using the factorization A = U*D*U**T or A = L*D*L**T computed by  
SSYTRF. SSYTRI2 sets the LEADING DIMENSION of the workspace  
before calling SSYTRI2X that actually computes the inverse.  
  
## Parameters  
Uplo : Character*1 [in]  
> Specifies whether the details of the factorization are stored  
> as an upper or lower triangular matrix.  
  
N : Integer [in]  
> The order of the matrix A.  N >= 0.  
  
A : Real Array, Dimension (lda,n) [in,out]  
> On entry, the block diagonal matrix D and the multipliers  
> used to obtain the factor U or L as computed by SSYTRF.  
> On exit, if INFO = 0, the (symmetric) inverse of the original  
> matrix.  If UPLO = 'U', the upper triangular part of the  
> inverse is formed and the part of A below the diagonal is not  
> referenced; if UPLO = 'L' the lower triangular part of the  
> inverse is formed and the part of A above the diagonal is  
> not referenced.  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,N).  
  
Ipiv : Integer Array, Dimension (n) [in]  
> Details of the interchanges and the block structure of D  
> as determined by SSYTRF.  
  
Work : Real Array, Dimension (max(1,lwork)) [out]  
  
Lwork : Integer [in]  
> The dimension of the array WORK.  
> If LWORK = -1, then a workspace query is assumed; the routine  
> calculates:  
> - the optimal size of the WORK array, returns  
> this value as the first entry of the WORK array,  
> - and no error message related to LWORK is issued by XERBLA.  
  
Info : Integer [out]  
> = 0: successful exit  
> < 0: if INFO = -i, the i-th argument had an illegal value  
> > 0: if INFO = i, D(i,i) = 0; the matrix is singular and its  
> inverse could not be computed.  
  
