```fortran
subroutine slasdq (
		uplo,
		sqre,
		n,
		ncvt,
		nru,
		ncc,
		d,
		e,
		vt,
		ldvt,
		*                          u,
		ldu,
		c,
		ldc,
		work,
		info
)
```

 SLASDQ computes the singular value decomposition (SVD) of a real
 (upper or lower) bidiagonal matrix with diagonal D and offdiagonal
 E, accumulating the transformations if desired. Letting B denote
 the input bidiagonal matrix, the algorithm computes orthogonal
 matrices Q and P such that B = Q * S * P**T (P**T denotes the transpose
 of P). The singular values S are overwritten on D.

 The input matrix U  is changed to U  * Q  if desired.
 The input matrix VT is changed to P**T * VT if desired.
 The input matrix C  is changed to Q**T * C  if desired.

 See "Computing  Small Singular Values of Bidiagonal Matrices With
 Guaranteed High Relative Accuracy," by J. Demmel and W. Kahan,
 LAPACK Working Note #3, for a detailed description of the algorithm.

## Parameters
Uplo : Character*1 [in]
> On entry, UPLO specifies whether the input bidiagonal matrix
> is upper or lower bidiagonal, and whether it is square are
> not.
> UPLO = 'U' or 'u'   B is upper bidiagonal.
> UPLO = 'L' or 'l'   B is lower bidiagonal.

Sqre : Integer [in]
> = 0: then the input matrix is N-by-N.
> = 1: then the input matrix is N-by-(N+1) if UPLU = 'U' and
> (N+1)-by-N if UPLU = 'L'.
> The bidiagonal matrix has
> N = NL + NR + 1 rows and
> M = N + SQRE >= N columns.

N : Integer [in]
> On entry, N specifies the number of rows and columns
> in the matrix. N must be at least 0.

Ncvt : Integer [in]
> On entry, NCVT specifies the number of columns of
> the matrix VT. NCVT must be at least 0.

Nru : Integer [in]
> On entry, NRU specifies the number of rows of
> the matrix U. NRU must be at least 0.

Ncc : Integer [in]
> On entry, NCC specifies the number of columns of
> the matrix C. NCC must be at least 0.

D : Real Array, Dimension (n) [in,out]
> On entry, D contains the diagonal entries of the
> bidiagonal matrix whose SVD is desired. On normal exit,
> D contains the singular values in ascending order.

E : Real Array. [in,out]
> dimension is (N-1) if SQRE = 0 and N if SQRE = 1.
> On entry, the entries of E contain the offdiagonal entries
> of the bidiagonal matrix whose SVD is desired. On normal
> exit, E will contain 0. If the algorithm does not converge,
> D and E will contain the diagonal and superdiagonal entries
> of a bidiagonal matrix orthogonally equivalent to the one
> given as input.

Vt : Real Array, Dimension (ldvt, Ncvt) [in,out]
> On entry, contains a matrix which on exit has been
> premultiplied by P**T, dimension N-by-NCVT if SQRE = 0
> and (N+1)-by-NCVT if SQRE = 1 (not referenced if NCVT=0).

Ldvt : Integer [in]
> On entry, LDVT specifies the leading dimension of VT as
> declared in the calling (sub) program. LDVT must be at
> least 1. If NCVT is nonzero LDVT must also be at least N.

U : Real Array, Dimension (ldu, N) [in,out]
> On entry, contains a  matrix which on exit has been
> postmultiplied by Q, dimension NRU-by-N if SQRE = 0
> and NRU-by-(N+1) if SQRE = 1 (not referenced if NRU=0).

Ldu : Integer [in]
> On entry, LDU  specifies the leading dimension of U as
> declared in the calling (sub) program. LDU must be at
> least max( 1, NRU ) .

C : Real Array, Dimension (ldc, Ncc) [in,out]
> On entry, contains an N-by-NCC matrix which on exit
> has been premultiplied by Q**T  dimension N-by-NCC if SQRE = 0
> and (N+1)-by-NCC if SQRE = 1 (not referenced if NCC=0).

Ldc : Integer [in]
> On entry, LDC  specifies the leading dimension of C as
> declared in the calling (sub) program. LDC must be at
> least 1. If NCC is nonzero, LDC must also be at least N.

Work : Real Array, Dimension (4*n) [out]
> Workspace. Only referenced if one of NCVT, NRU, or NCC is
> nonzero, and if N is at least 2.

Info : Integer [out]
> On exit, a value of 0 indicates a successful exit.
> If INFO < 0, argument number -INFO is illegal.
> If INFO > 0, the algorithm did not converge, and INFO
> specifies how many superdiagonals did not converge.

