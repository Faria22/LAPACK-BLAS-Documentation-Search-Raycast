# SDOT - Single Precision Dot Product

## Purpose

SDOT forms the dot product of two vectors (single precision).

## Signature

```fortran
REAL FUNCTION SDOT(N, X, INCX, Y, INCY)
```

## Parameters

**N** : *INTEGER*
> The number of elements in vectors X and Y.

**X** : *REAL array*
> The first input vector.

**INCX** : *INTEGER*
> The increment for X.

**Y** : *REAL array*
> The second input vector.

**INCY** : *INTEGER*
> The increment for Y.

## Returns

The dot product of X and Y.
