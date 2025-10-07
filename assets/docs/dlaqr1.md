```fortran  
subroutine dlaqr1 (  
integer n,  
double precision, dimension(ldh, *) h,  
integer ldh,  
double precision sr1,  
double precision si1,  
double precision sr2,  
double precision si2,  
double precision, dimension(*) v  
)  
```  
  
Given a 2-by-2 or 3-by-3 matrix H, DLAQR1 sets v to a  
scalar multiple of the first column of the product  
  
(*)  K = (H - (sr1 + i*si1)*I)*(H - (sr2 + i*si2)*I)  
  
scaling to avoid overflows and most underflows. It  
is assumed that either  
  
1) sr1 = sr2 and si1 = -si2  
or  
2) si1 = si2 = 0.  
  
This is useful for starting double implicit shift bulges  
in the QR algorithm.  
  
## Parameters  
N : Integer [in]  
> Order of the matrix H. N must be either 2 or 3.  
  
H : Double Precision Array, Dimension (ldh,n) [in]  
  
Ldh : Integer [in]  
> The leading dimension of H as declared in  
> the calling procedure.  LDH >= N  
  
Sr1 : Double Precision [in]  
  
Si1 : Double Precision [in]  
  
Sr2 : Double Precision [in]  
  
Si2 : Double Precision [in]  
  
V : Double Precision Array, Dimension (n) [out]  
> A scalar multiple of the first column of the  
  
