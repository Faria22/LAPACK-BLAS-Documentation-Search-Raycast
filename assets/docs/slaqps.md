```fortran
subroutine slaqps (
		m,
		n,
		offset,
		nb,
		kb,
		a,
		lda,
		jpvt,
		tau,
		vn1,
		*                          vn2,
		auxv,
		f,
		ldf
)
```

 SLAQPS computes a step of QR factorization with column pivoting
 of a real M-by-N matrix A by using Blas-3.  It tries to factorize
 NB columns from A starting from the row OFFSET+1, and updates all
 of the matrix with Blas-3 xGEMM.

 In some cases, due to catastrophic cancellations, it cannot
 factorize NB columns.  Hence, the actual number of factorized
 columns is returned in KB.

 Block A(1:OFFSET,1:N) is accordingly pivoted, but not factorized.

## Parameters
M : Integer [in]
> The number of rows of the matrix A. M >= 0.

N : Integer [in]
> The number of columns of the matrix A. N >= 0

Offset : Integer [in]
> The number of rows of A that have been factorized in
> previous steps.

Nb : Integer [in]
> The number of columns to factorize.

Kb : Integer [out]
> The number of columns actually factorized.

A : Real Array, Dimension (lda,n) [in,out]
> On entry, the M-by-N matrix A.
> On exit, block A(OFFSET+1:M,1:KB) is the triangular
> factor obtained and block A(1:OFFSET,1:N) has been
> accordingly pivoted, but no factorized.
> The rest of the matrix, block A(OFFSET+1:M,KB+1:N) has
> been updated.

Lda : Integer [in]
> The leading dimension of the array A. LDA >= max(1,M).

Jpvt : Integer Array, Dimension (n) [in,out]
> JPVT(I) = K <==> Column K of the full matrix A has been
> permuted into position I in AP.

Tau : Real Array, Dimension (kb) [out]
> The scalar factors of the elementary reflectors.

Vn1 : Real Array, Dimension (n) [in,out]
> The vector with the partial column norms.

Vn2 : Real Array, Dimension (n) [in,out]
> The vector with the exact column norms.

Auxv : Real Array, Dimension (nb) [in,out]
> Auxiliary vector.

F : Real Array, Dimension (ldf,nb) [in,out]
> Matrix F**T = L*Y**T*A.

Ldf : Integer [in]
> The leading dimension of the array F. LDF >= max(1,N).

