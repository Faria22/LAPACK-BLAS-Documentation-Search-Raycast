```fortran
subroutine dlasd7 (
		icompq,
		nl,
		nr,
		sqre,
		k,
		d,
		z,
		zw,
		vf,
		vfw,
		vl,
		*                          vlw,
		alpha,
		beta,
		dsigma,
		idx,
		idxp,
		idxq,
		*                          perm,
		givptr,
		givcol,
		ldgcol,
		givnum,
		ldgnum,
		*                          c,
		s,
		info
)
```

 DLASD7 merges the two sets of singular values together into a single
 sorted set. Then it tries to deflate the size of the problem. There
 are two ways in which deflation can occur:  when two or more singular
 values are close together or if there is a tiny entry in the Z
 vector. For each such occurrence the order of the related
 secular equation problem is reduced by one.

 DLASD7 is called from DLASD6.

## Parameters
Icompq : Integer [in]
> Specifies whether singular vectors are to be computed
> in compact form, as follows:
> = 0: Compute singular values only.
> = 1: Compute singular vectors of upper
> bidiagonal matrix in compact form.

Nl : Integer [in]
> The row dimension of the upper block. NL >= 1.

Nr : Integer [in]
> The row dimension of the lower block. NR >= 1.

Sqre : Integer [in]
> = 0: the lower block is an NR-by-NR square matrix.
> = 1: the lower block is an NR-by-(NR+1) rectangular matrix.
> The bidiagonal matrix has
> N = NL + NR + 1 rows and
> M = N + SQRE >= N columns.

K : Integer [out]
> Contains the dimension of the non-deflated matrix, this is
> the order of the related secular equation. 1 <= K <=N.

D : Double Precision Array, Dimension ( N ) [in,out]
> On entry D contains the singular values of the two submatrices
> to be combined. On exit D contains the trailing (N-K) updated
> singular values (those which were deflated) sorted into
> increasing order.

Z : Double Precision Array, Dimension ( M ) [out]
> On exit Z contains the updating row vector in the secular
> equation.

Zw : Double Precision Array, Dimension ( M ) [out]
> Workspace for Z.

Vf : Double Precision Array, Dimension ( M ) [in,out]
> On entry, VF(1:NL+1) contains the first components of all
> right singular vectors of the upper block; and VF(NL+2:M)
> contains the first components of all right singular vectors
> of the lower block. On exit, VF contains the first components
> of all right singular vectors of the bidiagonal matrix.

Vfw : Double Precision Array, Dimension ( M ) [out]
> Workspace for VF.

Vl : Double Precision Array, Dimension ( M ) [in,out]
> On entry, VL(1:NL+1) contains the  last components of all
> right singular vectors of the upper block; and VL(NL+2:M)
> contains the last components of all right singular vectors
> of the lower block. On exit, VL contains the last components
> of all right singular vectors of the bidiagonal matrix.

Vlw : Double Precision Array, Dimension ( M ) [out]
> Workspace for VL.

Alpha : Double Precision [in]
> Contains the diagonal element associated with the added row.

Beta : Double Precision [in]
> Contains the off-diagonal element associated with the added
> row.

Dsigma : Double Precision Array, Dimension ( N ) [out]
> Contains a copy of the diagonal elements (K-1 singular values
> and one zero) in the secular equation.

Idx : Integer Array, Dimension ( N ) [out]
> This will contain the permutation used to sort the contents of
> D into ascending order.

Idxp : Integer Array, Dimension ( N ) [out]
> This will contain the permutation used to place deflated
> values of D at the end of the array. On output IDXP(2:K)
> points to the nondeflated D-values and IDXP(K+1:N)
> points to the deflated singular values.

Idxq : Integer Array, Dimension ( N ) [in]
> This contains the permutation which separately sorts the two
> sub-problems in D into ascending order.  Note that entries in
> the first half of this permutation must first be moved one
> position backward; and entries in the second half
> must first have NL+1 added to their values.

Perm : Integer Array, Dimension ( N ) [out]
> The permutations (from deflation and sorting) to be applied
> to each singular block. Not referenced if ICOMPQ = 0.

Givptr : Integer [out]
> The number of Givens rotations which took place in this
> subproblem. Not referenced if ICOMPQ = 0.

Givcol : Integer Array, Dimension ( Ldgcol, 2 ) [out]
> Each pair of numbers indicates a pair of columns to take place
> in a Givens rotation. Not referenced if ICOMPQ = 0.

Ldgcol : Integer [in]
> The leading dimension of GIVCOL, must be at least N.

Givnum : Double Precision Array, Dimension ( Ldgnum, 2 ) [out]
> Each number indicates the C or S value to be used in the
> corresponding Givens rotation. Not referenced if ICOMPQ = 0.

Ldgnum : Integer [in]
> The leading dimension of GIVNUM, must be at least N.

C : Double Precision [out]
> C contains garbage if SQRE =0 and the C-value of a Givens
> rotation related to the right null space if SQRE = 1.

S : Double Precision [out]
> S contains garbage if SQRE =0 and the S-value of a Givens
> rotation related to the right null space if SQRE = 1.

Info : Integer [out]
> = 0:  successful exit.
> < 0:  if INFO = -i, the i-th argument had an illegal value.

