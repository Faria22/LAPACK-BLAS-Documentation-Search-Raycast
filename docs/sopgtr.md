```fortran
subroutine sopgtr	(	character	uplo,
		integer	n,
		real, dimension(*)	ap,
		real, dimension(*)	tau,
		real, dimension(ldq, *)	q,
		integer	ldq,
		real, dimension(*)	work,
		integer	info )
```

 SOPGTR generates a real orthogonal matrix Q which is defined as the
 product of n-1 elementary reflectors H(i) of order n, as returned by
 SSPTRD using packed storage:

 if UPLO = 'U', Q = H(n-1) . . . H(2) H(1),

 if UPLO = 'L', Q = H(1) H(2) . . . H(n-1).

## Parameters
Uplo : Character*1 [in]
> = 'U': Upper triangular packed storage used in previous
> call to SSPTRD;
> = 'L': Lower triangular packed storage used in previous
> call to SSPTRD.

N : Integer [in]
> The order of the matrix Q. N >= 0.

Ap : Real Array, Dimension (n*(n+1)/2) [in]
> The vectors which define the elementary reflectors, as
> returned by SSPTRD.

Tau : Real Array, Dimension (n-1) [in]
> TAU(i) must contain the scalar factor of the elementary
> reflector H(i), as returned by SSPTRD.

Q : Real Array, Dimension (ldq,n) [out]
> The N-by-N orthogonal matrix Q.

Ldq : Integer [in]
> The leading dimension of the array Q. LDQ >= max(1,N).

Work : Real Array, Dimension (n-1) [out]

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value

