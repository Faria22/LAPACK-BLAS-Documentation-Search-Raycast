```fortran
subroutine cbdsqr (
		uplo,
		n,
		ncvt,
		nru,
		ncc,
		d,
		e,
		vt,
		ldvt,
		u,
		*                          ldu,
		c,
		ldc,
		rwork,
		info
)
```

 CBDSQR computes the singular values and, optionally, the right and/or
 left singular vectors from the singular value decomposition (SVD) of
 a real N-by-N (upper or lower) bidiagonal matrix B using the implicit
 zero-shift QR algorithm.  The SVD of B has the form

    B = Q * S * P**H

 where S is the diagonal matrix of singular values, Q is an orthogonal
 matrix of left singular vectors, and P is an orthogonal matrix of
 right singular vectors.  If left singular vectors are requested, this
 subroutine actually returns U*Q instead of Q, and, if right singular
 vectors are requested, this subroutine returns P**H*VT instead of
 P**H, for given complex input matrices U and VT.  When U and VT are
 the unitary matrices that reduce a general matrix A to bidiagonal
 form: A = U*B*VT, as computed by CGEBRD, then

    A = (U*Q) * S * (P**H*VT)

 is the SVD of A.  Optionally, the subroutine may also compute Q**H*C
 for a given complex input matrix C.

 See "Computing  Small Singular Values of Bidiagonal Matrices With
 Guaranteed High Relative Accuracy," by J. Demmel and W. Kahan,
 LAPACK Working Note #3 (or SIAM J. Sci. Statist. Comput. vol. 11,
 no. 5, pp. 873-912, Sept 1990) and
 "Accurate singular values and differential qd algorithms," by
 B. Parlett and V. Fernando, Technical Report CPAM-554, Mathematics
 Department, University of California at Berkeley, July 1992
 for a detailed description of the algorithm.

## Parameters
Uplo : Character*1 [in]
> = 'U':  B is upper bidiagonal;
> = 'L':  B is lower bidiagonal.

N : Integer [in]
> The order of the matrix B.  N >= 0.

Ncvt : Integer [in]
> The number of columns of the matrix VT. NCVT >= 0.

Nru : Integer [in]
> The number of rows of the matrix U. NRU >= 0.

Ncc : Integer [in]
> The number of columns of the matrix C. NCC >= 0.

D : Real Array, Dimension (n) [in,out]
> On entry, the n diagonal elements of the bidiagonal matrix B.
> On exit, if INFO=0, the singular values of B in decreasing
> order.

E : Real Array, Dimension (n-1) [in,out]
> On entry, the N-1 offdiagonal elements of the bidiagonal
> matrix B.
> On exit, if INFO = 0, E is destroyed; if INFO > 0, D and E
> will contain the diagonal and superdiagonal elements of a
> bidiagonal matrix orthogonally equivalent to the one given
> as input.

Vt : Complex Array, Dimension (ldvt, Ncvt) [in,out]
> On entry, an N-by-NCVT matrix VT.
> On exit, VT is overwritten by P**H * VT.
> Not referenced if NCVT = 0.

Ldvt : Integer [in]
> The leading dimension of the array VT.
> LDVT >= max(1,N) if NCVT > 0; LDVT >= 1 if NCVT = 0.

U : Complex Array, Dimension (ldu, N) [in,out]
> On entry, an NRU-by-N matrix U.
> On exit, U is overwritten by U * Q.
> Not referenced if NRU = 0.

Ldu : Integer [in]
> The leading dimension of the array U.  LDU >= max(1,NRU).

C : Complex Array, Dimension (ldc, Ncc) [in,out]
> On entry, an N-by-NCC matrix C.
> On exit, C is overwritten by Q**H * C.
> Not referenced if NCC = 0.

Ldc : Integer [in]
> The leading dimension of the array C.
> LDC >= max(1,N) if NCC > 0; LDC >=1 if NCC = 0.

Rwork : Real Array, Dimension (lrwork) [out]
> LRWORK = 4*N, if NCVT = NRU = NCC = 0, and
> LRWORK = 4*(N-1), otherwise

Info : Integer [out]
> = 0:  successful exit
> < 0:  If INFO = -i, the i-th argument had an illegal value
> > 0:  the algorithm did not converge; D and E contain the
> elements of a bidiagonal matrix which is orthogonally
> similar to the input matrix B;  if INFO = i, i
> elements of E have not converged to zero.

