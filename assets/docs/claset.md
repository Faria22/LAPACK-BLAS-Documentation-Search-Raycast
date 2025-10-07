```fortran  
subroutine claset (  
character uplo,  
integer m,  
integer n,  
complex alpha,  
complex beta,  
complex, dimension(lda, *) a,  
integer lda  
)  
```  
  
CLASET initializes a 2-D array A to BETA on the diagonal and  
ALPHA on the offdiagonals.  
  
## Parameters  
Uplo : Character*1 [in]  
> Specifies the part of the matrix A to be set.  
> = 'U':      Upper triangular part is set. The lower triangle  
> is unchanged.  
> = 'L':      Lower triangular part is set. The upper triangle  
> is unchanged.  
> Otherwise:  All of the matrix A is set.  
  
M : Integer [in]  
> On entry, M specifies the number of rows of A.  
  
N : Integer [in]  
> On entry, N specifies the number of columns of A.  
  
Alpha : Complex [in]  
> All the offdiagonal array elements are set to ALPHA.  
  
Beta : Complex [in]  
> All the diagonal array elements are set to BETA.  
  
A : Complex Array, Dimension (lda,n) [out]  
> On entry, the m by n matrix A.  
> On exit, A(i,j) = ALPHA, 1 <= i <= m, 1 <= j <= n, i.ne.j;  
> A(i,i) = BETA , 1 <= i <= min(m,n)  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,M).  
  
