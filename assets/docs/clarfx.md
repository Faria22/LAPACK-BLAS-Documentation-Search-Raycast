```fortran  
subroutine clarfx (  
character side,  
integer m,  
integer n,  
complex, dimension(*) v,  
complex tau,  
complex, dimension(ldc, *) c,  
integer ldc,  
complex, dimension(*) work  
)  
```  
  
CLARFX applies a complex elementary reflector H to a complex m by n  
matrix C, from either the left or the right. H is represented in the  
form  
  
H = I - tau * v * v**H  
  
where tau is a complex scalar and v is a complex vector.  
  
If tau = 0, then H is taken to be the unit matrix  
  
This version uses inline code if H has order < 11.  
  
## Parameters  
Side : Character*1 [in]  
  
M : Integer [in]  
> The number of rows of the matrix C.  
  
N : Integer [in]  
> The number of columns of the matrix C.  
  
V : Complex Array, Dimension (m) If Side = 'l' [in]  
> or (N) if SIDE = 'R'  
> The vector v in the representation of H.  
  
Tau : Complex [in]  
> The value tau in the representation of H.  
  
C : Complex Array, Dimension (ldc,n) [in,out]  
> On entry, the m by n matrix C.  
  
Ldc : Integer [in]  
> The leading dimension of the array C. LDC >= max(1,M).  
  
Work : Complex Array, Dimension (n) If Side = 'l' [out]  
> or (M) if SIDE = 'R'  
> WORK is not referenced if H has order < 11.  
  
