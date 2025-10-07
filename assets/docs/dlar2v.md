```fortran  
subroutine dlar2v (  
integer n,  
double precision, dimension(*) x,  
double precision, dimension(*) y,  
double precision, dimension(*) z,  
integer incx,  
double precision, dimension(*) c,  
double precision, dimension(*) s,  
integer incc  
)  
```  
  
DLAR2V applies a vector of real plane rotations from both sides to  
a sequence of 2-by-2 real symmetric matrices, defined by the elements  
of the vectors x, y and z. For i = 1,2,...,n  
  
( x(i)  z(i) ) := (  c(i)  s(i) ) ( x(i)  z(i) ) ( c(i) -s(i) )  
( z(i)  y(i) )    ( -s(i)  c(i) ) ( z(i)  y(i) ) ( s(i)  c(i) )  
  
## Parameters  
N : Integer [in]  
> The number of plane rotations to be applied.  
  
X : Double Precision Array, [in,out]  
> The vector x.  
  
Y : Double Precision Array, [in,out]  
> The vector y.  
  
Z : Double Precision Array, [in,out]  
> The vector z.  
  
Incx : Integer [in]  
> The increment between elements of X, Y and Z. INCX > 0.  
  
C : Double Precision Array, Dimension (1+(n-1)*incc) [in]  
> The cosines of the plane rotations.  
  
S : Double Precision Array, Dimension (1+(n-1)*incc) [in]  
> The sines of the plane rotations.  
  
Incc : Integer [in]  
> The increment between elements of C and S. INCC > 0.  
  
