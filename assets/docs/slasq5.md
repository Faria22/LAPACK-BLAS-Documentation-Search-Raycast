```fortran  
subroutine slasq5 (  
i0,  
n0,  
z,  
pp,  
tau,  
sigma,  
dmin,  
dmin1,  
dmin2,  
dn,  
*                          dnm1,  
dnm2,  
ieee,  
eps  
)  
```  
  
SLASQ5 computes one dqds transform in ping-pong form, one  
version for IEEE machines another for non IEEE machines.  
  
## Parameters  
I0 : Integer [in]  
> First index.  
  
N0 : Integer [in]  
> Last index.  
  
Z : Real Array, Dimension ( 4*n ) [in]  
> an extra argument.  
  
Pp : Integer [in]  
> PP=0 for ping, PP=1 for pong.  
  
Tau : Real [in]  
> This is the shift.  
  
Sigma : Real [in]  
> This is the accumulated shift up to this step.  
  
Dmin : Real [out]  
> Minimum value of d.  
  
Dmin1 : Real [out]  
> Minimum value of d, excluding D( N0 ).  
  
Dmin2 : Real [out]  
> Minimum value of d, excluding D( N0 ) and D( N0-1 ).  
  
Dn : Real [out]  
> d(N0), the last value of d.  
  
Dnm1 : Real [out]  
> d(N0-1).  
  
Dnm2 : Real [out]  
> d(N0-2).  
  
Ieee : Logical [in]  
> Flag for IEEE or non IEEE arithmetic.  
  
Eps : Real [in]  
> This is the value of epsilon used.  
  
