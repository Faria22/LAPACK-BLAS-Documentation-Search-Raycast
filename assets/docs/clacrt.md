```fortran  
subroutine clacrt (  
integer n,  
complex, dimension(*) cx,  
integer incx,  
complex, dimension(*) cy,  
integer incy,  
complex c,  
complex s  
)  
```  
  
CLACRT performs the operation  
  
(  c  s )( x )  ==> ( x )  
( -s  c )( y )      ( y )  
  
where c and s are complex and the vectors x and y are complex.  
  
## Parameters  
N : Integer [in]  
> The number of elements in the vectors CX and CY.  
  
Cx : Complex Array, Dimension (n) [in,out]  
> On input, the vector x.  
  
Incx : Integer [in]  
> The increment between successive values of CX.  INCX <> 0.  
  
Cy : Complex Array, Dimension (n) [in,out]  
> On input, the vector y.  
  
Incy : Integer [in]  
> The increment between successive values of CY.  INCY <> 0.  
  
C : Complex [in]  
  
S : Complex [in]  
> C and S define the matrix  
> [  C   S  ].  
> [ -S   C  ]  
  
