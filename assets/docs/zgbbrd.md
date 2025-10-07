```fortran
subroutine zgbbrd (
		vect,
		m,
		n,
		ncc,
		kl,
		ku,
		ab,
		ldab,
		d,
		e,
		q,
		*                          ldq,
		pt,
		ldpt,
		c,
		ldc,
		work,
		rwork,
		info
)
```

 ZGBBRD reduces a complex general m-by-n band matrix A to real upper
 bidiagonal form B by a unitary transformation: Q**H * A * P = B.

 The routine computes B, and optionally forms Q or P**H, or computes
 Q**H*C for a given matrix C.

## Parameters
Vect : Character*1 [in]
> Specifies whether or not the matrices Q and P**H are to be
> formed.
> = 'N': do not form Q or P**H;
> = 'Q': form Q only;
> = 'P': form P**H only;
> = 'B': form both.

M : Integer [in]
> The number of rows of the matrix A.  M >= 0.

N : Integer [in]
> The number of columns of the matrix A.  N >= 0.

Ncc : Integer [in]
> The number of columns of the matrix C.  NCC >= 0.

Kl : Integer [in]
> The number of subdiagonals of the matrix A. KL >= 0.

Ku : Integer [in]
> The number of superdiagonals of the matrix A. KU >= 0.

Ab : Complex*16 Array, Dimension (ldab,n) [in,out]
> On entry, the m-by-n band matrix A, stored in rows 1 to
> KL+KU+1. The j-th column of A is stored in the j-th column of
> the array AB as follows:
> AB(ku+1+i-j,j) = A(i,j) for max(1,j-ku)<=i<=min(m,j+kl).
> On exit, A is overwritten by values generated during the
> reduction.

Ldab : Integer [in]
> The leading dimension of the array A. LDAB >= KL+KU+1.

D : Double Precision Array, Dimension (min(m,n)) [out]
> The diagonal elements of the bidiagonal matrix B.

E : Double Precision Array, Dimension (min(m,n)-1) [out]
> The superdiagonal elements of the bidiagonal matrix B.

Q : Complex*16 Array, Dimension (ldq,m) [out]
> If VECT = 'Q' or 'B', the m-by-m unitary matrix Q.
> If VECT = 'N' or 'P', the array Q is not referenced.

Ldq : Integer [in]
> The leading dimension of the array Q.
> LDQ >= max(1,M) if VECT = 'Q' or 'B'; LDQ >= 1 otherwise.

Pt : Complex*16 Array, Dimension (ldpt,n) [out]
> If VECT = 'P' or 'B', the n-by-n unitary matrix P'.
> If VECT = 'N' or 'Q', the array PT is not referenced.

Ldpt : Integer [in]
> The leading dimension of the array PT.
> LDPT >= max(1,N) if VECT = 'P' or 'B'; LDPT >= 1 otherwise.

C : Complex*16 Array, Dimension (ldc,ncc) [in,out]
> On entry, an m-by-ncc matrix C.
> On exit, C is overwritten by Q**H*C.
> C is not referenced if NCC = 0.

Ldc : Integer [in]
> The leading dimension of the array C.
> LDC >= max(1,M) if NCC > 0; LDC >= 1 if NCC = 0.

Work : Complex*16 Array, Dimension (max(m,n)) [out]

Rwork : Double Precision Array, Dimension (max(m,n)) [out]

Info : Integer [out]
> = 0:  successful exit.
> < 0:  if INFO = -i, the i-th argument had an illegal value.

