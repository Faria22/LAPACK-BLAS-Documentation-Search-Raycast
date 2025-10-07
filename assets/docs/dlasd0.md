```fortran
subroutine dlasd0 (
		n,
		sqre,
		d,
		e,
		u,
		ldu,
		vt,
		ldvt,
		smlsiz,
		iwork,
		*                          work,
		info
)
```

 Using a divide and conquer approach, DLASD0 computes the singular
 value decomposition (SVD) of a real upper bidiagonal N-by-M
 matrix B with diagonal D and offdiagonal E, where M = N + SQRE.
 The algorithm computes orthogonal matrices U and VT such that
 B = U * S * VT. The singular values S are overwritten on D.

 A related subroutine, DLASDA, computes only the singular values,
 and optionally, the singular vectors in compact form.

## Parameters
N : Integer [in]
> On entry, the row dimension of the upper bidiagonal matrix.
> This is also the dimension of the main diagonal array D.

Sqre : Integer [in]
> Specifies the column dimension of the bidiagonal matrix.
> = 0: The bidiagonal matrix has column dimension M = N;
> = 1: The bidiagonal matrix has column dimension M = N+1;

D : Double Precision Array, Dimension (n) [in,out]
> On entry D contains the main diagonal of the bidiagonal
> matrix.
> On exit D, if INFO = 0, contains its singular values.

E : Double Precision Array, Dimension (m-1) [in,out]
> Contains the subdiagonal entries of the bidiagonal matrix.
> On exit, E has been destroyed.

U : Double Precision Array, Dimension (ldu, N) [in,out]
> On exit, U contains the left singular vectors,
> if U passed in as (N, N) Identity.

Ldu : Integer [in]
> On entry, leading dimension of U.

Vt : Double Precision Array, Dimension (ldvt, M) [in,out]
> On exit, VT**T contains the right singular vectors,
> if VT passed in as (M, M) Identity.

Ldvt : Integer [in]
> On entry, leading dimension of VT.

Smlsiz : Integer [in]
> On entry, maximum size of the subproblems at the
> bottom of the computation tree.

Iwork : Integer Array, Dimension (8*n) [out]

Work : Double Precision Array, Dimension (3*m**2+2*m) [out]

Info : Integer [out]
> = 0:  successful exit.
> < 0:  if INFO = -i, the i-th argument had an illegal value.
> > 0:  if INFO = 1, a singular value did not converge

