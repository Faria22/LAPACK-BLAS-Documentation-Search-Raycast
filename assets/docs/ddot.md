# DDOT - Double Precision Dot Product

## Purpose

DDOT forms the dot product of two vectors:

```
result := x^T * y
```

## Signature

```fortran
DOUBLE PRECISION FUNCTION DDOT(N, X, INCX, Y, INCY)
```

## Parameters

**N** : *INTEGER*
> The number of elements in vectors X and Y.

**X** : *DOUBLE PRECISION array, dimension (1 + (N-1)*abs(INCX))*
> The first input vector.

**INCX** : *INTEGER*
> The increment for the elements of X.

**Y** : *DOUBLE PRECISION array, dimension (1 + (N-1)*abs(INCY))*
> The second input vector.

**INCY** : *INTEGER*
> The increment for the elements of Y.

## Returns

The dot product of vectors X and Y.

## Notes

DDOT is a Level 1 BLAS routine.
