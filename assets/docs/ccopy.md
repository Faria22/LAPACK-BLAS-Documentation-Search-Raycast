```fortran  
subroutine ccopy (  
integer n,  
complex, dimension(*) cx,  
integer incx,  
complex, dimension(*) cy,  
integer incy  
)  
```  
  
CCOPY copies a vector x to a vector y.  
  
## Parameters  
N : Integer [in]  
> number of elements in input vector(s)  
  
Cx : Complex Array, Dimension ( 1 + ( N - 1 )*abs( Incx ) ) [in]  
  
Incx : Integer [in]  
> storage spacing between elements of CX  
  
Cy : Complex Array, Dimension ( 1 + ( N - 1 )*abs( Incy ) ) [out]  
  
Incy : Integer [in]  
> storage spacing between elements of CY  
  
