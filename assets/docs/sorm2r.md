```fortran
subroutine sorm2r (
		side,
		trans,
		m,
		n,
		k,
		a,
		lda,
		tau,
		c,
		ldc,
		*                          work,
		info
)
```

 SORM2R overwrites the general real m by n matrix C with

       Q * C  if SIDE = 'L' and TRANS = 'N', or

       Q**T* C  if SIDE = 'L' and TRANS = 'T', or

       C * Q  if SIDE = 'R' and TRANS = 'N', or

       C * Q**T if SIDE = 'R' and TRANS = 'T',

 where Q is a real orthogonal matrix defined as the product of k
 elementary reflectors

       Q = H(1) H(2) . . . H(k)

 as returned by SGEQRF. Q is of order m if SIDE = 'L' and of order n
 if SIDE = 'R'.

## Parameters
Side : Character*1 [in]
> = 'L': apply Q or Q**T from the Left
> = 'R': apply Q or Q**T from the Right

Trans : Character*1 [in]
> = 'N': apply Q  (No transpose)
> = 'T': apply Q**T (Transpose)

M : Integer [in]
> The number of rows of the matrix C. M >= 0.

N : Integer [in]
> The number of columns of the matrix C. N >= 0.

K : Integer [in]
> The number of elementary reflectors whose product defines
> the matrix Q.
> If SIDE = 'L', M >= K >= 0;
> if SIDE = 'R', N >= K >= 0.

A : Real Array, Dimension (lda,k) [in]
> The i-th column must contain the vector which defines the
> elementary reflector H(i), for i = 1,2,...,k, as returned by
> SGEQRF in the first k columns of its array argument A.
> A is modified by the routine but restored on exit.

Lda : Integer [in]
> The leading dimension of the array A.
> If SIDE = 'L', LDA >= max(1,M);
> if SIDE = 'R', LDA >= max(1,N).

Tau : Real Array, Dimension (k) [in]
> TAU(i) must contain the scalar factor of the elementary
> reflector H(i), as returned by SGEQRF.

C : Real Array, Dimension (ldc,n) [in,out]
> On entry, the m by n matrix C.
> On exit, C is overwritten by Q*C or Q**T*C or C*Q**T or C*Q.

Ldc : Integer [in]
> The leading dimension of the array C. LDC >= max(1,M).

Work : Real Array, Dimension [out]
> (N) if SIDE = 'L',
> (M) if SIDE = 'R'

Info : Integer [out]
> = 0: successful exit
> < 0: if INFO = -i, the i-th argument had an illegal value

