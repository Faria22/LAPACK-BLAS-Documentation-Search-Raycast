```fortran  
subroutine dlas2 (  
double precision f,  
double precision g,  
double precision h,  
double precision ssmin,  
double precision ssmax  
)  
```  
  
DLAS2  computes the singular values of the 2-by-2 matrix  
[  F   G  ]  
[  0   H  ].  
On return, SSMIN is the smaller singular value and SSMAX is the  
larger singular value.  
  
## Parameters  
F : Double Precision [in]  
> The (1,1) element of the 2-by-2 matrix.  
  
G : Double Precision [in]  
> The (1,2) element of the 2-by-2 matrix.  
  
H : Double Precision [in]  
> The (2,2) element of the 2-by-2 matrix.  
  
Ssmin : Double Precision [out]  
> The smaller singular value.  
  
Ssmax : Double Precision [out]  
> The larger singular value.  
  
