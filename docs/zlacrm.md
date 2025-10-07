```fortran
subroutine zlacrm (
		integer m,
		integer n,
		complex*16, dimension(lda, *) a,
		integer lda,
		double precision, dimension(ldb, *) b,
		integer ldb,
		complex*16, dimension(ldc, *) c,
		integer ldc,
		double precision, dimension(*) rwork
)
```

 ZLACRM performs a very simple matrix-matrix multiplication:
          C := A * B,
 where A is M by N and complex; B is N by N and real;
 C is M by N and complex.

## Parameters
M : Integer [in]
> The number of rows of the matrix A and of the matrix C.
> M >= 0.

N : Integer [in]
> The number of columns and rows of the matrix B and
> the number of columns of the matrix C.
> N >= 0.

A : Complex*16 Array, Dimension (lda, N) [in]
> On entry, A contains the M by N matrix A.

Lda : Integer [in]
> The leading dimension of the array A. LDA >=max(1,M).

B : Double Precision Array, Dimension (ldb, N) [in]
> On entry, B contains the N by N matrix B.

Ldb : Integer [in]
> The leading dimension of the array B. LDB >=max(1,N).

C : Complex*16 Array, Dimension (ldc, N) [out]
> On exit, C contains the M by N matrix C.

Ldc : Integer [in]
> The leading dimension of the array C. LDC >=max(1,N).

Rwork : Double Precision Array, Dimension (2*m*n) [out]

