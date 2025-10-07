# DGEQR2P

## Function Signature

```fortran
DGEQR2P(M, N, A, LDA, TAU, WORK, INFO)
```

## Description


 DGEQR2P computes a QR factorization of a real m-by-n matrix A:

    A = Q * ( R ),
            ( 0 )

 where:

    Q is a m-by-m orthogonal matrix;
    R is an upper-triangular n-by-n matrix with nonnegative diagonal
    entries;
    0 is a (m-n)-by-n zero matrix, if m > n.


## Parameters

### M (in)

M is INTEGER The number of rows of the matrix A. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix A. N >= 0.

### A (in,out)

A is DOUBLE PRECISION array, dimension (LDA,N) On entry, the m by n matrix A. On exit, the elements on and above the diagonal of the array contain the min(m,n) by n upper trapezoidal matrix R (R is upper triangular if m >= n). The diagonal entries of R are nonnegative; the elements below the diagonal, with the array TAU, represent the orthogonal matrix Q as a product of elementary reflectors (see Further Details).

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,M).

### TAU (out)

TAU is DOUBLE PRECISION array, dimension (min(M,N)) The scalar factors of the elementary reflectors (see Further Details).

### WORK (out)

WORK is DOUBLE PRECISION array, dimension (N)

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

