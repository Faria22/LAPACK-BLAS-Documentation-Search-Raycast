# ZGETRS

## Function Signature

```fortran
ZGETRS(TRANS, N, NRHS, A, LDA, IPIV, B, LDB, INFO)
```

## Description


 ZGETRS solves a system of linear equations
    A * X = B,  A**T * X = B,  or  A**H * X = B
 with a general N-by-N matrix A using the LU factorization computed
 by ZGETRF.

## Parameters

### TRANS (in)

TRANS is CHARACTER*1 Specifies the form of the system of equations: = 'N': A * X = B (No transpose) = 'T': A**T * X = B (Transpose) = 'C': A**H * X = B (Conjugate transpose)

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### NRHS (in)

NRHS is INTEGER The number of right hand sides, i.e., the number of columns of the matrix B. NRHS >= 0.

### A (in)

A is COMPLEX*16 array, dimension (LDA,N) The factors L and U from the factorization A = P*L*U as computed by ZGETRF.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### IPIV (in)

IPIV is INTEGER array, dimension (N) The pivot indices from ZGETRF; for 1<=i<=N, row i of the matrix was interchanged with row IPIV(i).

### B (in,out)

B is COMPLEX*16 array, dimension (LDB,NRHS) On entry, the right hand side matrix B. On exit, the solution matrix X.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,N).

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

