```fortran  
subroutine dswap (  
integer n,  
double precision, dimension(*) dx,  
integer incx,  
double precision, dimension(*) dy,  
integer incy  
)  
```  
  
DSWAP interchanges two vectors.  
uses unrolled loops for increments equal to 1.  
  
## Parameters  
N : Integer [in]  
> number of elements in input vector(s)  
  
Dx : Double Precision Array, Dimension ( 1 + ( N - 1 )*abs( Incx ) ) [in,out]  
  
Incx : Integer [in]  
> storage spacing between elements of DX  
  
Dy : Double Precision Array, Dimension ( 1 + ( N - 1 )*abs( Incy ) ) [in,out]  
  
Incy : Integer [in]  
> storage spacing between elements of DY  
  
