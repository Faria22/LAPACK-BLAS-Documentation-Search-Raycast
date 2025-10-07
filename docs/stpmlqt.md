```fortran
subroutine stpmlqt (
		side,
		trans,
		m,
		n,
		k,
		l,
		mb,
		v,
		ldv,
		t,
		ldt,
		*                           a,
		lda,
		b,
		ldb,
		work,
		info
)
```

 STPMLQT applies a real orthogonal matrix Q obtained from a
 "triangular-pentagonal" real block reflector H to a general
 real matrix C, which consists of two blocks A and B.

## Parameters
Side : Character*1 [in]
> = 'L': apply Q or Q**T from the Left;
> = 'R': apply Q or Q**T from the Right.

Trans : Character*1 [in]
> = 'N':  No transpose, apply Q;
> = 'T':  Transpose, apply Q**T.

M : Integer [in]
> The number of rows of the matrix B. M >= 0.

N : Integer [in]
> The number of columns of the matrix B. N >= 0.

K : Integer [in]
> The number of elementary reflectors whose product defines
> the matrix Q.

L : Integer [in]
> The order of the trapezoidal part of V.
> K >= L >= 0.  See Further Details.

Mb : Integer [in]
> The block size used for the storage of T.  K >= MB >= 1.
> This must be the same value of MB used to generate T
> in STPLQT.

V : Real Array, Dimension (ldv,k) [in]
> The i-th row must contain the vector which defines the
> elementary reflector H(i), for i = 1,2,...,k, as returned by
> STPLQT in B.  See Further Details.

Ldv : Integer [in]
> The leading dimension of the array V. LDV >= K.

T : Real Array, Dimension (ldt,k) [in]
> The upper triangular factors of the block reflectors
> as returned by STPLQT, stored as a MB-by-K matrix.

Ldt : Integer [in]
> The leading dimension of the array T.  LDT >= MB.

A : Real Array, Dimension [in,out]
> (LDA,N) if SIDE = 'L' or
> (LDA,K) if SIDE = 'R'
> On entry, the K-by-N or M-by-K matrix A.
> On exit, A is overwritten by the corresponding block of
> Q*C or Q**T*C or C*Q or C*Q**T.  See Further Details.

Lda : Integer [in]
> The leading dimension of the array A.
> If SIDE = 'L', LDA >= max(1,K);
> If SIDE = 'R', LDA >= max(1,M).

B : Real Array, Dimension (ldb,n) [in,out]
> On entry, the M-by-N matrix B.
> On exit, B is overwritten by the corresponding block of
> Q*C or Q**T*C or C*Q or C*Q**T.  See Further Details.

Ldb : Integer [in]
> The leading dimension of the array B.
> LDB >= max(1,M).

Work : Real Array. The Dimension of Work is [out]
> N*MB if SIDE = 'L', or  M*MB if SIDE = 'R'.

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value

