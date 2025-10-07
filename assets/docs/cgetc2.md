```fortran  
subroutine cgetc2 (  
integer n,  
complex, dimension(lda, *) a,  
integer lda,  
integer, dimension(*) ipiv,  
integer, dimension(*) jpiv,  
integer info  
)  
```  
  
CGETC2 computes an LU factorization, using complete pivoting, of the  
n-by-n matrix A. The factorization has the form A = P * L * U * Q,  
where P and Q are permutation matrices, L is lower triangular with  
unit diagonal elements and U is upper triangular.  
  
This is a level 1 BLAS version of the algorithm.  
  
## Parameters  
N : Integer [in]  
> The order of the matrix A. N >= 0.  
  
A : Complex Array, Dimension (lda, N) [in,out]  
> On entry, the n-by-n matrix to be factored.  
> On exit, the factors L and U from the factorization  
> If U(k, k) appears to be less than SMIN, U(k, k) is given the  
> value of SMIN, giving a nonsingular perturbed system.  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1, N).  
  
Ipiv : Integer Array, Dimension (n). [out]  
> The pivot indices; for 1 <= i <= N, row i of the  
> matrix has been interchanged with row IPIV(i).  
  
Jpiv : Integer Array, Dimension (n). [out]  
> The pivot indices; for 1 <= j <= N, column j of the  
> matrix has been interchanged with column JPIV(j).  
  
Info : Integer [out]  
> = 0: successful exit  
> > 0: if INFO = k, U(k, k) is likely to produce overflow if  
> one tries to solve for x in Ax = b. So U is perturbed  
> to avoid the overflow.  
  
