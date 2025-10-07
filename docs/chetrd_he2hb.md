```fortran
subroutine chetrd_he2hb (
		uplo,
		n,
		kd,
		a,
		lda,
		ab,
		ldab,
		tau,
		*                              work,
		lwork,
		info
)
```

 CHETRD_HE2HB reduces a complex Hermitian matrix A to complex Hermitian
 band-diagonal form AB by a unitary similarity transformation:
 Q**H * A * Q = AB.

## Parameters
Uplo : Character*1 [in]
> = 'U':  Upper triangle of A is stored;
> = 'L':  Lower triangle of A is stored.

N : Integer [in]
> The order of the matrix A.  N >= 0.

Kd : Integer [in]
> The number of superdiagonals of the reduced matrix if UPLO = 'U',
> or the number of subdiagonals if UPLO = 'L'.  KD >= 0.
> The reduced matrix is stored in the array AB.

A : Complex Array, Dimension (lda,n) [in,out]
> On entry, the Hermitian matrix A.  If UPLO = 'U', the leading
> N-by-N upper triangular part of A contains the upper
> triangular part of the matrix A, and the strictly lower
> triangular part of A is not referenced.  If UPLO = 'L', the
> leading N-by-N lower triangular part of A contains the lower
> triangular part of the matrix A, and the strictly upper
> triangular part of A is not referenced.
> On exit, if UPLO = 'U', the diagonal and first superdiagonal
> of A are overwritten by the corresponding elements of the
> tridiagonal matrix T, and the elements above the first
> superdiagonal, with the array TAU, represent the unitary
> matrix Q as a product of elementary reflectors; if UPLO
> = 'L', the diagonal and first subdiagonal of A are over-
> written by the corresponding elements of the tridiagonal
> matrix T, and the elements below the first subdiagonal, with
> the array TAU, represent the unitary matrix Q as a product
> of elementary reflectors. See Further Details.

Lda : Integer [in]
> The leading dimension of the array A.  LDA >= max(1,N).

Ab : Complex Array, Dimension (ldab,n) [out]
> On exit, the upper or lower triangle of the Hermitian band
> matrix A, stored in the first KD+1 rows of the array.  The
> j-th column of A is stored in the j-th column of the array AB
> as follows:
> if UPLO = 'U', AB(kd+1+i-j,j) = A(i,j) for max(1,j-kd)<=i<=j;
> if UPLO = 'L', AB(1+i-j,j)    = A(i,j) for j<=i<=min(n,j+kd).

Ldab : Integer [in]
> The leading dimension of the array AB.  LDAB >= KD+1.

Tau : Complex Array, Dimension (n-kd) [out]
> The scalar factors of the elementary reflectors (see Further
> Details).

Work : Complex Array, Dimension (max(1,lwork)) [out]
> On exit, if INFO = 0, or if LWORK = -1,
> WORK(1) returns the size of LWORK.

Lwork : Integer [in]
> The dimension of the array WORK which should be calculated
> by a workspace query.
> If N <= KD+1, LWORK >= 1, else LWORK = MAX(1, LWORK_QUERY).
> If LWORK = -1, then a workspace query is assumed; the routine
> only calculates the optimal size of the WORK array, returns
> this value as the first entry of the WORK array, and no error
> message related to LWORK is issued by XERBLA.
> LWORK_QUERY = N*KD + N*max(KD,FACTOPTNB) + 2*KD*KD
> where FACTOPTNB is the blocking used by the QR or LQ
> algorithm, usually FACTOPTNB=128 is a good choice otherwise
> putting LWORK=-1 will provide the size of WORK.

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value

