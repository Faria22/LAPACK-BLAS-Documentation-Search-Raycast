# DLARUV

## Function Signature

```fortran
DLARUV(ISEED, N, X)
```

## Description


 DLARUV returns a vector of n random real numbers from a uniform (0,1)
 distribution (n <= 128).

 This is an auxiliary routine called by DLARNV and ZLARNV.

## Parameters

### ISEED (in,out)

ISEED is INTEGER array, dimension (4) On entry, the seed of the random number generator; the array elements must be between 0 and 4095, and ISEED(4) must be odd. On exit, the seed is updated.

### N (in)

N is INTEGER The number of random numbers to be generated. N <= 128.

### X (out)

X is DOUBLE PRECISION array, dimension (N) The generated random numbers.

