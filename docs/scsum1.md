# SCSUM1

## Function Signature

```fortran
SCSUM1(N, CX, INCX)
```

## Description


 SCSUM1 takes the sum of the absolute values of a complex
 vector and returns a single precision result.

 Based on SCASUM from the Level 1 BLAS.
 The change is to use the 'genuine' absolute value.

## Parameters

### N (in)

N is INTEGER The number of elements in the vector CX.

### CX (in)

CX is COMPLEX array, dimension (N) The vector whose elements will be summed.

### INCX (in)

INCX is INTEGER The spacing between successive values of CX. INCX > 0.

