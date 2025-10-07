# ZLARNV

## Function Signature

```fortran
ZLARNV(IDIST, ISEED, N, X)
```

## Description


 ZLARNV returns a vector of n random complex numbers from a uniform or
 normal distribution.

## Parameters

### IDIST (in)

IDIST is INTEGER Specifies the distribution of the random numbers: = 1: real and imaginary parts each uniform (0,1) = 2: real and imaginary parts each uniform (-1,1) = 3: real and imaginary parts each normal (0,1) = 4: uniformly distributed on the disc abs(z) < 1 = 5: uniformly distributed on the circle abs(z) = 1

### ISEED (in,out)

ISEED is INTEGER array, dimension (4) On entry, the seed of the random number generator; the array elements must be between 0 and 4095, and ISEED(4) must be odd. On exit, the seed is updated.

### N (in)

N is INTEGER The number of random numbers to be generated.

### X (out)

X is COMPLEX*16 array, dimension (N) The generated random numbers.

