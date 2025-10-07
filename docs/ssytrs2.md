```fortran
subroutine ssytrs2	(	uplo,
		n,
		nrhs,
		a,
		lda,
		ipiv,
		b,
		ldb,
		*                           work,
		info )
```

 SSYTRS2 solves a system of linear equations A*X = B with a real
 symmetric matrix A using the factorization A = U*D*U**T or
 A = L*D*L**T computed by SSYTRF and converted by SSYCONV.

## Parameters
Uplo : Character*1 [in]
> Specifies whether the details of the factorization are stored
> as an upper or lower triangular matrix.
> = 'U':  Upper triangular, form is A = U*D*U**T;
> = 'L':  Lower triangular, form is A = L*D*L**T.

N : Integer [in]
> The order of the matrix A.  N >= 0.

Nrhs : Integer [in]
> The number of right hand sides, i.e., the number of columns
> of the matrix B.  NRHS >= 0.

A : Real Array, Dimension (lda,n) [in,out]
> The block diagonal matrix D and the multipliers used to
> obtain the factor U or L as computed by SSYTRF.
> Note that A is input / output. This might be counter-intuitive,
> and one may think that A is input only. A is input / output. This
> is because, at the start of the subroutine, we permute A in a
> "better" form and then we permute A back to its original form at
> the end.

Lda : Integer [in]
> The leading dimension of the array A.  LDA >= max(1,N).

Ipiv : Integer Array, Dimension (n) [in]
> Details of the interchanges and the block structure of D
> as determined by SSYTRF.

B : Real Array, Dimension (ldb,nrhs) [in,out]
> On entry, the right hand side matrix B.
> On exit, the solution matrix X.

Ldb : Integer [in]
> The leading dimension of the array B.  LDB >= max(1,N).

Work : Real Array, Dimension (n) [out]

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value

