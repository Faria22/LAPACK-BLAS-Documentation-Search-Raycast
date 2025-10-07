```fortran  
subroutine slarfgp (  
integer n,  
real alpha,  
real, dimension(*) x,  
integer incx,  
real tau  
)  
```  
  
SLARFGP generates a real elementary reflector H of order n, such  
that  
  
H * ( alpha ) = ( beta ),   H**T * H = I.  
(   x   )   (   0  )  
  
where alpha and beta are scalars, beta is non-negative, and x is  
an (n-1)-element real vector.  H is represented in the form  
  
H = I - tau * ( 1 ) * ( 1 v**T ) ,  
( v )  
  
where tau is a real scalar and v is a real (n-1)-element  
vector.  
  
If the elements of x are all zero, then tau = 0 and H is taken to be  
the unit matrix.  
  
## Parameters  
N : Integer [in]  
> The order of the elementary reflector.  
  
Alpha : Real [in,out]  
> On entry, the value alpha.  
> On exit, it is overwritten with the value beta.  
  
X : Real Array, Dimension [in,out]  
> On entry, the vector x.  
> On exit, it is overwritten with the vector v.  
  
Incx : Integer [in]  
> The increment between elements of X. INCX > 0.  
  
Tau : Real [out]  
> The value tau.  
  
