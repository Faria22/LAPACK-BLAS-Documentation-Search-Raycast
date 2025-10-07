```fortran  
subroutine crot (  
integer n,  
complex, dimension(*) cx,  
integer incx,  
complex, dimension(*) cy,  
integer incy,  
real c,  
complex s  
)  
```  
  
CROT applies a plane rotation, where the cos (C) is real and the  
sin (S) is complex, and the vectors CX and CY are complex.  
  
## Parameters  
N : Integer [in]  
> The number of elements in the vectors CX and CY.  
  
Cx : Complex Array, Dimension (n) [in,out]  
> On input, the vector X.  
  
Incx : Integer [in]  
> The increment between successive values of CX.  INCX <> 0.  
  
Cy : Complex Array, Dimension (n) [in,out]  
> On input, the vector Y.  
  
Incy : Integer [in]  
> The increment between successive values of CY.  INCX <> 0.  
  
C : Real [in]  
  
S : Complex [in]  
> C and S define a rotation  
> [  C          S  ]  
> [ -conjg(S)   C  ]  
  
