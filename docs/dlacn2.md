# DLACN2

## Function Signature

```fortran
DLACN2(N, V, X, ISGN, EST, KASE, ISAVE)
```

## Description


 DLACN2 estimates the 1-norm of a square, real matrix A.
 Reverse communication is used for evaluating matrix-vector products.

## Parameters

### N (in)

N is INTEGER The order of the matrix. N >= 1.

### V (out)

V is DOUBLE PRECISION array, dimension (N) On the final return, V = A*W, where EST = norm(V)/norm(W) (W is not returned).

### X (in,out)

X is DOUBLE PRECISION array, dimension (N) On an intermediate return, X should be overwritten by A * X, if KASE=1, A**T * X, if KASE=2, and DLACN2 must be re-called with all the other parameters unchanged.

### ISGN (out)

ISGN is INTEGER array, dimension (N)

### EST (in,out)

EST is DOUBLE PRECISION On entry with KASE = 1 or 2 and ISAVE(1) = 3, EST should be unchanged from the previous call to DLACN2. On exit, EST is an estimate (a lower bound) for norm(A).

### KASE (in,out)

KASE is INTEGER On the initial call to DLACN2, KASE should be 0. On an intermediate return, KASE will be 1 or 2, indicating whether X should be overwritten by A * X or A**T * X. On the final return from DLACN2, KASE will again be 0.

### ISAVE (in,out)

ISAVE is INTEGER array, dimension (3) ISAVE is used to save variables between calls to DLACN2

