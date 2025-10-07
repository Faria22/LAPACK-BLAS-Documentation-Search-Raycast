```fortran
subroutine zhbgst	(	vect,
		uplo,
		n,
		ka,
		kb,
		ab,
		ldab,
		bb,
		ldbb,
		x,
		*                          ldx,
		work,
		rwork,
		info )
```

 ZHBGST reduces a complex Hermitian-definite banded generalized
 eigenproblem  A*x = lambda*B*x  to standard form  C*y = lambda*y,
 such that C has the same bandwidth as A.

 B must have been previously factorized as S**H*S by ZPBSTF, using a
 split Cholesky factorization. A is overwritten by C = X**H*A*X, where
 X = S**(-1)*Q and Q is a unitary matrix chosen to preserve the
 bandwidth of A.

## Parameters
Vect : Character*1 [in]
> = 'N':  do not form the transformation matrix X;
> = 'V':  form X.

Uplo : Character*1 [in]
> = 'U':  Upper triangle of A is stored;
> = 'L':  Lower triangle of A is stored.

N : Integer [in]
> The order of the matrices A and B.  N >= 0.

Ka : Integer [in]
> The number of superdiagonals of the matrix A if UPLO = 'U',
> or the number of subdiagonals if UPLO = 'L'.  KA >= 0.

Kb : Integer [in]
> The number of superdiagonals of the matrix B if UPLO = 'U',
> or the number of subdiagonals if UPLO = 'L'.  KA >= KB >= 0.

Ab : Complex*16 Array, Dimension (ldab,n) [in,out]
> On entry, the upper or lower triangle of the Hermitian band
> matrix A, stored in the first ka+1 rows of the array.  The
> j-th column of A is stored in the j-th column of the array AB
> as follows:
> if UPLO = 'U', AB(ka+1+i-j,j) = A(i,j) for max(1,j-ka)<=i<=j;
> if UPLO = 'L', AB(1+i-j,j)    = A(i,j) for j<=i<=min(n,j+ka).
> On exit, the transformed matrix X**H*A*X, stored in the same
> format as A.

Ldab : Integer [in]
> The leading dimension of the array AB.  LDAB >= KA+1.

Bb : Complex*16 Array, Dimension (ldbb,n) [in]
> The banded factor S from the split Cholesky factorization of
> B, as returned by ZPBSTF, stored in the first kb+1 rows of
> the array.

Ldbb : Integer [in]
> The leading dimension of the array BB.  LDBB >= KB+1.

X : Complex*16 Array, Dimension (ldx,n) [out]
> If VECT = 'V', the n-by-n matrix X.
> If VECT = 'N', the array X is not referenced.

Ldx : Integer [in]
> The leading dimension of the array X.
> LDX >= max(1,N) if VECT = 'V'; LDX >= 1 otherwise.

Work : Complex*16 Array, Dimension (n) [out]

Rwork : Double Precision Array, Dimension (n) [out]

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value.

