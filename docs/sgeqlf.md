# SGEQLF

## Function Signature

```fortran
SGEQLF(M, N, A, LDA, TAU, WORK, LWORK, INFO)
```

## Description


 SGEQLF computes a QL factorization of a real M-by-N matrix A:
 A = Q * L.

## Parameters

### M (in)

M is INTEGER The number of rows of the matrix A. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix A. N >= 0.

### A (in,out)

A is REAL array, dimension (LDA,N) On entry, the M-by-N matrix A. On exit, if m >= n, the lower triangle of the subarray A(m-n+1:m,1:n) contains the N-by-N lower triangular matrix L; if m <= n, the elements on and below the (n-m)-th superdiagonal contain the M-by-N lower trapezoidal matrix L; the remaining elements, with the array TAU, represent the orthogonal matrix Q as a product of elementary reflectors (see Further Details).

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,M).

### TAU (out)

TAU is REAL array, dimension (min(M,N)) The scalar factors of the elementary reflectors (see Further Details).

### WORK (out)

WORK is REAL array, dimension (MAX(1,LWORK)) On exit, if INFO = 0, WORK(1) returns the optimal LWORK.

### LWORK (in)

LWORK is INTEGER The dimension of the array WORK. LWORK >= 1, if MIN(M,N) = 0, and LWORK >= N, otherwise. For optimum performance LWORK >= N*NB, where NB is the optimal blocksize. If LWORK = -1, then a workspace query is assumed; the routine only calculates the optimal size of the WORK array, returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

