```fortran  
subroutine cgerq2 (  
integer m,  
integer n,  
complex, dimension(lda, *) a,  
integer lda,  
complex, dimension(*) tau,  
complex, dimension(*) work,  
integer info  
)  
```  
  
CGERQ2 computes an RQ factorization of a complex m by n matrix A:  
A = R * Q.  
  
## Parameters  
M : Integer [in]  
> The number of rows of the matrix A.  M >= 0.  
  
N : Integer [in]  
> The number of columns of the matrix A.  N >= 0.  
  
A : Complex Array, Dimension (lda,n) [in,out]  
> On entry, the m by n matrix A.  
> On exit, if m <= n, the upper triangle of the subarray  
> A(1:m,n-m+1:n) contains the m by m upper triangular matrix R;  
> if m >= n, the elements on and above the (m-n)-th subdiagonal  
> contain the m by n upper trapezoidal matrix R; the remaining  
> elements, with the array TAU, represent the unitary matrix  
> Q as a product of elementary reflectors (see Further  
> Details).  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,M).  
  
Tau : Complex Array, Dimension (min(m,n)) [out]  
> The scalar factors of the elementary reflectors (see Further  
> Details).  
  
Work : Complex Array, Dimension (m) [out]  
  
Info : Integer [out]  
> = 0: successful exit  
> < 0: if INFO = -i, the i-th argument had an illegal value  
  
