```fortran  
subroutine drot (  
integer n,  
double precision, dimension(*) dx,  
integer incx,  
double precision, dimension(*) dy,  
integer incy,  
double precision c,  
double precision s  
)  
```  
  
DROT applies a plane rotation.  
  
## Parameters  
N : Integer [in]  
> number of elements in input vector(s)  
  
Dx : Double Precision Array, Dimension ( 1 + ( N - 1 )*abs( Incx ) ) [in,out]  
  
Incx : Integer [in]  
> storage spacing between elements of DX  
  
Dy : Double Precision Array, Dimension ( 1 + ( N - 1 )*abs( Incy ) ) [in,out]  
  
Incy : Integer [in]  
> storage spacing between elements of DY  
  
C : Double Precision [in]  
  
S : Double Precision [in]  
  
