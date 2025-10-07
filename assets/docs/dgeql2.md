```fortran  
subroutine dgeql2 (  
integer m,  
integer n,  
double precision, dimension(lda, *) a,  
integer lda,  
double precision, dimension(*) tau,  
double precision, dimension(*) work,  
integer info  
)  
```  
  
DGEQL2 computes a QL factorization of a real m by n matrix A:  
A = Q * L.  
  
## Parameters  
M : Integer [in]  
> The number of rows of the matrix A.  M >= 0.  
  
N : Integer [in]  
> The number of columns of the matrix A.  N >= 0.  
  
A : Double Precision Array, Dimension (lda,n) [in,out]  
> On entry, the m by n matrix A.  
> On exit, if m >= n, the lower triangle of the subarray  
> A(m-n+1:m,1:n) contains the n by n lower triangular matrix L;  
> if m <= n, the elements on and below the (n-m)-th  
> superdiagonal contain the m by n lower trapezoidal matrix L;  
> the remaining elements, with the array TAU, represent the  
> orthogonal matrix Q as a product of elementary reflectors  
> (see Further Details).  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,M).  
  
Tau : Double Precision Array, Dimension (min(m,n)) [out]  
> The scalar factors of the elementary reflectors (see Further  
> Details).  
  
Work : Double Precision Array, Dimension (n) [out]  
  
Info : Integer [out]  
> = 0: successful exit  
> < 0: if INFO = -i, the i-th argument had an illegal value  
  
