```fortran
subroutine chsein (
		side,
		eigsrc,
		initv,
		select,
		n,
		h,
		ldh,
		w,
		vl,
		*                          ldvl,
		vr,
		ldvr,
		mm,
		m,
		work,
		rwork,
		ifaill,
		*                          ifailr,
		info
)
```

 CHSEIN uses inverse iteration to find specified right and/or left
 eigenvectors of a complex upper Hessenberg matrix H.

 The right eigenvector x and the left eigenvector y of the matrix H
 corresponding to an eigenvalue w are defined by:

              H * x = w * x,     y**h * H = w * y**h

 where y**h denotes the conjugate transpose of the vector y.

## Parameters
Side : Character*1 [in]
> = 'R': compute right eigenvectors only;
> = 'L': compute left eigenvectors only;
> = 'B': compute both right and left eigenvectors.

Eigsrc : Character*1 [in]
> Specifies the source of eigenvalues supplied in W:
> = 'Q': the eigenvalues were found using CHSEQR; thus, if
> H has zero subdiagonal elements, and so is
> block-triangular, then the j-th eigenvalue can be
> assumed to be an eigenvalue of the block containing
> the j-th row/column.  This property allows CHSEIN to
> perform inverse iteration on just one diagonal block.
> = 'N': no assumptions are made on the correspondence
> between eigenvalues and diagonal blocks.  In this
> case, CHSEIN must always perform inverse iteration
> using the whole matrix H.

Initv : Character*1 [in]
> = 'N': no initial vectors are supplied;
> = 'U': user-supplied initial vectors are stored in the arrays
> VL and/or VR.

Select : Logical Array, Dimension (n) [in]
> Specifies the eigenvectors to be computed. To select the
> eigenvector corresponding to the eigenvalue W(j),
> SELECT(j) must be set to .TRUE..

N : Integer [in]
> The order of the matrix H.  N >= 0.

H : Complex Array, Dimension (ldh,n) [in]
> The upper Hessenberg matrix H.
> If a NaN is detected in H, the routine will return with INFO=-6.

Ldh : Integer [in]
> The leading dimension of the array H.  LDH >= max(1,N).

W : Complex Array, Dimension (n) [in,out]
> On entry, the eigenvalues of H.
> On exit, the real parts of W may have been altered since
> close eigenvalues are perturbed slightly in searching for
> independent eigenvectors.

Vl : Complex Array, Dimension (ldvl,mm) [in,out]
> On entry, if INITV = 'U' and SIDE = 'L' or 'B', VL must
> contain starting vectors for the inverse iteration for the
> left eigenvectors; the starting vector for each eigenvector
> must be in the same column in which the eigenvector will be
> stored.
> On exit, if SIDE = 'L' or 'B', the left eigenvectors
> specified by SELECT will be stored consecutively in the
> columns of VL, in the same order as their eigenvalues.
> If SIDE = 'R', VL is not referenced.

Ldvl : Integer [in]
> The leading dimension of the array VL.
> LDVL >= max(1,N) if SIDE = 'L' or 'B'; LDVL >= 1 otherwise.

Vr : Complex Array, Dimension (ldvr,mm) [in,out]
> On entry, if INITV = 'U' and SIDE = 'R' or 'B', VR must
> contain starting vectors for the inverse iteration for the
> right eigenvectors; the starting vector for each eigenvector
> must be in the same column in which the eigenvector will be
> stored.
> On exit, if SIDE = 'R' or 'B', the right eigenvectors
> specified by SELECT will be stored consecutively in the
> columns of VR, in the same order as their eigenvalues.
> If SIDE = 'L', VR is not referenced.

Ldvr : Integer [in]
> The leading dimension of the array VR.
> LDVR >= max(1,N) if SIDE = 'R' or 'B'; LDVR >= 1 otherwise.

Mm : Integer [in]
> The number of columns in the arrays VL and/or VR. MM >= M.

M : Integer [out]
> The number of columns in the arrays VL and/or VR required to
> store the eigenvectors (= the number of .TRUE. elements in
> SELECT).

Work : Complex Array, Dimension (n*n) [out]

Rwork : Real Array, Dimension (n) [out]

Ifaill : Integer Array, Dimension (mm) [out]
> If SIDE = 'L' or 'B', IFAILL(i) = j > 0 if the left
> eigenvector in the i-th column of VL (corresponding to the
> eigenvalue w(j)) failed to converge; IFAILL(i) = 0 if the
> eigenvector converged satisfactorily.
> If SIDE = 'R', IFAILL is not referenced.

Ifailr : Integer Array, Dimension (mm) [out]
> If SIDE = 'R' or 'B', IFAILR(i) = j > 0 if the right
> eigenvector in the i-th column of VR (corresponding to the
> eigenvalue w(j)) failed to converge; IFAILR(i) = 0 if the
> eigenvector converged satisfactorily.
> If SIDE = 'L', IFAILR is not referenced.

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value
> > 0:  if INFO = i, i is the number of eigenvectors which
> failed to converge; see IFAILL and IFAILR for further
> details.

