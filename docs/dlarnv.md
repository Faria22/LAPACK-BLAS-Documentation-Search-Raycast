# DLARNV

## Function Signature

```fortran
DLARNV(IDIST, ISEED, N, X)
```

## Description


 DLARNV returns a vector of n random real numbers from a uniform or
 normal distribution.

## Parameters

### IDIST (in)

IDIST is INTEGER Specifies the distribution of the random numbers: = 1: uniform (0,1) = 2: uniform (-1,1) = 3: normal (0,1)

### ISEED (in,out)

ISEED is INTEGER array, dimension (4) On entry, the seed of the random number generator; the array elements must be between 0 and 4095, and ISEED(4) must be odd. On exit, the seed is updated.

### N (in)

N is INTEGER The number of random numbers to be generated.

### X (out)

X is DOUBLE PRECISION array, dimension (N) The generated random numbers.

