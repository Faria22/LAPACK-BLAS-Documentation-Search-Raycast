```fortran  
subroutine stpqrt (  
m,  
n,  
l,  
nb,  
a,  
lda,  
b,  
ldb,  
t,  
ldt,  
work,  
*                          info  
)  
```  
  
STPQRT computes a blocked QR factorization of a real  
"triangular-pentagonal" matrix C, which is composed of a  
triangular block A and pentagonal block B, using the compact  
WY representation for Q.  
  
## Parameters  
M : Integer [in]  
> The number of rows of the matrix B.  
> M >= 0.  
  
N : Integer [in]  
> The number of columns of the matrix B, and the order of the  
> triangular matrix A.  
> N >= 0.  
  
L : Integer [in]  
> The number of rows of the upper trapezoidal part of B.  
> MIN(M,N) >= L >= 0.  See Further Details.  
  
Nb : Integer [in]  
> The block size to be used in the blocked QR.  N >= NB >= 1.  
  
A : Real Array, Dimension (lda,n) [in,out]  
> On entry, the upper triangular N-by-N matrix A.  
> On exit, the elements on and above the diagonal of the array  
> contain the upper triangular matrix R.  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,N).  
  
B : Real Array, Dimension (ldb,n) [in,out]  
> On entry, the pentagonal M-by-N matrix B.  The first M-L rows  
> are rectangular, and the last L rows are upper trapezoidal.  
> On exit, B contains the pentagonal matrix V.  See Further Details.  
  
Ldb : Integer [in]  
> The leading dimension of the array B.  LDB >= max(1,M).  
  
T : Real Array, Dimension (ldt,n) [out]  
> The upper triangular block reflectors stored in compact form  
> as a sequence of upper triangular blocks.  See Further Details.  
  
Ldt : Integer [in]  
> The leading dimension of the array T.  LDT >= NB.  
  
Work : Real Array, Dimension (nb*n) [out]  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
  
