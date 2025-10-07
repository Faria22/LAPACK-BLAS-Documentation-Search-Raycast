```fortran
subroutine zupgtr	(	character	uplo,
		integer	n,
		complex*16, dimension(*)	ap,
		complex*16, dimension(*)	tau,
		complex*16, dimension(ldq, *)	q,
		integer	ldq,
		complex*16, dimension(*)	work,
		integer	info )
```

 ZUPGTR generates a complex unitary matrix Q which is defined as the
 product of n-1 elementary reflectors H(i) of order n, as returned by
 ZHPTRD using packed storage:

 if UPLO = 'U', Q = H(n-1) . . . H(2) H(1),

 if UPLO = 'L', Q = H(1) H(2) . . . H(n-1).

## Parameters
Uplo : Character*1 [in]
> = 'U': Upper triangular packed storage used in previous
> call to ZHPTRD;
> = 'L': Lower triangular packed storage used in previous
> call to ZHPTRD.

N : Integer [in]
> The order of the matrix Q. N >= 0.

Ap : Complex*16 Array, Dimension (n*(n+1)/2) [in]
> The vectors which define the elementary reflectors, as
> returned by ZHPTRD.

Tau : Complex*16 Array, Dimension (n-1) [in]
> TAU(i) must contain the scalar factor of the elementary
> reflector H(i), as returned by ZHPTRD.

Q : Complex*16 Array, Dimension (ldq,n) [out]
> The N-by-N unitary matrix Q.

Ldq : Integer [in]
> The leading dimension of the array Q. LDQ >= max(1,N).

Work : Complex*16 Array, Dimension (n-1) [out]

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value

