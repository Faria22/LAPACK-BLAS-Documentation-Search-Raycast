```fortran  
subroutine saxpy (  
integer n,  
real sa,  
real, dimension(*) sx,  
integer incx,  
real, dimension(*) sy,  
integer incy  
)  
```  
  
SAXPY constant times a vector plus a vector.  
uses unrolled loops for increments equal to one.  
  
## Parameters  
N : Integer [in]  
> number of elements in input vector(s)  
  
Sa : Real [in]  
> On entry, SA specifies the scalar alpha.  
  
Sx : Real Array, Dimension ( 1 + ( N - 1 )*abs( Incx ) ) [in]  
  
Incx : Integer [in]  
> storage spacing between elements of SX  
  
Sy : Real Array, Dimension ( 1 + ( N - 1 )*abs( Incy ) ) [in,out]  
  
Incy : Integer [in]  
> storage spacing between elements of SY  
  
