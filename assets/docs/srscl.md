```fortran  
subroutine srscl (  
integer n,  
real sa,  
real, dimension(*) sx,  
integer incx  
)  
```  
  
SRSCL multiplies an n-element real vector x by the real scalar 1/a.  
This is done without overflow or underflow as long as  
the final result x/a does not overflow or underflow.  
  
## Parameters  
N : Integer [in]  
> The number of components of the vector x.  
  
Sa : Real [in]  
> The scalar a which is used to divide each component of x.  
> SA must be >= 0, or the subroutine will divide by zero.  
  
Sx : Real Array, Dimension [in,out]  
> The n-element vector x.  
  
Incx : Integer [in]  
> The increment between successive values of the vector SX.  
  
