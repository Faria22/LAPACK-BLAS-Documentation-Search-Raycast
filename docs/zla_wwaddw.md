# ZLA_WWADDW

## Function Signature

```fortran
ZLA_WWADDW(N, X, Y, W)
```

## Description


    ZLA_WWADDW adds a vector W into a doubled-single vector (X, Y).

    This works for all extant IBM's hex and binary floating point
    arithmetic, but not for decimal.

## Parameters

### N (in)

N is INTEGER The length of vectors X, Y, and W.

### X (in,out)

X is COMPLEX*16 array, dimension (N) The first part of the doubled-single accumulation vector.

### Y (in,out)

Y is COMPLEX*16 array, dimension (N) The second part of the doubled-single accumulation vector.

### W (in)

W is COMPLEX*16 array, dimension (N) The vector to be added.

