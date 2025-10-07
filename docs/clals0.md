```fortran
subroutine clals0	(	icompq,
		nl,
		nr,
		sqre,
		nrhs,
		b,
		ldb,
		bx,
		ldbx,
		*                          perm,
		givptr,
		givcol,
		ldgcol,
		givnum,
		ldgnum,
		*                          poles,
		difl,
		difr,
		z,
		k,
		c,
		s,
		rwork,
		info )
```

 CLALS0 applies back the multiplying factors of either the left or the
 right singular vector matrix of a diagonal matrix appended by a row
 to the right hand side matrix B in solving the least squares problem
 using the divide-and-conquer SVD approach.

 For the left singular vector matrix, three types of orthogonal
 matrices are involved:

 (1L) Givens rotations: the number of such rotations is GIVPTR; the
      pairs of columns/rows they were applied to are stored in GIVCOL;
      and the C- and S-values of these rotations are stored in GIVNUM.

 (2L) Permutation. The (NL+1)-st row of B is to be moved to the first
      row, and for J=2:N, PERM(J)-th row of B is to be moved to the
      J-th row.

 (3L) The left singular vector matrix of the remaining matrix.

 For the right singular vector matrix, four types of orthogonal
 matrices are involved:

 (1R) The right singular vector matrix of the remaining matrix.

 (2R) If SQRE = 1, one extra Givens rotation to generate the right
      null space.

 (3R) The inverse transformation of (2L).

 (4R) The inverse transformation of (1L).

## Parameters
Icompq : Integer [in]
> Specifies whether singular vectors are to be computed in
> factored form:
> = 0: Left singular vector matrix.
> = 1: Right singular vector matrix.

Nl : Integer [in]
> The row dimension of the upper block. NL >= 1.

Nr : Integer [in]
> The row dimension of the lower block. NR >= 1.

Sqre : Integer [in]
> = 0: the lower block is an NR-by-NR square matrix.
> = 1: the lower block is an NR-by-(NR+1) rectangular matrix.
> The bidiagonal matrix has row dimension N = NL + NR + 1,
> and column dimension M = N + SQRE.

Nrhs : Integer [in]
> The number of columns of B and BX. NRHS must be at least 1.

B : Complex Array, Dimension ( Ldb, Nrhs ) [in,out]
> On input, B contains the right hand sides of the least
> squares problem in rows 1 through M. On output, B contains
> the solution X in rows 1 through N.

Ldb : Integer [in]
> The leading dimension of B. LDB must be at least
> max(1,MAX( M, N ) ).

Bx : Complex Array, Dimension ( Ldbx, Nrhs ) [out]

Ldbx : Integer [in]
> The leading dimension of BX.

Perm : Integer Array, Dimension ( N ) [in]
> The permutations (from deflation and sorting) applied
> to the two blocks.

Givptr : Integer [in]
> The number of Givens rotations which took place in this
> subproblem.

Givcol : Integer Array, Dimension ( Ldgcol, 2 ) [in]
> Each pair of numbers indicates a pair of rows/columns
> involved in a Givens rotation.

Ldgcol : Integer [in]
> The leading dimension of GIVCOL, must be at least N.

Givnum : Real Array, Dimension ( Ldgnum, 2 ) [in]
> Each number indicates the C or S value used in the
> corresponding Givens rotation.

Ldgnum : Integer [in]
> The leading dimension of arrays DIFR, POLES and
> GIVNUM, must be at least K.

Poles : Real Array, Dimension ( Ldgnum, 2 ) [in]
> On entry, POLES(1:K, 1) contains the new singular
> values obtained from solving the secular equation, and
> POLES(1:K, 2) is an array containing the poles in the secular
> equation.

Difl : Real Array, Dimension ( K ). [in]
> On entry, DIFL(I) is the distance between I-th updated
> (undeflated) singular value and the I-th (undeflated) old
> singular value.

Difr : Real Array, Dimension ( Ldgnum, 2 ). [in]
> On entry, DIFR(I, 1) contains the distances between I-th
> updated (undeflated) singular value and the I+1-th
> (undeflated) old singular value. And DIFR(I, 2) is the
> normalizing factor for the I-th right singular vector.

Z : Real Array, Dimension ( K ) [in]
> Contain the components of the deflation-adjusted updating row
> vector.

K : Integer [in]
> Contains the dimension of the non-deflated matrix,
> This is the order of the related secular equation. 1 <= K <=N.

C : Real [in]
> C contains garbage if SQRE =0 and the C-value of a Givens
> rotation related to the right null space if SQRE = 1.

S : Real [in]
> S contains garbage if SQRE =0 and the S-value of a Givens
> rotation related to the right null space if SQRE = 1.

Rwork : Real Array, Dimension [out]
> ( K*(1+NRHS) + 2*NRHS )

Info : Integer [out]
> = 0:  successful exit.
> < 0:  if INFO = -i, the i-th argument had an illegal value.

