```fortran  
subroutine caxpy (  
integer n,  
complex ca,  
complex, dimension(*) cx,  
integer incx,  
complex, dimension(*) cy,  
integer incy  
)  
```  
  
CAXPY constant times a vector plus a vector.  
  
## Parameters  
N : Integer [in]  
> number of elements in input vector(s)  
  
Ca : Complex [in]  
> On entry, CA specifies the scalar alpha.  
  
Cx : Complex Array, Dimension ( 1 + ( N - 1 )*abs( Incx ) ) [in]  
  
Incx : Integer [in]  
> storage spacing between elements of CX  
  
Cy : Complex Array, Dimension ( 1 + ( N - 1 )*abs( Incy ) ) [in,out]  
  
Incy : Integer [in]  
> storage spacing between elements of CY  
  
