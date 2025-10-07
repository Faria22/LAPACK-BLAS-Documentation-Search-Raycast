# SGEBD2

## Function Signature

```fortran
SGEBD2(M, N, A, LDA, D, E, TAUQ, TAUP, WORK, INFO)
```

## Description


 SGEBD2 reduces a real general m by n matrix A to upper or lower
 bidiagonal form B by an orthogonal transformation: Q**T * A * P = B.

 If m >= n, B is upper bidiagonal; if m < n, B is lower bidiagonal.

## Parameters

### M (in)

M is INTEGER The number of rows in the matrix A. M >= 0.

### N (in)

N is INTEGER The number of columns in the matrix A. N >= 0.

### A (in,out)

A is REAL array, dimension (LDA,N) On entry, the m by n general matrix to be reduced. On exit, if m >= n, the diagonal and the first superdiagonal are overwritten with the upper bidiagonal matrix B; the elements below the diagonal, with the array TAUQ, represent the orthogonal matrix Q as a product of elementary reflectors, and the elements above the first superdiagonal, with the array TAUP, represent the orthogonal matrix P as a product of elementary reflectors; if m < n, the diagonal and the first subdiagonal are overwritten with the lower bidiagonal matrix B; the elements below the first subdiagonal, with the array TAUQ, represent the orthogonal matrix Q as a product of elementary reflectors, and the elements above the diagonal, with the array TAUP, represent the orthogonal matrix P as a product of elementary reflectors. See Further Details.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,M).

### D (out)

D is REAL array, dimension (min(M,N)) The diagonal elements of the bidiagonal matrix B: D(i) = A(i,i).

### E (out)

E is REAL array, dimension (min(M,N)-1) The off-diagonal elements of the bidiagonal matrix B: if m >= n, E(i) = A(i,i+1) for i = 1,2,...,n-1; if m < n, E(i) = A(i+1,i) for i = 1,2,...,m-1.

### TAUQ (out)

TAUQ is REAL array, dimension (min(M,N)) The scalar factors of the elementary reflectors which represent the orthogonal matrix Q. See Further Details.

### TAUP (out)

TAUP is REAL array, dimension (min(M,N)) The scalar factors of the elementary reflectors which represent the orthogonal matrix P. See Further Details.

### WORK (out)

WORK is REAL array, dimension (max(M,N))

### INFO (out)

INFO is INTEGER = 0: successful exit. < 0: if INFO = -i, the i-th argument had an illegal value.

