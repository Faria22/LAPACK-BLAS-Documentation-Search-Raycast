# IZMAX1

## Function Signature

```fortran
IZMAX1(N, ZX, INCX)
```

## Description


 IZMAX1 finds the index of the first vector element of maximum absolute value.

 Based on IZAMAX from Level 1 BLAS.
 The change is to use the 'genuine' absolute value.

## Parameters

### N (in)

N is INTEGER The number of elements in the vector ZX.

### ZX (in)

ZX is COMPLEX*16 array, dimension (N) The vector ZX. The IZMAX1 function returns the index of its first element of maximum absolute value.

### INCX (in)

INCX is INTEGER The spacing between successive values of ZX. INCX >= 1.

