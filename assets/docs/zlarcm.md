```fortran  
subroutine zlarcm (  
integer m,  
integer n,  
double precision, dimension(lda, *) a,  
integer lda,  
complex*16, dimension(ldb, *) b,  
integer ldb,  
complex*16, dimension(ldc, *) c,  
integer ldc,  
double precision, dimension(*) rwork  
)  
```  
  
ZLARCM performs a very simple matrix-matrix multiplication:  
C := A * B,  
where A is M by M and real; B is M by N and complex;  
C is M by N and complex.  
  
## Parameters  
M : Integer [in]  
> The number of rows of the matrix A and of the matrix C.  
> M >= 0.  
  
N : Integer [in]  
> The number of columns and rows of the matrix B and  
> the number of columns of the matrix C.  
> N >= 0.  
  
A : Double Precision Array, Dimension (lda, M) [in]  
> On entry, A contains the M by M matrix A.  
  
Lda : Integer [in]  
> The leading dimension of the array A. LDA >=max(1,M).  
  
B : Complex*16 Array, Dimension (ldb, N) [in]  
> On entry, B contains the M by N matrix B.  
  
Ldb : Integer [in]  
> The leading dimension of the array B. LDB >=max(1,M).  
  
C : Complex*16 Array, Dimension (ldc, N) [out]  
> On exit, C contains the M by N matrix C.  
  
Ldc : Integer [in]  
> The leading dimension of the array C. LDC >=max(1,M).  
  
Rwork : Double Precision Array, Dimension (2*m*n) [out]  
  
