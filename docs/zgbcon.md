```fortran
subroutine zgbcon	(	norm,
		n,
		kl,
		ku,
		ab,
		ldab,
		ipiv,
		anorm,
		rcond,
		*                          work,
		rwork,
		info )
```

 ZGBCON estimates the reciprocal of the condition number of a complex
 general band matrix A, in either the 1-norm or the infinity-norm,
 using the LU factorization computed by ZGBTRF.

 An estimate is obtained for norm(inv(A)), and the reciprocal of the
 condition number is computed as
    RCOND = 1 / ( norm(A) * norm(inv(A)) ).

## Parameters
Norm : Character*1 [in]
> Specifies whether the 1-norm condition number or the
> infinity-norm condition number is required:
> = '1' or 'O':  1-norm;
> = 'I':         Infinity-norm.

N : Integer [in]
> The order of the matrix A.  N >= 0.

Kl : Integer [in]
> The number of subdiagonals within the band of A.  KL >= 0.

Ku : Integer [in]
> The number of superdiagonals within the band of A.  KU >= 0.

Ab : Complex*16 Array, Dimension (ldab,n) [in]
> Details of the LU factorization of the band matrix A, as
> computed by ZGBTRF.  U is stored as an upper triangular band
> matrix with KL+KU superdiagonals in rows 1 to KL+KU+1, and
> the multipliers used during the factorization are stored in
> rows KL+KU+2 to 2*KL+KU+1.

Ldab : Integer [in]
> The leading dimension of the array AB.  LDAB >= 2*KL+KU+1.

Ipiv : Integer Array, Dimension (n) [in]
> The pivot indices; for 1 <= i <= N, row i of the matrix was
> interchanged with row IPIV(i).

Anorm : Double Precision [in]
> If NORM = '1' or 'O', the 1-norm of the original matrix A.
> If NORM = 'I', the infinity-norm of the original matrix A.

Rcond : Double Precision [out]
> The reciprocal of the condition number of the matrix A,
> computed as RCOND = 1/(norm(A) * norm(inv(A))).

Work : Complex*16 Array, Dimension (2*n) [out]

Rwork : Double Precision Array, Dimension (n) [out]

Info : Integer [out]
> = 0:  successful exit
> < 0: if INFO = -i, the i-th argument had an illegal value

