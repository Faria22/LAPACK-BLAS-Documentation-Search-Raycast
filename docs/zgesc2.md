# ZGESC2

## Function Signature

```fortran
ZGESC2(N, A, LDA, RHS, IPIV, JPIV, SCALE)
```

## Description


 ZGESC2 solves a system of linear equations

           A * X = scale* RHS

 with a general N-by-N matrix A using the LU factorization with
 complete pivoting computed by ZGETC2.


## Parameters

### N (in)

N is INTEGER The number of columns of the matrix A.

### A (in)

A is COMPLEX*16 array, dimension (LDA, N) On entry, the LU part of the factorization of the n-by-n matrix A computed by ZGETC2: A = P * L * U * Q

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1, N).

### RHS (in,out)

RHS is COMPLEX*16 array, dimension N. On entry, the right hand side vector b. On exit, the solution vector X.

### IPIV (in)

IPIV is INTEGER array, dimension (N). The pivot indices; for 1 <= i <= N, row i of the matrix has been interchanged with row IPIV(i).

### JPIV (in)

JPIV is INTEGER array, dimension (N). The pivot indices; for 1 <= j <= N, column j of the matrix has been interchanged with column JPIV(j).

### SCALE (out)

SCALE is DOUBLE PRECISION On exit, SCALE contains the scale factor. SCALE is chosen 0 <= SCALE <= 1 to prevent overflow in the solution.

