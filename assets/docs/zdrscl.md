```fortran  
subroutine zdrscl (  
integer n,  
double precision sa,  
complex*16, dimension(*) sx,  
integer incx  
)  
```  
  
ZDRSCL multiplies an n-element complex vector x by the real scalar  
1/a.  This is done without overflow or underflow as long as  
the final result x/a does not overflow or underflow.  
  
## Parameters  
N : Integer [in]  
> The number of components of the vector x.  
  
Sa : Double Precision [in]  
> The scalar a which is used to divide each component of x.  
> SA must be >= 0, or the subroutine will divide by zero.  
  
Sx : Complex*16 Array, Dimension [in,out]  
> The n-element vector x.  
  
Incx : Integer [in]  
> The increment between successive values of the vector SX.  
  
