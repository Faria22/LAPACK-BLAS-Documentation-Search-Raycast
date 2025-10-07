# DAXPY - Double Precision Constant times a Vector Plus a Vector

## Purpose

DAXPY computes the operation:

```
y := alpha*x + y
```

where alpha is a scalar, and x and y are vectors.

## Signature

```fortran
SUBROUTINE DAXPY(N, ALPHA, X, INCX, Y, INCY)
```

## Parameters

**N** : *INTEGER*
> The number of elements in vectors X and Y.

**ALPHA** : *DOUBLE PRECISION*
> The scalar alpha.

**X** : *DOUBLE PRECISION array, dimension (1 + (N-1)*abs(INCX))*
> The input vector X.

**INCX** : *INTEGER*
> The increment for the elements of X. INCX must not be zero.

**Y** : *DOUBLE PRECISION array, dimension (1 + (N-1)*abs(INCY))*
> On entry, the input vector Y. On exit, Y is overwritten with the result alpha*X + Y.

**INCY** : *INTEGER*
> The increment for the elements of Y. INCY must not be zero.
