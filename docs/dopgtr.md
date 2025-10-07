```fortran
subroutine dopgtr	(	character	uplo,
		integer	n,
		double precision, dimension(*)	ap,
		double precision, dimension(*)	tau,
		double precision, dimension(ldq, *)	q,
		integer	ldq,
		double precision, dimension(*)	work,
		integer	info )
```

 DOPGTR generates a real orthogonal matrix Q which is defined as the
 product of n-1 elementary reflectors H(i) of order n, as returned by
 DSPTRD using packed storage:

 if UPLO = 'U', Q = H(n-1) . . . H(2) H(1),

 if UPLO = 'L', Q = H(1) H(2) . . . H(n-1).

## Parameters
Uplo : Character*1 [in]
> = 'U': Upper triangular packed storage used in previous
> call to DSPTRD;
> = 'L': Lower triangular packed storage used in previous
> call to DSPTRD.

N : Integer [in]
> The order of the matrix Q. N >= 0.

Ap : Double Precision Array, Dimension (n*(n+1)/2) [in]
> The vectors which define the elementary reflectors, as
> returned by DSPTRD.

Tau : Double Precision Array, Dimension (n-1) [in]
> TAU(i) must contain the scalar factor of the elementary
> reflector H(i), as returned by DSPTRD.

Q : Double Precision Array, Dimension (ldq,n) [out]
> The N-by-N orthogonal matrix Q.

Ldq : Integer [in]
> The leading dimension of the array Q. LDQ >= max(1,N).

Work : Double Precision Array, Dimension (n-1) [out]

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value

