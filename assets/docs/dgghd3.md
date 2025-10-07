```fortran
subroutine dgghd3 (
		compq,
		compz,
		n,
		ilo,
		ihi,
		a,
		lda,
		b,
		ldb,
		q,
		*                          ldq,
		z,
		ldz,
		work,
		lwork,
		info
)
```

 DGGHD3 reduces a pair of real matrices (A,B) to generalized upper
 Hessenberg form using orthogonal transformations, where A is a
 general matrix and B is upper triangular.  The form of the
 generalized eigenvalue problem is
    A*x = lambda*B*x,
 and B is typically made upper triangular by computing its QR
 factorization and moving the orthogonal matrix Q to the left side
 of the equation.

 This subroutine simultaneously reduces A to a Hessenberg matrix H:
    Q**T*A*Z = H
 and transforms B to another upper triangular matrix T:
    Q**T*B*Z = T
 in order to reduce the problem to its standard form
    H*y = lambda*T*y
 where y = Z**T*x.

 The orthogonal matrices Q and Z are determined as products of Givens
 rotations.  They may either be formed explicitly, or they may be
 postmultiplied into input matrices Q1 and Z1, so that

      Q1 * A * Z1**T = (Q1*Q) * H * (Z1*Z)**T

      Q1 * B * Z1**T = (Q1*Q) * T * (Z1*Z)**T

 If Q1 is the orthogonal matrix from the QR factorization of B in the
 original equation A*x = lambda*B*x, then DGGHD3 reduces the original
 problem to generalized Hessenberg form.

 This is a blocked variant of DGGHRD, using matrix-matrix
 multiplications for parts of the computation to enhance performance.

## Parameters
Compq : Character*1 [in]
> = 'N': do not compute Q;
> = 'I': Q is initialized to the unit matrix, and the
> orthogonal matrix Q is returned;
> = 'V': Q must contain an orthogonal matrix Q1 on entry,
> and the product Q1*Q is returned.

Compz : Character*1 [in]
> = 'N': do not compute Z;
> = 'I': Z is initialized to the unit matrix, and the
> orthogonal matrix Z is returned;
> = 'V': Z must contain an orthogonal matrix Z1 on entry,
> and the product Z1*Z is returned.

N : Integer [in]
> The order of the matrices A and B.  N >= 0.

Ilo : Integer [in]

Ihi : Integer [in]
> ILO and IHI mark the rows and columns of A which are to be
> reduced.  It is assumed that A is already upper triangular
> in rows and columns 1:ILO-1 and IHI+1:N.  ILO and IHI are
> normally set by a previous call to DGGBAL; otherwise they
> should be set to 1 and N respectively.
> 1 <= ILO <= IHI <= N, if N > 0; ILO=1 and IHI=0, if N=0.

A : Double Precision Array, Dimension (lda, N) [in,out]
> On entry, the N-by-N general matrix to be reduced.
> On exit, the upper triangle and the first subdiagonal of A
> are overwritten with the upper Hessenberg matrix H, and the
> rest is set to zero.

Lda : Integer [in]
> The leading dimension of the array A.  LDA >= max(1,N).

B : Double Precision Array, Dimension (ldb, N) [in,out]
> On entry, the N-by-N upper triangular matrix B.
> On exit, the upper triangular matrix T = Q**T B Z.  The
> elements below the diagonal are set to zero.

Ldb : Integer [in]
> The leading dimension of the array B.  LDB >= max(1,N).

Q : Double Precision Array, Dimension (ldq, N) [in,out]
> On entry, if COMPQ = 'V', the orthogonal matrix Q1,
> typically from the QR factorization of B.
> On exit, if COMPQ='I', the orthogonal matrix Q, and if
> COMPQ = 'V', the product Q1*Q.
> Not referenced if COMPQ='N'.

Ldq : Integer [in]
> The leading dimension of the array Q.
> LDQ >= N if COMPQ='V' or 'I'; LDQ >= 1 otherwise.

Z : Double Precision Array, Dimension (ldz, N) [in,out]
> On entry, if COMPZ = 'V', the orthogonal matrix Z1.
> On exit, if COMPZ='I', the orthogonal matrix Z, and if
> COMPZ = 'V', the product Z1*Z.
> Not referenced if COMPZ='N'.

Ldz : Integer [in]
> The leading dimension of the array Z.
> LDZ >= N if COMPZ='V' or 'I'; LDZ >= 1 otherwise.

Work : Double Precision Array, Dimension (max(1,lwork)) [out]
> On exit, if INFO = 0, WORK(1) returns the optimal LWORK.

Lwork : Integer [in]
> The length of the array WORK. LWORK >= 1.
> For optimum performance LWORK >= 6*N*NB, where NB is the
> optimal blocksize.
> If LWORK = -1, then a workspace query is assumed; the routine
> only calculates the optimal size of the WORK array, returns
> this value as the first entry of the WORK array, and no error
> message related to LWORK is issued by XERBLA.

Info : Integer [out]
> = 0:  successful exit.
> < 0:  if INFO = -i, the i-th argument had an illegal value.

