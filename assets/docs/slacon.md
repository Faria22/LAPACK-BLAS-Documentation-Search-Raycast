```fortran  
subroutine slacon (  
integer n,  
real, dimension(*) v,  
real, dimension(*) x,  
integer, dimension(*) isgn,  
real est,  
integer kase  
)  
```  
  
SLACON estimates the 1-norm of a square, real matrix A.  
Reverse communication is used for evaluating matrix-vector products.  
  
## Parameters  
N : Integer [in]  
> The order of the matrix.  N >= 1.  
  
V : Real Array, Dimension (n) [out]  
> (W is not returned).  
  
X : Real Array, Dimension (n) [in,out]  
> On an intermediate return, X should be overwritten by  
> and SLACON must be re-called with all the other parameters  
> unchanged.  
  
Isgn : Integer Array, Dimension (n) [out]  
  
Est : Real [in,out]  
> On entry with KASE = 1 or 2 and JUMP = 3, EST should be  
> unchanged from the previous call to SLACON.  
> On exit, EST is an estimate (a lower bound) for norm(A).  
  
Kase : Integer [in,out]  
> On the initial call to SLACON, KASE should be 0.  
> On an intermediate return, KASE will be 1 or 2, indicating  
> On the final return from SLACON, KASE will again be 0.  
  
