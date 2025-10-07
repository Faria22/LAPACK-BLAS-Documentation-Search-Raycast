```fortran
subroutine zheswapr (
		character uplo,
		integer n,
		complex*16, dimension(lda, n) a,
		integer lda,
		integer i1,
		integer i2
)
```

 ZHESWAPR applies an elementary permutation on the rows and the columns of
 a hermitian matrix.

## Parameters
Uplo : Character*1 [in]
> Specifies whether the details of the factorization are stored
> as an upper or lower triangular matrix.
> = 'U':  Upper triangular, form is A = U*D*U**T;
> = 'L':  Lower triangular, form is A = L*D*L**T.

N : Integer [in]
> The order of the matrix A.  N >= 0.

A : Complex*16 Array, Dimension (lda,n) [in,out]
> On entry, the NB diagonal matrix D and the multipliers
> used to obtain the factor U or L as computed by CSYTRF.
> On exit, if INFO = 0, the (symmetric) inverse of the original
> matrix.  If UPLO = 'U', the upper triangular part of the
> inverse is formed and the part of A below the diagonal is not
> referenced; if UPLO = 'L' the lower triangular part of the
> inverse is formed and the part of A above the diagonal is
> not referenced.

Lda : Integer [in]
> The leading dimension of the array A.  LDA >= max(1,N).

I1 : Integer [in]
> Index of the first row to swap

I2 : Integer [in]
> Index of the second row to swap

