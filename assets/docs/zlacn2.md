```fortran  
subroutine zlacn2 (  
integer n,  
complex*16, dimension(*) v,  
complex*16, dimension(*) x,  
double precision est,  
integer kase,  
integer, dimension(3) isave  
)  
```  
  
ZLACN2 estimates the 1-norm of a square, complex matrix A.  
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
> On entry with KASE = 1 or 2 and ISAVE(1) = 3, EST should be  
> unchanged from the previous call to ZLACN2.  
> On exit, EST is an estimate (a lower bound) for norm(A).  
  
Kase : Integer [in,out]  
> On the initial call to ZLACN2, KASE should be 0.  
> On an intermediate return, KASE will be 1 or 2, indicating  
> On the final return from ZLACN2, KASE will again be 0.  
  
Isave : Integer Array, Dimension (3) [in,out]  
> ISAVE is used to save variables between calls to ZLACN2  
  
