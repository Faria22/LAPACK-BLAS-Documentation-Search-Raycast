```fortran  
subroutine slahr2 (  
integer n,  
integer k,  
integer nb,  
real, dimension(lda, *) a,  
integer lda,  
real, dimension(nb) tau,  
real, dimension(ldt, nb) t,  
integer ldt,  
y,  
integer ldy  
)  
```  
  
SLAHR2 reduces the first NB columns of A real general n-BY-(n-k+1)  
matrix A so that elements below the k-th subdiagonal are zero. The  
reduction is performed by an orthogonal similarity transformation  
Q**T * A * Q. The routine returns the matrices V and T which determine  
Q as a block reflector I - V*T*V**T, and also the matrix Y = A * V * T.  
  
This is an auxiliary routine called by SGEHRD.  
  
## Parameters  
N : Integer [in]  
> The order of the matrix A.  
  
K : Integer [in]  
> The offset for the reduction. Elements below the k-th  
> subdiagonal in the first NB columns are reduced to zero.  
> K < N.  
  
Nb : Integer [in]  
> The number of columns to be reduced.  
  
A : Real Array, Dimension (lda,n-k+1) [in,out]  
> On entry, the n-by-(n-k+1) general matrix A.  
> On exit, the elements on and above the k-th subdiagonal in  
> the first NB columns are overwritten with the corresponding  
> elements of the reduced matrix; the elements below the k-th  
> subdiagonal, with the array TAU, represent the matrix Q as a  
> product of elementary reflectors. The other columns of A are  
> unchanged. See Further Details.  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,N).  
  
Tau : Real Array, Dimension (nb) [out]  
> The scalar factors of the elementary reflectors. See Further  
> Details.  
  
T : Real Array, Dimension (ldt,nb) [out]  
> The upper triangular matrix T.  
  
Ldt : Integer [in]  
> The leading dimension of the array T.  LDT >= NB.  
  
Y : Real Array, Dimension (ldy,nb) [out]  
> The n-by-nb matrix Y.  
  
Ldy : Integer [in]  
> The leading dimension of the array Y. LDY >= N.  
  
