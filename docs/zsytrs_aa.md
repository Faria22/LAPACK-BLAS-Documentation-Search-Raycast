```fortran
subroutine zsytrs_aa (
		uplo,
		n,
		nrhs,
		a,
		lda,
		ipiv,
		b,
		ldb,
		*                             work,
		lwork,
		info
)
```

 ZSYTRS_AA solves a system of linear equations A*X = B with a complex
 symmetric matrix A using the factorization A = U**T*T*U or
 A = L*T*L**T computed by ZSYTRF_AA.

## Parameters
Uplo : Character*1 [in]
> Specifies whether the details of the factorization are stored
> as an upper or lower triangular matrix.
> = 'U':  Upper triangular, form is A = U**T*T*U;
> = 'L':  Lower triangular, form is A = L*T*L**T.

N : Integer [in]
> The order of the matrix A.  N >= 0.

Nrhs : Integer [in]
> The number of right hand sides, i.e., the number of columns
> of the matrix B.  NRHS >= 0.

A : Complex*16 Array, Dimension (lda,n) [in]
> Details of factors computed by ZSYTRF_AA.

Lda : Integer [in]
> The leading dimension of the array A.  LDA >= max(1,N).

Ipiv : Integer Array, Dimension (n) [in]
> Details of the interchanges as computed by ZSYTRF_AA.

B : Complex*16 Array, Dimension (ldb,nrhs) [in,out]
> On entry, the right hand side matrix B.
> On exit, the solution matrix X.

Ldb : Integer [in]
> The leading dimension of the array B.  LDB >= max(1,N).

Work : Complex*16 Array, Dimension (max(1,lwork)) [out]

Lwork : Integer [in]
> The dimension of the array WORK. LWORK >= max(1,3*N-2).

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value

