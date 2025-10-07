```fortran  
subroutine ztplqt2 (  
integer m,  
integer n,  
integer l,  
complex*16, dimension(lda, *) a,  
integer lda,  
complex*16, dimension(ldb, *) b,  
integer ldb,  
complex*16, dimension(ldt, *) t,  
integer ldt,  
integer info  
)  
```  
  
ZTPLQT2 computes a LQ a factorization of a complex "triangular-pentagonal"  
matrix C, which is composed of a triangular block A and pentagonal block B,  
using the compact WY representation for Q.  
  
## Parameters  
M : Integer [in]  
> The total number of rows of the matrix B.  
> M >= 0.  
  
N : Integer [in]  
> The number of columns of the matrix B, and the order of  
> the triangular matrix A.  
> N >= 0.  
  
L : Integer [in]  
> The number of rows of the lower trapezoidal part of B.  
> MIN(M,N) >= L >= 0.  See Further Details.  
  
A : Complex*16 Array, Dimension (lda,m) [in,out]  
> On entry, the lower triangular M-by-M matrix A.  
> On exit, the elements on and below the diagonal of the array  
> contain the lower triangular matrix L.  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,M).  
  
B : Complex*16 Array, Dimension (ldb,n) [in,out]  
> On entry, the pentagonal M-by-N matrix B.  The first N-L columns  
> are rectangular, and the last L columns are lower trapezoidal.  
> On exit, B contains the pentagonal matrix V.  See Further Details.  
  
Ldb : Integer [in]  
> The leading dimension of the array B.  LDB >= max(1,M).  
  
T : Complex*16 Array, Dimension (ldt,m) [out]  
> The N-by-N upper triangular factor T of the block reflector.  
> See Further Details.  
  
Ldt : Integer [in]  
> The leading dimension of the array T.  LDT >= max(1,M)  
  
Info : Integer [out]  
> = 0: successful exit  
> < 0: if INFO = -i, the i-th argument had an illegal value  
  
