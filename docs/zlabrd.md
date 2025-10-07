# ZLABRD

## Function Signature

```fortran
ZLABRD(M, N, NB, A, LDA, D, E, TAUQ, TAUP, X, LDX, Y,
*                          LDY)
```

## Description


 ZLABRD reduces the first NB rows and columns of a complex general
 m by n matrix A to upper or lower real bidiagonal form by a unitary
 transformation Q**H * A * P, and returns the matrices X and Y which
 are needed to apply the transformation to the unreduced part of A.

 If m >= n, A is reduced to upper bidiagonal form; if m < n, to lower
 bidiagonal form.

 This is an auxiliary routine called by ZGEBRD

## Parameters

### M (in)

M is INTEGER The number of rows in the matrix A.

### N (in)

N is INTEGER The number of columns in the matrix A.

### NB (in)

NB is INTEGER The number of leading rows and columns of A to be reduced.

### A (in,out)

A is COMPLEX*16 array, dimension (LDA,N) On entry, the m by n general matrix to be reduced. On exit, the first NB rows and columns of the matrix are overwritten; the rest of the array is unchanged. If m >= n, elements on and below the diagonal in the first NB columns, with the array TAUQ, represent the unitary matrix Q as a product of elementary reflectors; and elements above the diagonal in the first NB rows, with the array TAUP, represent the unitary matrix P as a product of elementary reflectors. If m < n, elements below the diagonal in the first NB columns, with the array TAUQ, represent the unitary matrix Q as a product of elementary reflectors, and elements on and above the diagonal in the first NB rows, with the array TAUP, represent the unitary matrix P as a product of elementary reflectors. See Further Details.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,M).

### D (out)

D is DOUBLE PRECISION array, dimension (NB) The diagonal elements of the first NB rows and columns of the reduced matrix. D(i) = A(i,i).

### E (out)

E is DOUBLE PRECISION array, dimension (NB) The off-diagonal elements of the first NB rows and columns of the reduced matrix.

### TAUQ (out)

TAUQ is COMPLEX*16 array, dimension (NB) The scalar factors of the elementary reflectors which represent the unitary matrix Q. See Further Details.

### TAUP (out)

TAUP is COMPLEX*16 array, dimension (NB) The scalar factors of the elementary reflectors which represent the unitary matrix P. See Further Details.

### X (out)

X is COMPLEX*16 array, dimension (LDX,NB) The m-by-nb matrix X required to update the unreduced part of A.

### LDX (in)

LDX is INTEGER The leading dimension of the array X. LDX >= max(1,M).

### Y (out)

Y is COMPLEX*16 array, dimension (LDY,NB) The n-by-nb matrix Y required to update the unreduced part of A.

### LDY (in)

LDY is INTEGER The leading dimension of the array Y. LDY >= max(1,N).

