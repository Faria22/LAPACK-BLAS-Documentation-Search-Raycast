# SSTERF

## Function Signature

```fortran
SSTERF(N, D, E, INFO)
```

## Description


 SSTERF computes all eigenvalues of a symmetric tridiagonal matrix
 using the Pal-Walker-Kahan variant of the QL or QR algorithm.

## Parameters

### N (in)

N is INTEGER The order of the matrix. N >= 0.

### D (in,out)

D is REAL array, dimension (N) On entry, the n diagonal elements of the tridiagonal matrix. On exit, if INFO = 0, the eigenvalues in ascending order.

### E (in,out)

E is REAL array, dimension (N-1) On entry, the (n-1) subdiagonal elements of the tridiagonal matrix. On exit, E has been destroyed.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value > 0: the algorithm failed to find all of the eigenvalues in a total of 30*N iterations; if INFO = i, then i elements of E have not converged to zero.

