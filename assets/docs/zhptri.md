```fortran  
subroutine zhptri (  
character uplo,  
integer n,  
complex*16, dimension(*) ap,  
integer, dimension(*) ipiv,  
complex*16, dimension(*) work,  
integer info  
)  
```  
  
ZHPTRI computes the inverse of a complex Hermitian indefinite matrix  
A in packed storage using the factorization A = U*D*U**H or  
A = L*D*L**H computed by ZHPTRF.  
  
## Parameters  
Uplo : Character*1 [in]  
> Specifies whether the details of the factorization are stored  
> as an upper or lower triangular matrix.  
  
N : Integer [in]  
> The order of the matrix A.  N >= 0.  
  
Ap : Complex*16 Array, Dimension (n*(n+1)/2) [in,out]  
> On entry, the block diagonal matrix D and the multipliers  
> used to obtain the factor U or L as computed by ZHPTRF,  
> stored as a packed triangular matrix.  
> On exit, if INFO = 0, the (Hermitian) inverse of the original  
> matrix, stored as a packed triangular matrix. The j-th column  
> of inv(A) is stored in the array AP as follows:  
> if UPLO = 'L',  
  
Ipiv : Integer Array, Dimension (n) [in]  
> Details of the interchanges and the block structure of D  
> as determined by ZHPTRF.  
  
Work : Complex*16 Array, Dimension (n) [out]  
  
Info : Integer [out]  
> = 0: successful exit  
> < 0: if INFO = -i, the i-th argument had an illegal value  
> > 0: if INFO = i, D(i,i) = 0; the matrix is singular and its  
> inverse could not be computed.  
  
