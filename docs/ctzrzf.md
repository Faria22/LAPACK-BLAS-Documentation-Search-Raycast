# CTZRZF

## Function Signature

```fortran
CTZRZF(M, N, A, LDA, TAU, WORK, LWORK, INFO)
```

## Description


 CTZRZF reduces the M-by-N ( M<=N ) complex upper trapezoidal matrix A
 to upper triangular form by means of unitary transformations.

 The upper trapezoidal matrix A is factored as

    A = ( R  0 ) * Z,

 where Z is an N-by-N unitary matrix and R is an M-by-M upper
 triangular matrix.

## Parameters

### M (in)

M is INTEGER The number of rows of the matrix A. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix A. N >= M.

### A (in,out)

A is COMPLEX array, dimension (LDA,N) On entry, the leading M-by-N upper trapezoidal part of the array A must contain the matrix to be factorized. On exit, the leading M-by-M upper triangular part of A contains the upper triangular matrix R, and elements M+1 to N of the first M rows of A, with the array TAU, represent the unitary matrix Z as a product of M elementary reflectors.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,M).

### TAU (out)

TAU is COMPLEX array, dimension (M) The scalar factors of the elementary reflectors.

### WORK (out)

WORK is COMPLEX array, dimension (MAX(1,LWORK)) On exit, if INFO = 0, WORK(1) returns the optimal LWORK.

### LWORK (in)

LWORK is INTEGER The dimension of the array WORK. LWORK >= max(1,M). For optimum performance LWORK >= M*NB, where NB is the optimal blocksize. If LWORK = -1, then a workspace query is assumed; the routine only calculates the optimal size of the WORK array, returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

