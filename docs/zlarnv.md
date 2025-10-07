```fortran
subroutine zlarnv	(	integer	idist,
		integer, dimension(4)	iseed,
		integer	n,
		complex*16, dimension(*)	x )
```

 ZLARNV returns a vector of n random complex numbers from a uniform or
 normal distribution.

## Parameters
Idist : Integer [in]
> Specifies the distribution of the random numbers:
> = 1:  real and imaginary parts each uniform (0,1)
> = 2:  real and imaginary parts each uniform (-1,1)
> = 3:  real and imaginary parts each normal (0,1)
> = 4:  uniformly distributed on the disc abs(z) < 1
> = 5:  uniformly distributed on the circle abs(z) = 1

Iseed : Integer Array, Dimension (4) [in,out]
> On entry, the seed of the random number generator; the array
> elements must be between 0 and 4095, and ISEED(4) must be
> odd.
> On exit, the seed is updated.

N : Integer [in]
> The number of random numbers to be generated.

X : Complex*16 Array, Dimension (n) [out]
> The generated random numbers.

