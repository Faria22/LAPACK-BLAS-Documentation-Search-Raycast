# SLARRR

## Function Signature

```fortran
SLARRR(N, D, E, INFO)
```

## Description


 Perform tests to decide whether the symmetric tridiagonal matrix T
 warrants expensive computations which guarantee high relative accuracy
 in the eigenvalues.

## Parameters

### N (in)

N is INTEGER The order of the matrix. N > 0.

### D (in)

D is REAL array, dimension (N) The N diagonal elements of the tridiagonal matrix T.

### E (in,out)

E is REAL array, dimension (N) On entry, the first (N-1) entries contain the subdiagonal elements of the tridiagonal matrix T; E(N) is set to ZERO.

### INFO (out)

INFO is INTEGER INFO = 0(default) : the matrix warrants computations preserving relative accuracy. INFO = 1 : the matrix warrants computations guaranteeing only absolute accuracy.

