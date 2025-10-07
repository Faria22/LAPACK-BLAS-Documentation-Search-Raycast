# CGEQRFP

## Function Signature

```fortran
CGEQRFP(M, N, A, LDA, TAU, WORK, LWORK, INFO)
```

## Description


 CGEQR2P computes a QR factorization of a complex M-by-N matrix A:

    A = Q * ( R ),
            ( 0 )

 where:

    Q is a M-by-M orthogonal matrix;
    R is an upper-triangular N-by-N matrix with nonnegative diagonal
    entries;
    0 is a (M-N)-by-N zero matrix, if M > N.


## Parameters

### M (in)

M is INTEGER The number of rows of the matrix A. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix A. N >= 0.

### A (in,out)

A is COMPLEX array, dimension (LDA,N) On entry, the M-by-N matrix A. On exit, the elements on and above the diagonal of the array contain the min(M,N)-by-N upper trapezoidal matrix R (R is upper triangular if m >= n). The diagonal entries of R are real and nonnegative; the elements below the diagonal, with the array TAU, represent the unitary matrix Q as a product of min(m,n) elementary reflectors (see Further Details).

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,M).

### TAU (out)

TAU is COMPLEX array, dimension (min(M,N)) The scalar factors of the elementary reflectors (see Further Details).

### WORK (out)

WORK is COMPLEX array, dimension (MAX(1,LWORK)) On exit, if INFO = 0, WORK(1) returns the optimal LWORK.

### LWORK (in)

LWORK is INTEGER The dimension of the array WORK. LWORK >= 1, if MIN(M,N) = 0, and LWORK >= N, otherwise. For optimum performance LWORK >= N*NB, where NB is the optimal blocksize. If LWORK = -1, then a workspace query is assumed; the routine only calculates the optimal size of the WORK array, returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

