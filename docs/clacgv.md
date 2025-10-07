# CLACGV

## Function Signature

```fortran
CLACGV(N, X, INCX)
```

## Description


 CLACGV conjugates a complex vector of length N.

## Parameters

### N (in)

N is INTEGER The length of the vector X. N >= 0.

### X (in,out)

X is COMPLEX array, dimension (1+(N-1)*abs(INCX)) On entry, the vector of length N to be conjugated. On exit, X is overwritten with conjg(X).

### INCX (in)

INCX is INTEGER The spacing between successive elements of X.

