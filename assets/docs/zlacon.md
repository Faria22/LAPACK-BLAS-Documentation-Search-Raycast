```fortran  
subroutine zlacon (  
integer n,  
complex*16, dimension(n) v,  
complex*16, dimension(n) x,  
double precision est,  
integer kase  
)  
```  
  
ZLACON estimates the 1-norm of a square, complex matrix A.  
Reverse communication is used for evaluating matrix-vector products.  
  
## Parameters  
N : Integer [in]  
> The order of the matrix.  N >= 1.  
  
V : Complex*16 Array, Dimension (n) [out]  
> (W is not returned).  
  
X : Complex*16 Array, Dimension (n) [in,out]  
> On an intermediate return, X should be overwritten by  
> re-called with all the other parameters unchanged.  
  
Est : Double Precision [in,out]  
> On entry with KASE = 1 or 2 and JUMP = 3, EST should be  
> unchanged from the previous call to ZLACON.  
> On exit, EST is an estimate (a lower bound) for norm(A).  
  
Kase : Integer [in,out]  
> On the initial call to ZLACON, KASE should be 0.  
> On an intermediate return, KASE will be 1 or 2, indicating  
> On the final return from ZLACON, KASE will again be 0.  
  
