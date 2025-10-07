# ZLACON

## Function Signature

```fortran
ZLACON(N, V, X, EST, KASE)
```

## Description


 ZLACON estimates the 1-norm of a square, complex matrix A.
 Reverse communication is used for evaluating matrix-vector products.

## Parameters

### N (in)

N is INTEGER The order of the matrix. N >= 1.

### V (out)

V is COMPLEX*16 array, dimension (N) On the final return, V = A*W, where EST = norm(V)/norm(W) (W is not returned).

### X (in,out)

X is COMPLEX*16 array, dimension (N) On an intermediate return, X should be overwritten by A * X, if KASE=1, A**H * X, if KASE=2, where A**H is the conjugate transpose of A, and ZLACON must be re-called with all the other parameters unchanged.

### EST (in,out)

EST is DOUBLE PRECISION On entry with KASE = 1 or 2 and JUMP = 3, EST should be unchanged from the previous call to ZLACON. On exit, EST is an estimate (a lower bound) for norm(A).

### KASE (in,out)

KASE is INTEGER On the initial call to ZLACON, KASE should be 0. On an intermediate return, KASE will be 1 or 2, indicating whether X should be overwritten by A * X or A**H * X. On the final return from ZLACON, KASE will again be 0.

