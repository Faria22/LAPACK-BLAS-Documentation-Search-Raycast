```fortran
subroutine dlasd2 (
		nl,
		nr,
		sqre,
		k,
		d,
		z,
		alpha,
		beta,
		u,
		ldu,
		vt,
		*                          ldvt,
		dsigma,
		u2,
		ldu2,
		vt2,
		ldvt2,
		idxp,
		idx,
		*                          idxc,
		idxq,
		coltyp,
		info
)
```

 DLASD2 merges the two sets of singular values together into a single
 sorted set.  Then it tries to deflate the size of the problem.
 There are two ways in which deflation can occur:  when two or more
 singular values are close together or if there is a tiny entry in the
 Z vector.  For each such occurrence the order of the related secular
 equation problem is reduced by one.

 DLASD2 is called from DLASD1.

## Parameters
Nl : Integer [in]
> The row dimension of the upper block.  NL >= 1.

Nr : Integer [in]
> The row dimension of the lower block.  NR >= 1.

Sqre : Integer [in]
> = 0: the lower block is an NR-by-NR square matrix.
> = 1: the lower block is an NR-by-(NR+1) rectangular matrix.
> The bidiagonal matrix has N = NL + NR + 1 rows and
> M = N + SQRE >= N columns.

K : Integer [out]
> Contains the dimension of the non-deflated matrix,
> This is the order of the related secular equation. 1 <= K <=N.

D : Double Precision Array, Dimension(n) [in,out]
> On entry D contains the singular values of the two submatrices
> to be combined.  On exit D contains the trailing (N-K) updated
> singular values (those which were deflated) sorted into
> increasing order.

Z : Double Precision Array, Dimension(n) [out]
> On exit Z contains the updating row vector in the secular
> equation.

Alpha : Double Precision [in]
> Contains the diagonal element associated with the added row.

Beta : Double Precision [in]
> Contains the off-diagonal element associated with the added
> row.

U : Double Precision Array, Dimension(ldu,n) [in,out]
> On entry U contains the left singular vectors of two
> submatrices in the two square blocks with corners at (1,1),
> (NL, NL), and (NL+2, NL+2), (N,N).
> On exit U contains the trailing (N-K) updated left singular
> vectors (those which were deflated) in its last N-K columns.

Ldu : Integer [in]
> The leading dimension of the array U.  LDU >= N.

Vt : Double Precision Array, Dimension(ldvt,m) [in,out]
> On entry VT**T contains the right singular vectors of two
> submatrices in the two square blocks with corners at (1,1),
> (NL+1, NL+1), and (NL+2, NL+2), (M,M).
> On exit VT**T contains the trailing (N-K) updated right singular
> vectors (those which were deflated) in its last N-K columns.
> In case SQRE =1, the last row of VT spans the right null
> space.

Ldvt : Integer [in]
> The leading dimension of the array VT.  LDVT >= M.

Dsigma : Double Precision Array, Dimension (n) [out]
> Contains a copy of the diagonal elements (K-1 singular values
> and one zero) in the secular equation.

U2 : Double Precision Array, Dimension(ldu2,n) [out]
> Contains a copy of the first K-1 left singular vectors which
> will be used by DLASD3 in a matrix multiply (DGEMM) to solve
> for the new left singular vectors. U2 is arranged into four
> blocks. The first block contains a column with 1 at NL+1 and
> zero everywhere else; the second block contains non-zero
> entries only at and above NL; the third contains non-zero
> entries only below NL+1; and the fourth is dense.

Ldu2 : Integer [in]
> The leading dimension of the array U2.  LDU2 >= N.

Vt2 : Double Precision Array, Dimension(ldvt2,n) [out]
> VT2**T contains a copy of the first K right singular vectors
> which will be used by DLASD3 in a matrix multiply (DGEMM) to
> solve for the new right singular vectors. VT2 is arranged into
> three blocks. The first block contains a row that corresponds
> to the special 0 diagonal element in SIGMA; the second block
> contains non-zeros only at and before NL +1; the third block
> contains non-zeros only at and after  NL +2.

Ldvt2 : Integer [in]
> The leading dimension of the array VT2.  LDVT2 >= M.

Idxp : Integer Array, Dimension(n) [out]
> This will contain the permutation used to place deflated
> values of D at the end of the array. On output IDXP(2:K)
> points to the nondeflated D-values and IDXP(K+1:N)
> points to the deflated singular values.

Idx : Integer Array, Dimension(n) [out]
> This will contain the permutation used to sort the contents of
> D into ascending order.

Idxc : Integer Array, Dimension(n) [out]
> This will contain the permutation used to arrange the columns
> of the deflated U matrix into three groups:  the first group
> contains non-zero entries only at and above NL, the second
> contains non-zero entries only below NL+2, and the third is
> dense.

Idxq : Integer Array, Dimension(n) [in,out]
> This contains the permutation which separately sorts the two
> sub-problems in D into ascending order.  Note that entries in
> the first hlaf of this permutation must first be moved one
> position backward; and entries in the second half
> must first have NL+1 added to their values.

Coltyp : Integer Array, Dimension(n) [out]
> As workspace, this will contain a label which will indicate
> which of the following types a column in the U2 matrix or a
> row in the VT2 matrix is:
> 1 : non-zero in the upper half only
> 2 : non-zero in the lower half only
> 3 : dense
> 4 : deflated
> On exit, it is an array of dimension 4, with COLTYP(I) being
> the dimension of the I-th type columns.

Info : Integer [out]
> = 0:  successful exit.
> < 0:  if INFO = -i, the i-th argument had an illegal value.

