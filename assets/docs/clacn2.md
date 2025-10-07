```fortran
subroutine clacn2 (
		integer n,
		complex, dimension(*) v,
		complex, dimension(*) x,
		real est,
		integer kase,
		integer, dimension(3) isave
)
```

 CLACN2 estimates the 1-norm of a square, complex matrix A.
 Reverse communication is used for evaluating matrix-vector products.

## Parameters
N : Integer [in]
> The order of the matrix.  N >= 1.

V : Complex Array, Dimension (n) [out]
> On the final return, V = A*W,  where  EST = norm(V)/norm(W)
> (W is not returned).

X : Complex Array, Dimension (n) [in,out]
> On an intermediate return, X should be overwritten by
> A * X,   if KASE=1,
> A**H * X,  if KASE=2,
> where A**H is the conjugate transpose of A, and CLACN2 must be
> re-called with all the other parameters unchanged.

Est : Real [in,out]
> On entry with KASE = 1 or 2 and ISAVE(1) = 3, EST should be
> unchanged from the previous call to CLACN2.
> On exit, EST is an estimate (a lower bound) for norm(A).

Kase : Integer [in,out]
> On the initial call to CLACN2, KASE should be 0.
> On an intermediate return, KASE will be 1 or 2, indicating
> whether X should be overwritten by A * X  or A**H * X.
> On the final return from CLACN2, KASE will again be 0.

Isave : Integer Array, Dimension (3) [in,out]
> ISAVE is used to save variables between calls to SLACN2

