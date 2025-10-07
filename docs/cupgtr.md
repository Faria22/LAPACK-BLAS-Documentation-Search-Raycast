```fortran
subroutine cupgtr (
		character uplo,
		integer n,
		complex, dimension(*) ap,
		complex, dimension(*) tau,
		complex, dimension(ldq, *) q,
		integer ldq,
		complex, dimension(*) work,
		integer info
)
```

 CUPGTR generates a complex unitary matrix Q which is defined as the
 product of n-1 elementary reflectors H(i) of order n, as returned by
 CHPTRD using packed storage:

 if UPLO = 'U', Q = H(n-1) . . . H(2) H(1),

 if UPLO = 'L', Q = H(1) H(2) . . . H(n-1).

## Parameters
Uplo : Character*1 [in]
> = 'U': Upper triangular packed storage used in previous
> call to CHPTRD;
> = 'L': Lower triangular packed storage used in previous
> call to CHPTRD.

N : Integer [in]
> The order of the matrix Q. N >= 0.

Ap : Complex Array, Dimension (n*(n+1)/2) [in]
> The vectors which define the elementary reflectors, as
> returned by CHPTRD.

Tau : Complex Array, Dimension (n-1) [in]
> TAU(i) must contain the scalar factor of the elementary
> reflector H(i), as returned by CHPTRD.

Q : Complex Array, Dimension (ldq,n) [out]
> The N-by-N unitary matrix Q.

Ldq : Integer [in]
> The leading dimension of the array Q. LDQ >= max(1,N).

Work : Complex Array, Dimension (n-1) [out]

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value

