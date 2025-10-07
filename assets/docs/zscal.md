```fortran  
subroutine zscal (  
integer n,  
complex*16 za,  
complex*16, dimension(*) zx,  
integer incx  
)  
```  
  
ZSCAL scales a vector by a constant.  
  
## Parameters  
N : Integer [in]  
> number of elements in input vector(s)  
  
Za : Complex*16 [in]  
> On entry, ZA specifies the scalar alpha.  
  
Zx : Complex*16 Array, Dimension ( 1 + ( N - 1 )*abs( Incx ) ) [in,out]  
  
Incx : Integer [in]  
> storage spacing between elements of ZX  
  
