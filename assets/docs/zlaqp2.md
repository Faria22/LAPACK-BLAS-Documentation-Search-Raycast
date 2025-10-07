```fortran  
subroutine zlaqp2 (  
m,  
n,  
offset,  
a,  
lda,  
jpvt,  
tau,  
vn1,  
vn2,  
*                          work  
)  
```  
  
ZLAQP2 computes a QR factorization with column pivoting of  
the block A(OFFSET+1:M,1:N).  
The block A(1:OFFSET,1:N) is accordingly pivoted, but not factorized.  
  
## Parameters  
M : Integer [in]  
> The number of rows of the matrix A. M >= 0.  
  
N : Integer [in]  
> The number of columns of the matrix A. N >= 0.  
  
Offset : Integer [in]  
> The number of rows of the matrix A that must be pivoted  
> but no factorized. OFFSET >= 0.  
  
A : Complex*16 Array, Dimension (lda,n) [in,out]  
> On entry, the M-by-N matrix A.  
> On exit, the upper triangle of block A(OFFSET+1:M,1:N) is  
> the triangular factor obtained; the elements in block  
> A(OFFSET+1:M,1:N) below the diagonal, together with the  
> array TAU, represent the orthogonal matrix Q as a product of  
> elementary reflectors. Block A(1:OFFSET,1:N) has been  
> accordingly pivoted, but no factorized.  
  
Lda : Integer [in]  
> The leading dimension of the array A. LDA >= max(1,M).  
  
Jpvt : Integer Array, Dimension (n) [in,out]  
> On entry, if JPVT(i) .ne. 0, the i-th column of A is permuted  
> the i-th column of A is a free column.  
> was the k-th column of A.  
  
Tau : Complex*16 Array, Dimension (min(m,n)) [out]  
> The scalar factors of the elementary reflectors.  
  
Vn1 : Double Precision Array, Dimension (n) [in,out]  
> The vector with the partial column norms.  
  
Vn2 : Double Precision Array, Dimension (n) [in,out]  
> The vector with the exact column norms.  
  
Work : Complex*16 Array, Dimension (n) [out]  
  
