```fortran
subroutine sgerqf (
		integer m,
		integer n,
		real, dimension(lda, *) a,
		integer lda,
		real, dimension(*) tau,
		real, dimension(*) work,
		integer lwork,
		integer info
)
```

 SGERQF computes an RQ factorization of a real M-by-N matrix A:
 A = R * Q.

## Parameters
M : Integer [in]
> The number of rows of the matrix A.  M >= 0.

N : Integer [in]
> The number of columns of the matrix A.  N >= 0.

A : Real Array, Dimension (lda,n) [in,out]
> On entry, the M-by-N matrix A.
> On exit,
> if m <= n, the upper triangle of the subarray
> A(1:m,n-m+1:n) contains the M-by-M upper triangular matrix R;
> if m >= n, the elements on and above the (m-n)-th subdiagonal
> contain the M-by-N upper trapezoidal matrix R;
> the remaining elements, with the array TAU, represent the
> orthogonal matrix Q as a product of min(m,n) elementary
> reflectors (see Further Details).

Lda : Integer [in]
> The leading dimension of the array A.  LDA >= max(1,M).

Tau : Real Array, Dimension (min(m,n)) [out]
> The scalar factors of the elementary reflectors (see Further
> Details).

Work : Real Array, Dimension (max(1,lwork)) [out]
> On exit, if INFO = 0, WORK(1) returns the optimal LWORK.

Lwork : Integer [in]
> The dimension of the array WORK.
> LWORK >= 1, if MIN(M,N) = 0, and LWORK >= M, otherwise.
> For optimum performance LWORK >= M*NB, where NB is
> the optimal blocksize.
> If LWORK = -1, then a workspace query is assumed; the routine
> only calculates the optimal size of the WORK array, returns
> this value as the first entry of the WORK array, and no error
> message related to LWORK is issued by XERBLA.

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value

