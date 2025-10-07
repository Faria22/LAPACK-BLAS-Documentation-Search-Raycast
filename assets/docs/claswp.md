```fortran  
subroutine claswp (  
integer n,  
complex, dimension(lda, *) a,  
integer lda,  
integer k1,  
integer k2,  
integer, dimension(*) ipiv,  
integer incx  
)  
```  
  
CLASWP performs a series of row interchanges on the matrix A.  
One row interchange is initiated for each of rows K1 through K2 of A.  
  
## Parameters  
N : Integer [in]  
> The number of columns of the matrix A.  
  
A : Complex Array, Dimension (lda,n) [in,out]  
> On entry, the matrix of column dimension N to which the row  
> interchanges will be applied.  
> On exit, the permuted matrix.  
  
Lda : Integer [in]  
> The leading dimension of the array A.  
  
K1 : Integer [in]  
> The first element of IPIV for which a row interchange will  
> be done.  
  
K2 : Integer [in]  
> (K2-K1+1) is the number of elements of IPIV for which a row  
> interchange will be done.  
  
Ipiv : Integer Array, Dimension (k1+(k2-k1)*abs(incx)) [in]  
> The vector of pivot indices. Only the elements in positions  
> interchanged.  
  
Incx : Integer [in]  
> The increment between successive values of IPIV. If INCX  
> is negative, the pivots are applied in reverse order.  
  
