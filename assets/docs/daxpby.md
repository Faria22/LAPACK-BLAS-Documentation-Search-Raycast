```fortran  
subroutine daxpby (  
integer n,  
double precision da,  
double precision, dimension(*) dx,  
integer incx,  
double precision db,  
double precision, dimension(*) dy,  
integer incy  
)  
```  
  
DAXPBY constant times a vector plus constant times a vector.  
  
Y = ALPHA * X + BETA * Y  
  
  
## Parameters  
N : Integer [in]  
> number of elements in input vector(s)  
  
Da : Double Precision [in]  
> On entry, DA specifies the scalar alpha.  
  
Dx : Double Precision Array, Dimension ( 1 + ( N - 1 )*abs( Incx ) ) [in]  
  
Incx : Integer [in]  
> storage spacing between elements of DX  
  
Db : Double Precision [in]  
> On entry, DB specifies the scalar beta.  
  
Dy : Double Precision Array, Dimension ( 1 + ( N - 1 )*abs( Incy ) ) [in,out]  
  
Incy : Integer [in]  
> storage spacing between elements of DY  
  
