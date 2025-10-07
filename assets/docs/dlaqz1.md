```fortran  
subroutine dlaqz1 (  
a,  
lda,  
b,  
ldb,  
sr1,  
sr2,  
si,  
beta1,  
beta2,  
*     $    v  
)  
```  
  
Given a 3-by-3 matrix pencil (A,B), DLAQZ1 sets v to a  
scalar multiple of the first column of the product  
  
(*)  K = (A - (beta2*sr2 - i*si)*B)*B^(-1)*(beta1*A - (sr2 + i*si2)*B)*B^(-1).  
  
It is assumed that either  
  
1) sr1 = sr2  
or  
2) si = 0.  
  
This is useful for starting double implicit shift bulges  
in the QZ algorithm.  
  
## Parameters  
A : Double Precision Array, Dimension (lda,n) [in]  
  
Lda : Integer [in]  
> The leading dimension of A as declared in  
> the calling procedure.  
  
B : Double Precision Array, Dimension (ldb,n) [in]  
  
Ldb : Integer [in]  
> The leading dimension of B as declared in  
> the calling procedure.  
  
Sr1 : Double Precision [in]  
  
Sr2 : Double Precision [in]  
  
Si : Double Precision [in]  
  
Beta1 : Double Precision [in]  
  
Beta2 : Double Precision [in]  
  
V : Double Precision Array, Dimension (n) [out]  
> A scalar multiple of the first column of the  
  
