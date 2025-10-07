```fortran  
subroutine zrscl (  
integer n,  
complex*16 a,  
complex*16, dimension(*) x,  
integer incx  
)  
```  
  
ZRSCL multiplies an n-element complex vector x by the complex scalar  
1/a.  This is done without overflow or underflow as long as  
the final result x/a does not overflow or underflow.  
  
## Parameters  
N : Integer [in]  
> The number of components of the vector x.  
  
A : Complex*16 [in]  
> The scalar a which is used to divide each component of x.  
> A must not be 0, or the subroutine will divide by zero.  
  
X : Complex*16 Array, Dimension [in,out]  
> The n-element vector x.  
  
Incx : Integer [in]  
> The increment between successive values of the vector SX.  
  
