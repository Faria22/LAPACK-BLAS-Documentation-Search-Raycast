```fortran  
subroutine zgbequ (  
m,  
n,  
kl,  
ku,  
ab,  
ldab,  
r,  
c,  
rowcnd,  
colcnd,  
*                          amax,  
info  
)  
```  
  
ZGBEQU computes row and column scalings intended to equilibrate an  
M-by-N band matrix A and reduce its condition number.  R returns the  
row scale factors and C the column scale factors, chosen to try to  
make the largest element in each row and column of the matrix B with  
elements B(i,j)=R(i)*A(i,j)*C(j) have absolute value 1.  
  
R(i) and C(j) are restricted to be between SMLNUM = smallest safe  
number and BIGNUM = largest safe number.  Use of these scaling  
factors is not guaranteed to reduce the condition number of A but  
works well in practice.  
  
## Parameters  
M : Integer [in]  
> The number of rows of the matrix A.  M >= 0.  
  
N : Integer [in]  
> The number of columns of the matrix A.  N >= 0.  
  
Kl : Integer [in]  
> The number of subdiagonals within the band of A.  KL >= 0.  
  
Ku : Integer [in]  
> The number of superdiagonals within the band of A.  KU >= 0.  
  
Ab : Complex*16 Array, Dimension (ldab,n) [in]  
> The band matrix A, stored in rows 1 to KL+KU+1.  The j-th  
> column of A is stored in the j-th column of the array AB as  
> follows:  
> AB(ku+1+i-j,j) = A(i,j) for max(1,j-ku)<=i<=min(m,j+kl).  
  
Ldab : Integer [in]  
> The leading dimension of the array AB.  LDAB >= KL+KU+1.  
  
R : Double Precision Array, Dimension (m) [out]  
> If INFO = 0, or INFO > M, R contains the row scale factors  
> for A.  
  
C : Double Precision Array, Dimension (n) [out]  
> If INFO = 0, C contains the column scale factors for A.  
  
Rowcnd : Double Precision [out]  
> If INFO = 0 or INFO > M, ROWCND contains the ratio of the  
> smallest R(i) to the largest R(i).  If ROWCND >= 0.1 and  
> AMAX is neither too large nor too small, it is not worth  
> scaling by R.  
  
Colcnd : Double Precision [out]  
> If INFO = 0, COLCND contains the ratio of the smallest  
> C(i) to the largest C(i).  If COLCND >= 0.1, it is not  
> worth scaling by C.  
  
Amax : Double Precision [out]  
> Absolute value of largest matrix element.  If AMAX is very  
> close to overflow or very close to underflow, the matrix  
> should be scaled.  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
> > 0:  if INFO = i, and i is  
> <= M:  the i-th row of A is exactly zero  
> >  M:  the (i-M)-th column of A is exactly zero  
  
