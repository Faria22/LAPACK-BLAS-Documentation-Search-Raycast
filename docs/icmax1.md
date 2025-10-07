# ICMAX1

## Function Signature

```fortran
ICMAX1(N, CX, INCX)
```

## Description


 ICMAX1 finds the index of the first vector element of maximum absolute value.

 Based on ICAMAX from Level 1 BLAS.
 The change is to use the 'genuine' absolute value.

## Parameters

### N (in)

N is INTEGER The number of elements in the vector CX.

### CX (in)

CX is COMPLEX array, dimension (N) The vector CX. The ICMAX1 function returns the index of its first element of maximum absolute value.

### INCX (in)

INCX is INTEGER The spacing between successive values of CX. INCX >= 1.

