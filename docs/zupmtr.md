```fortran
subroutine zupmtr (
		side,
		uplo,
		trans,
		m,
		n,
		ap,
		tau,
		c,
		ldc,
		work,
		*                          info
)
```

 ZUPMTR overwrites the general complex M-by-N matrix C with

                 SIDE = 'L'     SIDE = 'R'
 TRANS = 'N':      Q * C          C * Q
 TRANS = 'C':      Q**H * C       C * Q**H

 where Q is a complex unitary matrix of order nq, with nq = m if
 SIDE = 'L' and nq = n if SIDE = 'R'. Q is defined as the product of
 nq-1 elementary reflectors, as returned by ZHPTRD using packed
 storage:

 if UPLO = 'U', Q = H(nq-1) . . . H(2) H(1);

 if UPLO = 'L', Q = H(1) H(2) . . . H(nq-1).

## Parameters
Side : Character*1 [in]
> = 'L': apply Q or Q**H from the Left;
> = 'R': apply Q or Q**H from the Right.

Uplo : Character*1 [in]
> = 'U': Upper triangular packed storage used in previous
> call to ZHPTRD;
> = 'L': Lower triangular packed storage used in previous
> call to ZHPTRD.

Trans : Character*1 [in]
> = 'N':  No transpose, apply Q;
> = 'C':  Conjugate transpose, apply Q**H.

M : Integer [in]
> The number of rows of the matrix C. M >= 0.

N : Integer [in]
> The number of columns of the matrix C. N >= 0.

Ap : Complex*16 Array, Dimension [in]
> (M*(M+1)/2) if SIDE = 'L'
> (N*(N+1)/2) if SIDE = 'R'
> The vectors which define the elementary reflectors, as
> returned by ZHPTRD.  AP is modified by the routine but
> restored on exit.

Tau : Complex*16 Array, Dimension (m-1) If Side = 'l' [in]
> or (N-1) if SIDE = 'R'
> TAU(i) must contain the scalar factor of the elementary
> reflector H(i), as returned by ZHPTRD.

C : Complex*16 Array, Dimension (ldc,n) [in,out]
> On entry, the M-by-N matrix C.
> On exit, C is overwritten by Q*C or Q**H*C or C*Q**H or C*Q.

Ldc : Integer [in]
> The leading dimension of the array C. LDC >= max(1,M).

Work : Complex*16 Array, Dimension [out]
> (N) if SIDE = 'L'
> (M) if SIDE = 'R'

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value

