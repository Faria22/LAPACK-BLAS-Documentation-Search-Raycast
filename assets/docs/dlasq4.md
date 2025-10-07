```fortran  
subroutine dlasq4 (  
i0,  
n0,  
z,  
pp,  
n0in,  
dmin,  
dmin1,  
dmin2,  
dn,  
*                          dn1,  
dn2,  
tau,  
ttype,  
g  
)  
```  
  
DLASQ4 computes an approximation TAU to the smallest eigenvalue  
using values of d from the previous transform.  
  
## Parameters  
I0 : Integer [in]  
> First index.  
  
N0 : Integer [in]  
> Last index.  
  
Z : Double Precision Array, Dimension ( 4*n0 ) [in]  
> Z holds the qd array.  
  
Pp : Integer [in]  
> PP=0 for ping, PP=1 for pong.  
  
N0in : Integer [in]  
> The value of N0 at start of EIGTEST.  
  
Dmin : Double Precision [in]  
> Minimum value of d.  
  
Dmin1 : Double Precision [in]  
> Minimum value of d, excluding D( N0 ).  
  
Dmin2 : Double Precision [in]  
> Minimum value of d, excluding D( N0 ) and D( N0-1 ).  
  
Dn : Double Precision [in]  
> d(N)  
  
Dn1 : Double Precision [in]  
> d(N-1)  
  
Dn2 : Double Precision [in]  
> d(N-2)  
  
Tau : Double Precision [out]  
> This is the shift.  
  
Ttype : Integer [out]  
> Shift type.  
  
G : Double Precision [in,out]  
> G is passed as an argument in order to save its value between  
> calls to DLASQ4.  
  
