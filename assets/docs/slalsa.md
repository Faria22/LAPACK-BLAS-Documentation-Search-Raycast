```fortran
subroutine slalsa (
		icompq,
		smlsiz,
		n,
		nrhs,
		b,
		ldb,
		bx,
		ldbx,
		u,
		*                          ldu,
		vt,
		k,
		difl,
		difr,
		z,
		poles,
		givptr,
		*                          givcol,
		ldgcol,
		perm,
		givnum,
		c,
		s,
		work,
		*                          iwork,
		info
)
```

 SLALSA is an intermediate step in solving the least squares problem
 by computing the SVD of the coefficient matrix in compact form (The
 singular vectors are computed as products of simple orthogonal
 matrices.).

 If ICOMPQ = 0, SLALSA applies the inverse of the left singular vector
 matrix of an upper bidiagonal matrix to the right hand side; and if
 ICOMPQ = 1, SLALSA applies the right singular vector matrix to the
 right hand side. The singular vector matrices were generated in
 compact form by SLALSA.

## Parameters
Icompq : Integer [in]
> Specifies whether the left or the right singular vector
> matrix is involved.
> = 0: Left singular vector matrix
> = 1: Right singular vector matrix

Smlsiz : Integer [in]
> The maximum size of the subproblems at the bottom of the
> computation tree.

N : Integer [in]
> The row and column dimensions of the upper bidiagonal matrix.

Nrhs : Integer [in]
> The number of columns of B and BX. NRHS must be at least 1.

B : Real Array, Dimension ( Ldb, Nrhs ) [in,out]
> On input, B contains the right hand sides of the least
> squares problem in rows 1 through M.
> On output, B contains the solution X in rows 1 through N.

Ldb : Integer [in]
> The leading dimension of B in the calling subprogram.
> LDB must be at least max(1,MAX( M, N ) ).

Bx : Real Array, Dimension ( Ldbx, Nrhs ) [out]
> On exit, the result of applying the left or right singular
> vector matrix to B.

Ldbx : Integer [in]
> The leading dimension of BX.

U : Real Array, Dimension ( Ldu, Smlsiz ). [in]
> On entry, U contains the left singular vector matrices of all
> subproblems at the bottom level.

Ldu : Integer, Ldu = > N. [in]
> The leading dimension of arrays U, VT, DIFL, DIFR,
> POLES, GIVNUM, and Z.

Vt : Real Array, Dimension ( Ldu, Smlsiz+1 ). [in]
> On entry, VT**T contains the right singular vector matrices of
> all subproblems at the bottom level.

K : Integer Array, Dimension ( N ). [in]

Difl : Real Array, Dimension ( Ldu, Nlvl ). [in]
> where NLVL = INT(log_2 (N/(SMLSIZ+1))) + 1.

Difr : Real Array, Dimension ( Ldu, 2 * Nlvl ). [in]
> On entry, DIFL(*, I) and DIFR(*, 2 * I -1) record
> distances between singular values on the I-th level and
> singular values on the (I -1)-th level, and DIFR(*, 2 * I)
> record the normalizing factors of the right singular vectors
> matrices of subproblems on I-th level.

Z : Real Array, Dimension ( Ldu, Nlvl ). [in]
> On entry, Z(1, I) contains the components of the deflation-
> adjusted updating row vector for subproblems on the I-th
> level.

Poles : Real Array, Dimension ( Ldu, 2 * Nlvl ). [in]
> On entry, POLES(*, 2 * I -1: 2 * I) contains the new and old
> singular values involved in the secular equations on the I-th
> level.

Givptr : Integer Array, Dimension ( N ). [in]
> On entry, GIVPTR( I ) records the number of Givens
> rotations performed on the I-th problem on the computation
> tree.

Givcol : Integer Array, Dimension ( Ldgcol, 2 * Nlvl ). [in]
> On entry, for each I, GIVCOL(*, 2 * I - 1: 2 * I) records the
> locations of Givens rotations performed on the I-th level on
> the computation tree.

Ldgcol : Integer, Ldgcol = > N. [in]
> The leading dimension of arrays GIVCOL and PERM.

Perm : Integer Array, Dimension ( Ldgcol, Nlvl ). [in]
> On entry, PERM(*, I) records permutations done on the I-th
> level of the computation tree.

Givnum : Real Array, Dimension ( Ldu, 2 * Nlvl ). [in]
> On entry, GIVNUM(*, 2 *I -1 : 2 * I) records the C- and S-
> values of Givens rotations performed on the I-th level on the
> computation tree.

C : Real Array, Dimension ( N ). [in]
> On entry, if the I-th subproblem is not square,
> C( I ) contains the C-value of a Givens rotation related to
> the right null space of the I-th subproblem.

S : Real Array, Dimension ( N ). [in]
> On entry, if the I-th subproblem is not square,
> S( I ) contains the S-value of a Givens rotation related to
> the right null space of the I-th subproblem.

Work : Real Array, Dimension (n) [out]

Iwork : Integer Array, Dimension (3*n) [out]

Info : Integer [out]
> = 0:  successful exit.
> < 0:  if INFO = -i, the i-th argument had an illegal value.

