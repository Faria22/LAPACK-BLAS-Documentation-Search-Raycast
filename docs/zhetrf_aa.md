```fortran
subroutine zhetrf_aa (
		character uplo,
		integer n,
		complex*16, dimension(lda, *) a,
		integer lda,
		integer, dimension(*) ipiv,
		complex*16, dimension(*) work,
		integer lwork,
		integer info
)
```

 ZHETRF_AA computes the factorization of a complex hermitian matrix A
 using the Aasen's algorithm.  The form of the factorization is

    A = U**H*T*U  or  A = L*T*L**H

 where U (or L) is a product of permutation and unit upper (lower)
 triangular matrices, and T is a hermitian tridiagonal matrix.

 This is the blocked version of the algorithm, calling Level 3 BLAS.

## Parameters
Uplo : Character*1 [in]
> = 'U':  Upper triangle of A is stored;
> = 'L':  Lower triangle of A is stored.

N : Integer [in]
> The order of the matrix A.  N >= 0.

A : Complex*16 Array, Dimension (lda,n) [in,out]
> On entry, the hermitian matrix A.  If UPLO = 'U', the leading
> N-by-N upper triangular part of A contains the upper
> triangular part of the matrix A, and the strictly lower
> triangular part of A is not referenced.  If UPLO = 'L', the
> leading N-by-N lower triangular part of A contains the lower
> triangular part of the matrix A, and the strictly upper
> triangular part of A is not referenced.
> On exit, the tridiagonal matrix is stored in the diagonals
> and the subdiagonals of A just below (or above) the diagonals,
> and L is stored below (or above) the subdiagonals, when UPLO
> is 'L' (or 'U').

Lda : Integer [in]
> The leading dimension of the array A.  LDA >= max(1,N).

Ipiv : Integer Array, Dimension (n) [out]
> On exit, it contains the details of the interchanges, i.e.,
> the row and column k of A were interchanged with the
> row and column IPIV(k).

Work : Complex*16 Array, Dimension (max(1,lwork)) [out]
> On exit, if INFO = 0, WORK(1) returns the optimal LWORK.

Lwork : Integer [in]
> The length of WORK.
> LWORK >= 1, if N >= 1, and LWORK >= 2*N, otherwise.
> For optimum performance LWORK >= N*(1+NB), where NB is
> the optimal blocksize, returned by ILAENV.
> If LWORK = -1, then a workspace query is assumed; the routine
> only calculates the optimal size of the WORK array, returns
> this value as the first entry of the WORK array, and no error
> message related to LWORK is issued by XERBLA.

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value.

