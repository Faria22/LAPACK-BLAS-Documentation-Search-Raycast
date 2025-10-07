# CLAGTM

## Function Signature

```fortran
CLAGTM(TRANS, N, NRHS, ALPHA, DL, D, DU, X, LDX, BETA,
*                          B, LDB)
```

## Description


 CLAGTM performs a matrix-matrix product of the form

    B := alpha * A * X + beta * B

 where A is a tridiagonal matrix of order N, B and X are N by NRHS
 matrices, and alpha and beta are real scalars, each of which may be
 0., 1., or -1.

## Parameters

### TRANS (in)

TRANS is CHARACTER*1 Specifies the operation applied to A. = 'N': No transpose, B := alpha * A * X + beta * B = 'T': Transpose, B := alpha * A**T * X + beta * B = 'C': Conjugate transpose, B := alpha * A**H * X + beta * B

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### NRHS (in)

NRHS is INTEGER The number of right hand sides, i.e., the number of columns of the matrices X and B.

### ALPHA (in)

ALPHA is REAL The scalar alpha. ALPHA must be 0., 1., or -1.; otherwise, it is assumed to be 0.

### DL (in)

DL is COMPLEX array, dimension (N-1) The (n-1) sub-diagonal elements of T.

### D (in)

D is COMPLEX array, dimension (N) The diagonal elements of T.

### DU (in)

DU is COMPLEX array, dimension (N-1) The (n-1) super-diagonal elements of T.

### X (in)

X is COMPLEX array, dimension (LDX,NRHS) The N by NRHS matrix X.

### LDX (in)

LDX is INTEGER The leading dimension of the array X. LDX >= max(N,1).

### BETA (in)

BETA is REAL The scalar beta. BETA must be 0., 1., or -1.; otherwise, it is assumed to be 1.

### B (in,out)

B is COMPLEX array, dimension (LDB,NRHS) On entry, the N by NRHS matrix B. On exit, B is overwritten by the matrix expression B := alpha * A * X + beta * B.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(N,1).

