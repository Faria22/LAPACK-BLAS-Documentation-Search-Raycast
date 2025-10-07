```fortran
subroutine zgeqr2p (
		integer m,
		integer n,
		complex*16, dimension(lda, *) a,
		integer lda,
		complex*16, dimension(*) tau,
		complex*16, dimension(*) work,
		integer info
)
```

 ZGEQR2P computes a QR factorization of a complex m-by-n matrix A:

    A = Q * ( R ),
            ( 0 )

 where:

    Q is a m-by-m orthogonal matrix;
    R is an upper-triangular n-by-n matrix with nonnegative diagonal
    entries;
    0 is a (m-n)-by-n zero matrix, if m > n.


## Parameters
M : Integer [in]
> The number of rows of the matrix A.  M >= 0.

N : Integer [in]
> The number of columns of the matrix A.  N >= 0.

A : Complex*16 Array, Dimension (lda,n) [in,out]
> On entry, the m by n matrix A.
> On exit, the elements on and above the diagonal of the array
> contain the min(m,n) by n upper trapezoidal matrix R (R is
> upper triangular if m >= n). The diagonal entries of R
> are real and nonnegative; the elements below the diagonal,
> with the array TAU, represent the unitary matrix Q as a
> product of elementary reflectors (see Further Details).

Lda : Integer [in]
> The leading dimension of the array A.  LDA >= max(1,M).

Tau : Complex*16 Array, Dimension (min(m,n)) [out]
> The scalar factors of the elementary reflectors (see Further
> Details).

Work : Complex*16 Array, Dimension (n) [out]

Info : Integer [out]
> = 0: successful exit
> < 0: if INFO = -i, the i-th argument had an illegal value

