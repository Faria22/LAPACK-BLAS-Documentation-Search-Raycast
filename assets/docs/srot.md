```fortran  
subroutine srot (  
integer n,  
real, dimension(*) sx,  
integer incx,  
real, dimension(*) sy,  
integer incy,  
real c,  
real s  
)  
```  
  
applies a plane rotation.  
  
## Parameters  
N : Integer [in]  
> number of elements in input vector(s)  
  
Sx : Real Array, Dimension ( 1 + ( N - 1 )*abs( Incx ) ) [in,out]  
  
Incx : Integer [in]  
> storage spacing between elements of SX  
  
Sy : Real Array, Dimension ( 1 + ( N - 1 )*abs( Incy ) ) [in,out]  
  
Incy : Integer [in]  
> storage spacing between elements of SY  
  
C : Real [in]  
  
S : Real [in]  
  
