```fortran
subroutine dlaeda	(	n,
		tlvls,
		curlvl,
		curpbm,
		prmptr,
		perm,
		givptr,
		*                          givcol,
		givnum,
		q,
		qptr,
		z,
		ztemp,
		info )
```

 DLAEDA computes the Z vector corresponding to the merge step in the
 CURLVLth step of the merge process with TLVLS steps for the CURPBMth
 problem.

## Parameters
N : Integer [in]
> The dimension of the symmetric tridiagonal matrix.  N >= 0.

Tlvls : Integer [in]
> The total number of merging levels in the overall divide and
> conquer tree.

Curlvl : Integer [in]
> The current level in the overall merge routine,
> 0 <= curlvl <= tlvls.

Curpbm : Integer [in]
> The current problem in the current level in the overall
> merge routine (counting from upper left to lower right).

Prmptr : Integer Array, Dimension (n Lg N) [in]
> Contains a list of pointers which indicate where in PERM a
> level's permutation is stored.  PRMPTR(i+1) - PRMPTR(i)
> indicates the size of the permutation and incidentally the
> size of the full, non-deflated problem.

Perm : Integer Array, Dimension (n Lg N) [in]
> Contains the permutations (from deflation and sorting) to be
> applied to each eigenblock.

Givptr : Integer Array, Dimension (n Lg N) [in]
> Contains a list of pointers which indicate where in GIVCOL a
> level's Givens rotations are stored.  GIVPTR(i+1) - GIVPTR(i)
> indicates the number of Givens rotations.

Givcol : Integer Array, Dimension (2, N Lg N) [in]
> Each pair of numbers indicates a pair of columns to take place
> in a Givens rotation.

Givnum : Double Precision Array, Dimension (2, N Lg N) [in]
> Each number indicates the S value to be used in the
> corresponding Givens rotation.

Q : Double Precision Array, Dimension (n**2) [in]
> Contains the square eigenblocks from previous levels, the
> starting positions for blocks are given by QPTR.

Qptr : Integer Array, Dimension (n+2) [in]
> Contains a list of pointers which indicate where in Q an
> eigenblock is stored.  SQRT( QPTR(i+1) - QPTR(i) ) indicates
> the size of the block.

Z : Double Precision Array, Dimension (n) [out]
> On output this vector contains the updating vector (the last
> row of the first sub-eigenvector matrix and the first row of
> the second sub-eigenvector matrix).

Ztemp : Double Precision Array, Dimension (n) [out]

Info : Integer [out]
> = 0:  successful exit.
> < 0:  if INFO = -i, the i-th argument had an illegal value.

