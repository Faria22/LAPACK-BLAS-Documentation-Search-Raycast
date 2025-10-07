```fortran
subroutine dtpqrt2 (
		integer m,
		integer n,
		integer l,
		double precision, dimension(lda, *) a,
		integer lda,
		double precision, dimension(ldb, *) b,
		integer ldb,
		double precision, dimension(ldt, *) t,
		integer ldt,
		integer info
)
```

 DTPQRT2 computes a QR factorization of a real "triangular-pentagonal"
 matrix C, which is composed of a triangular block A and pentagonal block B,
 using the compact WY representation for Q.

## Parameters
M : Integer [in]
> The total number of rows of the matrix B.
> M >= 0.

N : Integer [in]
> The number of columns of the matrix B, and the order of
> the triangular matrix A.
> N >= 0.

L : Integer [in]
> The number of rows of the upper trapezoidal part of B.
> MIN(M,N) >= L >= 0.  See Further Details.

A : Double Precision Array, Dimension (lda,n) [in,out]
> On entry, the upper triangular N-by-N matrix A.
> On exit, the elements on and above the diagonal of the array
> contain the upper triangular matrix R.

Lda : Integer [in]
> The leading dimension of the array A.  LDA >= max(1,N).

B : Double Precision Array, Dimension (ldb,n) [in,out]
> On entry, the pentagonal M-by-N matrix B.  The first M-L rows
> are rectangular, and the last L rows are upper trapezoidal.
> On exit, B contains the pentagonal matrix V.  See Further Details.

Ldb : Integer [in]
> The leading dimension of the array B.  LDB >= max(1,M).

T : Double Precision Array, Dimension (ldt,n) [out]
> The N-by-N upper triangular factor T of the block reflector.
> See Further Details.

Ldt : Integer [in]
> The leading dimension of the array T.  LDT >= max(1,N)

Info : Integer [out]
> = 0: successful exit
> < 0: if INFO = -i, the i-th argument had an illegal value

