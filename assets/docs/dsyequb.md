```fortran  
subroutine dsyequb (  
character uplo,  
integer n,  
double precision, dimension(lda, *) a,  
integer lda,  
double precision, dimension(*) s,  
double precision scond,  
double precision amax,  
double precision, dimension(*) work,  
integer info  
)  
```  
  
DSYEQUB computes row and column scalings intended to equilibrate a  
symmetric matrix A (with respect to the Euclidean norm) and reduce  
its condition number. The scale factors S are computed by the BIN  
algorithm (see references) so that the scaled matrix B with elements  
B(i,j) = S(i)*A(i,j)*S(j) has a condition number within a factor N of  
the smallest possible condition number over all possible diagonal  
scalings.  
  
## Parameters  
Uplo : Character*1 [in]  
> = 'U':  Upper triangle of A is stored;  
> = 'L':  Lower triangle of A is stored.  
  
N : Integer [in]  
> The order of the matrix A. N >= 0.  
  
A : Double Precision Array, Dimension (lda,n) [in]  
> The N-by-N symmetric matrix whose scaling factors are to be  
> computed.  
  
Lda : Integer [in]  
> The leading dimension of the array A. LDA >= max(1,N).  
  
S : Double Precision Array, Dimension (n) [out]  
> If INFO = 0, S contains the scale factors for A.  
  
Scond : Double Precision [out]  
> If INFO = 0, S contains the ratio of the smallest S(i) to  
> the largest S(i). If SCOND >= 0.1 and AMAX is neither too  
> large nor too small, it is not worth scaling by S.  
  
Amax : Double Precision [out]  
> Largest absolute value of any matrix element. If AMAX is  
> very close to overflow or very close to underflow, the  
> matrix should be scaled.  
  
Work : Double Precision Array, Dimension (2*n) [out]  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
> > 0:  if INFO = i, the i-th diagonal element is nonpositive.  
  
