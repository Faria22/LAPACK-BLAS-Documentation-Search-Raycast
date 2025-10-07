# SGTTS2

## Function Signature

```fortran
SGTTS2(ITRANS, N, NRHS, DL, D, DU, DU2, IPIV, B, LDB)
```

## Description


 SGTTS2 solves one of the systems of equations
    A*X = B  or  A**T*X = B,
 with a tridiagonal matrix A using the LU factorization computed
 by SGTTRF.

## Parameters

### ITRANS (in)

ITRANS is INTEGER Specifies the form of the system of equations. = 0: A * X = B (No transpose) = 1: A**T* X = B (Transpose) = 2: A**T* X = B (Conjugate transpose = Transpose)

### N (in)

N is INTEGER The order of the matrix A.

### NRHS (in)

NRHS is INTEGER The number of right hand sides, i.e., the number of columns of the matrix B. NRHS >= 0.

### DL (in)

DL is REAL array, dimension (N-1) The (n-1) multipliers that define the matrix L from the LU factorization of A.

### D (in)

D is REAL array, dimension (N) The n diagonal elements of the upper triangular matrix U from the LU factorization of A.

### DU (in)

DU is REAL array, dimension (N-1) The (n-1) elements of the first super-diagonal of U.

### DU2 (in)

DU2 is REAL array, dimension (N-2) The (n-2) elements of the second super-diagonal of U.

### IPIV (in)

IPIV is INTEGER array, dimension (N) The pivot indices; for 1 <= i <= n, row i of the matrix was interchanged with row IPIV(i). IPIV(i) will always be either i or i+1; IPIV(i) = i indicates a row interchange was not required.

### B (in,out)

B is REAL array, dimension (LDB,NRHS) On entry, the matrix of right hand side vectors B. On exit, B is overwritten by the solution vectors X.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,N).

