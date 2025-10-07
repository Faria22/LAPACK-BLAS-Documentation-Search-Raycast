```fortran  
subroutine saxpby (  
integer n,  
real sa,  
real, dimension(*) sx,  
integer incx,  
real sb,  
real, dimension(*) sy,  
integer incy  
)  
```  
  
SAXPBY constant times a vector plus constant times a vector.  
  
Y = ALPHA * X + BETA * Y  
  
  
## Parameters  
N : Integer [in]  
> number of elements in input vector(s)  
  
Sa : Real [in]  
> On entry, SA specifies the scalar alpha.  
  
Sx : Real Array, Dimension ( 1 + ( N - 1 )*abs( Incx ) ) [in]  
  
Incx : Integer [in]  
> storage spacing between elements of SX  
  
Sb : Real [in]  
> On entry, SB specifies the scalar beta.  
  
Sy : Real Array, Dimension ( 1 + ( N - 1 )*abs( Incy ) ) [in,out]  
  
Incy : Integer [in]  
> storage spacing between elements of SY  
  
