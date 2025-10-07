```fortran
subroutine dlarnv	(	integer	idist,
		integer, dimension(4)	iseed,
		integer	n,
		double precision, dimension(*)	x )
```

 DLARNV returns a vector of n random real numbers from a uniform or
 normal distribution.

## Parameters
Idist : Integer [in]
> Specifies the distribution of the random numbers:
> = 1:  uniform (0,1)
> = 2:  uniform (-1,1)
> = 3:  normal (0,1)

Iseed : Integer Array, Dimension (4) [in,out]
> On entry, the seed of the random number generator; the array
> elements must be between 0 and 4095, and ISEED(4) must be
> odd.
> On exit, the seed is updated.

N : Integer [in]
> The number of random numbers to be generated.

X : Double Precision Array, Dimension (n) [out]
> The generated random numbers.

