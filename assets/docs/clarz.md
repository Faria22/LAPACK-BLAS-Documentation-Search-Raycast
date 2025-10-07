```fortran  
subroutine clarz (  
character side,  
integer m,  
integer n,  
integer l,  
complex, dimension(*) v,  
integer incv,  
complex tau,  
complex, dimension(ldc, *) c,  
integer ldc,  
complex, dimension(*) work  
)  
```  
  
CLARZ applies a complex elementary reflector H to a complex  
M-by-N matrix C, from either the left or the right. H is represented  
in the form  
  
H = I - tau * v * v**H  
  
where tau is a complex scalar and v is a complex vector.  
  
If tau = 0, then H is taken to be the unit matrix.  
  
To apply H**H (the conjugate transpose of H), supply conjg(tau) instead  
tau.  
  
H is a product of k elementary reflectors as returned by CTZRZF.  
  
## Parameters  
Side : Character*1 [in]  
  
M : Integer [in]  
> The number of rows of the matrix C.  
  
N : Integer [in]  
> The number of columns of the matrix C.  
  
L : Integer [in]  
> The number of entries of the vector V containing  
> the meaningful part of the Householder vectors.  
> If SIDE = 'L', M >= L >= 0, if SIDE = 'R', N >= L >= 0.  
  
V : Complex Array, Dimension (1+(l-1)*abs(incv)) [in]  
> The vector v in the representation of H as returned by  
> CTZRZF. V is not used if TAU = 0.  
  
Incv : Integer [in]  
> The increment between elements of v. INCV <> 0.  
  
Tau : Complex [in]  
> The value tau in the representation of H.  
  
C : Complex Array, Dimension (ldc,n) [in,out]  
> On entry, the M-by-N matrix C.  
  
Ldc : Integer [in]  
> The leading dimension of the array C. LDC >= max(1,M).  
  
Work : Complex Array, Dimension [out]  
> (N) if SIDE = 'L'  
> or (M) if SIDE = 'R'  
  
