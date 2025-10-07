```fortran  
subroutine dtfttp (  
character transr,  
character uplo,  
integer n,  
double precision, dimension(0: *) arf,  
double precision, dimension(0: *) ap,  
integer info  
)  
```  
  
DTFTTP copies a triangular matrix A from rectangular full packed  
format (TF) to standard packed format (TP).  
  
## Parameters  
Transr : Character*1 [in]  
> = 'N':  ARF is in Normal format;  
> = 'T':  ARF is in Transpose format;  
  
Uplo : Character*1 [in]  
> = 'U':  A is upper triangular;  
> = 'L':  A is lower triangular.  
  
N : Integer [in]  
> The order of the matrix A. N >= 0.  
  
Arf : Double Precision Array, Dimension ( N*(n+1)/2 ), [in]  
> On entry, the upper or lower triangular matrix A stored in  
> RFP format. For a further discussion see Notes below.  
  
Ap : Double Precision Array, Dimension ( N*(n+1)/2 ), [out]  
> On exit, the upper or lower triangular matrix A, packed  
> columnwise in a linear array. The j-th column of A is stored  
> in the array AP as follows:  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
  
