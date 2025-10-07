```fortran  
subroutine clacon (  
integer n,  
complex, dimension(n) v,  
complex, dimension(n) x,  
real est,  
integer kase  
)  
```  
  
CLACON estimates the 1-norm of a square, complex matrix A.  
Reverse communication is used for evaluating matrix-vector products.  
  
## Parameters  
N : Integer [in]  
> The order of the matrix.  N >= 1.  
  
V : Complex Array, Dimension (n) [out]  
> (W is not returned).  
  
X : Complex Array, Dimension (n) [in,out]  
> On an intermediate return, X should be overwritten by  
> re-called with all the other parameters unchanged.  
  
Est : Real [in,out]  
> On entry with KASE = 1 or 2 and JUMP = 3, EST should be  
> unchanged from the previous call to CLACON.  
> On exit, EST is an estimate (a lower bound) for norm(A).  
  
Kase : Integer [in,out]  
> On the initial call to CLACON, KASE should be 0.  
> On an intermediate return, KASE will be 1 or 2, indicating  
> On the final return from CLACON, KASE will again be 0.  
  
