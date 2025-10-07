```fortran  
subroutine slaev2 (  
real a,  
real b,  
real c,  
real rt1,  
real rt2,  
real cs1,  
real sn1  
)  
```  
  
SLAEV2 computes the eigendecomposition of a 2-by-2 symmetric matrix  
[  A   B  ]  
[  B   C  ].  
On return, RT1 is the eigenvalue of larger absolute value, RT2 is the  
eigenvalue of smaller absolute value, and (CS1,SN1) is the unit right  
eigenvector for RT1, giving the decomposition  
  
[ CS1  SN1 ] [  A   B  ] [ CS1 -SN1 ]  =  [ RT1  0  ]  
[-SN1  CS1 ] [  B   C  ] [ SN1  CS1 ]     [  0  RT2 ].  
  
## Parameters  
A : Real [in]  
> The (1,1) element of the 2-by-2 matrix.  
  
B : Real [in]  
> The (1,2) element and the conjugate of the (2,1) element of  
> the 2-by-2 matrix.  
  
C : Real [in]  
> The (2,2) element of the 2-by-2 matrix.  
  
Rt1 : Real [out]  
> The eigenvalue of larger absolute value.  
  
Rt2 : Real [out]  
> The eigenvalue of smaller absolute value.  
  
Cs1 : Real [out]  
  
Sn1 : Real [out]  
> The vector (CS1, SN1) is a unit right eigenvector for RT1.  
  
