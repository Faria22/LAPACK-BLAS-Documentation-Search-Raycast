```fortran  
subroutine dlarrc (  
jobt,  
n,  
vl,  
vu,  
d,  
e,  
pivmin,  
*                                   eigcnt,  
lcnt,  
rcnt,  
info  
)  
```  
  
Find the number of eigenvalues of the symmetric tridiagonal matrix T  
that are in the interval (VL,VU] if JOBT = 'T', and of L D L^T  
if JOBT = 'L'.  
  
## Parameters  
Jobt : Character*1 [in]  
> = 'T':  Compute Sturm count for matrix T.  
> = 'L':  Compute Sturm count for matrix L D L^T.  
  
N : Integer [in]  
> The order of the matrix. N > 0.  
  
Vl : Double Precision [in]  
> The lower bound for the eigenvalues.  
  
Vu : Double Precision [in]  
> The upper bound for the eigenvalues.  
  
D : Double Precision Array, Dimension (n) [in]  
> JOBT = 'T': The N diagonal elements of the tridiagonal matrix T.  
> JOBT = 'L': The N diagonal elements of the diagonal matrix D.  
  
E : Double Precision Array, Dimension (n) [in]  
> JOBT = 'T': The N-1 offdiagonal elements of the matrix T.  
> JOBT = 'L': The N-1 offdiagonal elements of the matrix L.  
  
Pivmin : Double Precision [in]  
> The minimum pivot in the Sturm sequence for T.  
  
Eigcnt : Integer [out]  
> The number of eigenvalues of the symmetric tridiagonal matrix T  
> that are in the interval (VL,VU]  
  
Lcnt : Integer [out]  
  
Rcnt : Integer [out]  
> The left and right negcounts of the interval.  
  
Info : Integer [out]  
  
