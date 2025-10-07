```fortran  
subroutine zaxpy (  
integer n,  
complex*16 za,  
complex*16, dimension(*) zx,  
integer incx,  
complex*16, dimension(*) zy,  
integer incy  
)  
```  
  
ZAXPY constant times a vector plus a vector.  
  
## Parameters  
N : Integer [in]  
> number of elements in input vector(s)  
  
Za : Complex*16 [in]  
> On entry, ZA specifies the scalar alpha.  
  
Zx : Complex*16 Array, Dimension ( 1 + ( N - 1 )*abs( Incx ) ) [in]  
  
Incx : Integer [in]  
> storage spacing between elements of ZX  
  
Zy : Complex*16 Array, Dimension ( 1 + ( N - 1 )*abs( Incy ) ) [in,out]  
  
Incy : Integer [in]  
> storage spacing between elements of ZY  
  
