```fortran  
subroutine zgesc2 (  
integer n,  
complex*16, dimension(lda, *) a,  
integer lda,  
complex*16, dimension(*) rhs,  
integer, dimension(*) ipiv,  
integer, dimension(*) jpiv,  
double precision scale  
)  
```  
  
ZGESC2 solves a system of linear equations  
  
A * X = scale* RHS  
  
with a general N-by-N matrix A using the LU factorization with  
complete pivoting computed by ZGETC2.  
  
  
## Parameters  
N : Integer [in]  
> The number of columns of the matrix A.  
  
A : Complex*16 Array, Dimension (lda, N) [in]  
> On entry, the  LU part of the factorization of the n-by-n  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1, N).  
  
Rhs : Complex*16 Array, Dimension N. [in,out]  
> On entry, the right hand side vector b.  
> On exit, the solution vector X.  
  
Ipiv : Integer Array, Dimension (n). [in]  
> The pivot indices; for 1 <= i <= N, row i of the  
> matrix has been interchanged with row IPIV(i).  
  
Jpiv : Integer Array, Dimension (n). [in]  
> The pivot indices; for 1 <= j <= N, column j of the  
> matrix has been interchanged with column JPIV(j).  
  
Scale : Double Precision [out]  
> On exit, SCALE contains the scale factor. SCALE is chosen  
> 0 <= SCALE <= 1 to prevent overflow in the solution.  
  
