```fortran
subroutine cgetri (
		integer n,
		complex, dimension(lda, *) a,
		integer lda,
		integer, dimension(*) ipiv,
		complex, dimension(*) work,
		integer lwork,
		integer info
)
```

 CGETRI computes the inverse of a matrix using the LU factorization
 computed by CGETRF.

 This method inverts U and then computes inv(A) by solving the system
 inv(A)*L = inv(U) for inv(A).

## Parameters
N : Integer [in]
> The order of the matrix A.  N >= 0.

A : Complex Array, Dimension (lda,n) [in,out]
> On entry, the factors L and U from the factorization
> A = P*L*U as computed by CGETRF.
> On exit, if INFO = 0, the inverse of the original matrix A.

Lda : Integer [in]
> The leading dimension of the array A.  LDA >= max(1,N).

Ipiv : Integer Array, Dimension (n) [in]
> The pivot indices from CGETRF; for 1<=i<=N, row i of the
> matrix was interchanged with row IPIV(i).

Work : Complex Array, Dimension (max(1,lwork)) [out]
> On exit, if INFO=0, then WORK(1) returns the optimal LWORK.

Lwork : Integer [in]
> The dimension of the array WORK.  LWORK >= max(1,N).
> For optimal performance LWORK >= N*NB, where NB is
> the optimal blocksize returned by ILAENV.
> If LWORK = -1, then a workspace query is assumed; the routine
> only calculates the optimal size of the WORK array, returns
> this value as the first entry of the WORK array, and no error
> message related to LWORK is issued by XERBLA.

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value
> > 0:  if INFO = i, U(i,i) is exactly zero; the matrix is
> singular and its inverse could not be computed.

