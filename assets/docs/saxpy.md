# SAXPY - Single Precision Constant times a Vector Plus a Vector

## Purpose

SAXPY computes the operation:

```
y := alpha*x + y
```

## Signature

```fortran
SUBROUTINE SAXPY(N, ALPHA, X, INCX, Y, INCY)
```

## Parameters

**N** : *INTEGER*
> The number of elements in vectors X and Y.

**ALPHA** : *REAL*
> The scalar alpha.

**X** : *REAL array, dimension (1 + (N-1)*abs(INCX))*
> The input vector X.

**INCX** : *INTEGER*
> The increment for the elements of X. INCX must not be zero.

**Y** : *REAL array, dimension (1 + (N-1)*abs(INCY))*
> On entry, the input vector Y. On exit, Y is overwritten with alpha*X + Y.

**INCY** : *INTEGER*
> The increment for the elements of Y. INCY must not be zero.
