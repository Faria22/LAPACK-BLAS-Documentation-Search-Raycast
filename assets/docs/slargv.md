```fortran  
subroutine slargv (  
integer n,  
real, dimension(*) x,  
integer incx,  
real, dimension(*) y,  
integer incy,  
real, dimension(*) c,  
integer incc  
)  
```  
  
SLARGV generates a vector of real plane rotations, determined by  
elements of the real vectors x and y. For i = 1,2,...,n  
  
(  c(i)  s(i) ) ( x(i) ) = ( a(i) )  
( -s(i)  c(i) ) ( y(i) ) = (   0  )  
  
## Parameters  
N : Integer [in]  
> The number of plane rotations to be generated.  
  
X : Real Array, [in,out]  
> On entry, the vector x.  
> On exit, x(i) is overwritten by a(i), for i = 1,...,n.  
  
Incx : Integer [in]  
> The increment between elements of X. INCX > 0.  
  
Y : Real Array, [in,out]  
> On entry, the vector y.  
> On exit, the sines of the plane rotations.  
  
Incy : Integer [in]  
> The increment between elements of Y. INCY > 0.  
  
C : Real Array, Dimension (1+(n-1)*incc) [out]  
> The cosines of the plane rotations.  
  
Incc : Integer [in]  
> The increment between elements of C. INCC > 0.  
  
