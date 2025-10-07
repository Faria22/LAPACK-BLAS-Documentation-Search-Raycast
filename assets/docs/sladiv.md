```fortran  
subroutine sladiv (  
real a,  
real b,  
real c,  
real d,  
real p,  
real q  
)  
```  
  
SLADIV performs complex division in  real arithmetic  
  
a + i*b  
p + i*q = ---------  
c + i*d  
  
The algorithm is due to Michael Baudin and Robert L. Smith  
and can be found in the paper  
"A Robust Complex Division in Scilab"  
  
## Parameters  
A : Real [in]  
  
B : Real [in]  
  
C : Real [in]  
  
D : Real [in]  
> The scalars a, b, c, and d in the above expression.  
  
P : Real [out]  
  
Q : Real [out]  
> The scalars p and q in the above expression.  
  
