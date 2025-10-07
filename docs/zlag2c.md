```fortran
subroutine zlag2c (
		integer m,
		integer n,
		complex*16, dimension(lda, *) a,
		integer lda,
		complex, dimension(ldsa, *) sa,
		integer ldsa,
		integer info
)
```

 ZLAG2C converts a COMPLEX*16 matrix, SA, to a COMPLEX matrix, A.

 RMAX is the overflow for the SINGLE PRECISION arithmetic
 ZLAG2C checks that all the entries of A are between -RMAX and
 RMAX. If not the conversion is aborted and a flag is raised.

 This is an auxiliary routine so there is no argument checking.

## Parameters
M : Integer [in]
> The number of lines of the matrix A.  M >= 0.

N : Integer [in]
> The number of columns of the matrix A.  N >= 0.

A : Complex*16 Array, Dimension (lda,n) [in]
> On entry, the M-by-N coefficient matrix A.

Lda : Integer [in]
> The leading dimension of the array A.  LDA >= max(1,M).

Sa : Complex Array, Dimension (ldsa,n) [out]
> On exit, if INFO=0, the M-by-N coefficient matrix SA; if
> INFO>0, the content of SA is unspecified.

Ldsa : Integer [in]
> The leading dimension of the array SA.  LDSA >= max(1,M).

Info : Integer [out]
> = 0:  successful exit.
> = 1:  an entry of the matrix A is greater than the SINGLE
> PRECISION overflow threshold, in this case, the content
> of SA in exit is unspecified.

