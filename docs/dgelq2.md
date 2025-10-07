# DGELQ2

## Function Signature

```fortran
DGELQ2(M, N, A, LDA, TAU, WORK, INFO)
```

## Description


 DGELQ2 computes an LQ factorization of a real m-by-n matrix A:

    A = ( L 0 ) *  Q

 where:

    Q is a n-by-n orthogonal matrix;
    L is a lower-triangular m-by-m matrix;
    0 is a m-by-(n-m) zero matrix, if m < n.


## Parameters

### M (in)

M is INTEGER The number of rows of the matrix A. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix A. N >= 0.

### A (in,out)

A is DOUBLE PRECISION array, dimension (LDA,N) On entry, the m by n matrix A. On exit, the elements on and below the diagonal of the array contain the m by min(m,n) lower trapezoidal matrix L (L is lower triangular if m <= n); the elements above the diagonal, with the array TAU, represent the orthogonal matrix Q as a product of elementary reflectors (see Further Details).

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,M).

### TAU (out)

TAU is DOUBLE PRECISION array, dimension (min(M,N)) The scalar factors of the elementary reflectors (see Further Details).

### WORK (out)

WORK is DOUBLE PRECISION array, dimension (M)

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

