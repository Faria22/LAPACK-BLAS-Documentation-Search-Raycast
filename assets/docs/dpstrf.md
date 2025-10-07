```fortran
subroutine dpstrf (
		character uplo,
		integer n,
		double precision, dimension(lda, *) a,
		integer lda,
		integer, dimension(n) piv,
		integer rank,
		double precision tol,
		double precision, dimension(2*n) work,
		integer info
)
```

 DPSTRF computes the Cholesky factorization with complete
 pivoting of a real symmetric positive semidefinite matrix A.

 The factorization has the form
    P**T * A * P = U**T * U ,  if UPLO = 'U',
    P**T * A * P = L  * L**T,  if UPLO = 'L',
 where U is an upper triangular matrix and L is lower triangular, and
 P is stored as vector PIV.

 This algorithm does not attempt to check that A is positive
 semidefinite. This version of the algorithm calls level 3 BLAS.

## Parameters
Uplo : Character*1 [in]
> Specifies whether the upper or lower triangular part of the
> symmetric matrix A is stored.
> = 'U':  Upper triangular
> = 'L':  Lower triangular

N : Integer [in]
> The order of the matrix A.  N >= 0.

A : Double Precision Array, Dimension (lda,n) [in,out]
> On entry, the symmetric matrix A.  If UPLO = 'U', the leading
> n by n upper triangular part of A contains the upper
> triangular part of the matrix A, and the strictly lower
> triangular part of A is not referenced.  If UPLO = 'L', the
> leading n by n lower triangular part of A contains the lower
> triangular part of the matrix A, and the strictly upper
> triangular part of A is not referenced.
> On exit, if INFO = 0, the factor U or L from the Cholesky
> factorization as above.

Lda : Integer [in]
> The leading dimension of the array A.  LDA >= max(1,N).

Piv : Integer Array, Dimension (n) [out]
> PIV is such that the nonzero entries are P( PIV(K), K ) = 1.

Rank : Integer [out]
> The rank of A given by the number of steps the algorithm
> completed.

Tol : Double Precision [in]
> User defined tolerance. If TOL < 0, then N*U*MAX( A(K,K) )
> will be used. The algorithm terminates at the (K-1)st step
> if the pivot <= TOL.

Work : Double Precision Array, Dimension (2*n) [out]
> Work space.

Info : Integer [out]
> < 0: If INFO = -K, the K-th argument had an illegal value,
> = 0: algorithm completed successfully, and
> > 0: the matrix A is either rank deficient with computed rank
> as returned in RANK, or is not positive semidefinite. See
> Section 7 of LAPACK Working Note #161 for further
> information.

