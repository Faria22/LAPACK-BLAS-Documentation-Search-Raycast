# DZSUM1

## Function Signature

```fortran
DZSUM1(N, CX, INCX)
```

## Description


 DZSUM1 takes the sum of the absolute values of a complex
 vector and returns a double precision result.

 Based on DZASUM from the Level 1 BLAS.
 The change is to use the 'genuine' absolute value.

## Parameters

### N (in)

N is INTEGER The number of elements in the vector CX.

### CX (in)

CX is COMPLEX*16 array, dimension (N) The vector whose elements will be summed.

### INCX (in)

INCX is INTEGER The spacing between successive values of CX. INCX > 0.

