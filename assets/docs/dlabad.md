```fortran  
subroutine dlabad (  
double precision small,  
double precision large  
)  
```  
  
DLABAD is a no-op and kept for compatibility reasons. It used  
to correct the overflow/underflow behavior of machines that  
are not IEEE-754 compliant.  
  
  
## Parameters  
Small : Double Precision [in,out]  
> On entry, the underflow threshold as computed by DLAMCH.  
> On exit, the unchanged value SMALL.  
  
Large : Double Precision [in,out]  
> On entry, the overflow threshold as computed by DLAMCH.  
> On exit, the unchanged value LARGE.  
  
