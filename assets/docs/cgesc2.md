```fortran  
subroutine cgesc2 (  
integer n,  
complex, dimension(lda, *) a,  
integer lda,  
complex, dimension(*) rhs,  
integer, dimension(*) ipiv,  
integer, dimension(*) jpiv,  
real scale  
)  
```  
  
CGESC2 solves a system of linear equations  
  
A * X = scale* RHS  
  
with a general N-by-N matrix A using the LU factorization with  
complete pivoting computed by CGETC2.  
  
  
## Parameters  
N : Integer [in]  
> The number of columns of the matrix A.  
  
A : Complex Array, Dimension (lda, N) [in]  
> On entry, the  LU part of the factorization of the n-by-n  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1, N).  
  
Rhs : Complex Array, Dimension N. [in,out]  
> On entry, the right hand side vector b.  
> On exit, the solution vector X.  
  
Ipiv : Integer Array, Dimension (n). [in]  
> The pivot indices; for 1 <= i <= N, row i of the  
> matrix has been interchanged with row IPIV(i).  
  
Jpiv : Integer Array, Dimension (n). [in]  
> The pivot indices; for 1 <= j <= N, column j of the  
> matrix has been interchanged with column JPIV(j).  
  
Scale : Real [out]  
> On exit, SCALE contains the scale factor. SCALE is chosen  
> 0 <= SCALE <= 1 to prevent overflow in the solution.  
  
