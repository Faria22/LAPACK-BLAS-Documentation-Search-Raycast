```fortran  
subroutine clabrd (  
m,  
n,  
nb,  
a,  
lda,  
d,  
e,  
tauq,  
taup,  
x,  
ldx,  
y,  
*                          ldy  
)  
```  
  
CLABRD reduces the first NB rows and columns of a complex general  
m by n matrix A to upper or lower real bidiagonal form by a unitary  
transformation Q**H * A * P, and returns the matrices X and Y which  
are needed to apply the transformation to the unreduced part of A.  
  
If m >= n, A is reduced to upper bidiagonal form; if m < n, to lower  
bidiagonal form.  
  
This is an auxiliary routine called by CGEBRD  
  
## Parameters  
M : Integer [in]  
> The number of rows in the matrix A.  
  
N : Integer [in]  
> The number of columns in the matrix A.  
  
Nb : Integer [in]  
> The number of leading rows and columns of A to be reduced.  
  
A : Complex Array, Dimension (lda,n) [in,out]  
> On entry, the m by n general matrix to be reduced.  
> On exit, the first NB rows and columns of the matrix are  
> overwritten; the rest of the array is unchanged.  
> If m >= n, elements on and below the diagonal in the first NB  
> columns, with the array TAUQ, represent the unitary  
> matrix Q as a product of elementary reflectors; and  
> elements above the diagonal in the first NB rows, with the  
> array TAUP, represent the unitary matrix P as a product  
> of elementary reflectors.  
> If m < n, elements below the diagonal in the first NB  
> columns, with the array TAUQ, represent the unitary  
> matrix Q as a product of elementary reflectors, and  
> elements on and above the diagonal in the first NB rows,  
> with the array TAUP, represent the unitary matrix P as  
> a product of elementary reflectors.  
> See Further Details.  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,M).  
  
D : Real Array, Dimension (nb) [out]  
> The diagonal elements of the first NB rows and columns of  
> the reduced matrix.  D(i) = A(i,i).  
  
E : Real Array, Dimension (nb) [out]  
> The off-diagonal elements of the first NB rows and columns of  
> the reduced matrix.  
  
Tauq : Complex Array, Dimension (nb) [out]  
> The scalar factors of the elementary reflectors which  
> represent the unitary matrix Q. See Further Details.  
  
Taup : Complex Array, Dimension (nb) [out]  
> The scalar factors of the elementary reflectors which  
> represent the unitary matrix P. See Further Details.  
  
X : Complex Array, Dimension (ldx,nb) [out]  
> The m-by-nb matrix X required to update the unreduced part  
> of A.  
  
Ldx : Integer [in]  
> The leading dimension of the array X. LDX >= max(1,M).  
  
Y : Complex Array, Dimension (ldy,nb) [out]  
> The n-by-nb matrix Y required to update the unreduced part  
> of A.  
  
Ldy : Integer [in]  
> The leading dimension of the array Y. LDY >= max(1,N).  
  
