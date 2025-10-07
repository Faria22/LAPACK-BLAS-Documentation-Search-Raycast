```fortran  
subroutine clartv (  
integer n,  
complex, dimension(*) x,  
integer incx,  
complex, dimension(*) y,  
integer incy,  
real, dimension(*) c,  
complex, dimension(*) s,  
integer incc  
)  
```  
  
CLARTV applies a vector of complex plane rotations with real cosines  
to elements of the complex vectors x and y. For i = 1,2,...,n  
  
( x(i) ) := (        c(i)   s(i) ) ( x(i) )  
( y(i) )    ( -conjg(s(i))  c(i) ) ( y(i) )  
  
## Parameters  
N : Integer [in]  
> The number of plane rotations to be applied.  
  
X : Complex Array, Dimension (1+(n-1)*incx) [in,out]  
> The vector x.  
  
Incx : Integer [in]  
> The increment between elements of X. INCX > 0.  
  
Y : Complex Array, Dimension (1+(n-1)*incy) [in,out]  
> The vector y.  
  
Incy : Integer [in]  
> The increment between elements of Y. INCY > 0.  
  
C : Real Array, Dimension (1+(n-1)*incc) [in]  
> The cosines of the plane rotations.  
  
S : Complex Array, Dimension (1+(n-1)*incc) [in]  
> The sines of the plane rotations.  
  
Incc : Integer [in]  
> The increment between elements of C and S. INCC > 0.  
  
