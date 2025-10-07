```fortran  
subroutine dlarfg (  
integer n,  
double precision alpha,  
double precision, dimension(*) x,  
integer incx,  
double precision tau  
)  
```  
  
DLARFG generates a real elementary reflector H of order n, such  
that  
  
H * ( alpha ) = ( beta ),   H**T * H = I.  
(   x   )   (   0  )  
  
where alpha and beta are scalars, and x is an (n-1)-element real  
vector. H is represented in the form  
  
H = I - tau * ( 1 ) * ( 1 v**T ) ,  
( v )  
  
where tau is a real scalar and v is a real (n-1)-element  
vector.  
  
If the elements of x are all zero, then tau = 0 and H is taken to be  
the unit matrix.  
  
Otherwise  1 <= tau <= 2.  
  
## Parameters  
N : Integer [in]  
> The order of the elementary reflector.  
  
Alpha : Double Precision [in,out]  
> On entry, the value alpha.  
> On exit, it is overwritten with the value beta.  
  
X : Double Precision Array, Dimension [in,out]  
> On entry, the vector x.  
> On exit, it is overwritten with the vector v.  
  
Incx : Integer [in]  
> The increment between elements of X. INCX > 0.  
  
Tau : Double Precision [out]  
> The value tau.  
  
