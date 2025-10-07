# SGTRFS

## Function Signature

```fortran
SGTRFS(TRANS, N, NRHS, DL, D, DU, DLF, DF, DUF, DU2,
*                          IPIV, B, LDB, X, LDX, FERR, BERR, WORK, IWORK,
*                          INFO)
```

## Description


 SGTRFS improves the computed solution to a system of linear
 equations when the coefficient matrix is tridiagonal, and provides
 error bounds and backward error estimates for the solution.

## Parameters

### TRANS (in)

TRANS is CHARACTER*1 Specifies the form of the system of equations: = 'N': A * X = B (No transpose) = 'T': A**T * X = B (Transpose) = 'C': A**H * X = B (Conjugate transpose = Transpose)

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### NRHS (in)

NRHS is INTEGER The number of right hand sides, i.e., the number of columns of the matrix B. NRHS >= 0.

### DL (in)

DL is REAL array, dimension (N-1) The (n-1) subdiagonal elements of A.

### D (in)

D is REAL array, dimension (N) The diagonal elements of A.

### DU (in)

DU is REAL array, dimension (N-1) The (n-1) superdiagonal elements of A.

### DLF (in)

DLF is REAL array, dimension (N-1) The (n-1) multipliers that define the matrix L from the LU factorization of A as computed by SGTTRF.

### DF (in)

DF is REAL array, dimension (N) The n diagonal elements of the upper triangular matrix U from the LU factorization of A.

### DUF (in)

DUF is REAL array, dimension (N-1) The (n-1) elements of the first superdiagonal of U.

### DU2 (in)

DU2 is REAL array, dimension (N-2) The (n-2) elements of the second superdiagonal of U.

### IPIV (in)

IPIV is INTEGER array, dimension (N) The pivot indices; for 1 <= i <= n, row i of the matrix was interchanged with row IPIV(i). IPIV(i) will always be either i or i+1; IPIV(i) = i indicates a row interchange was not required.

### B (in)

B is REAL array, dimension (LDB,NRHS) The right hand side matrix B.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,N).

### X (in,out)

X is REAL array, dimension (LDX,NRHS) On entry, the solution matrix X, as computed by SGTTRS. On exit, the improved solution matrix X.

### LDX (in)

LDX is INTEGER The leading dimension of the array X. LDX >= max(1,N).

### FERR (out)

FERR is REAL array, dimension (NRHS) The estimated forward error bound for each solution vector X(j) (the j-th column of the solution matrix X). If XTRUE is the true solution corresponding to X(j), FERR(j) is an estimated upper bound for the magnitude of the largest element in (X(j) - XTRUE) divided by the magnitude of the largest element in X(j). The estimate is as reliable as the estimate for RCOND, and is almost always a slight overestimate of the true error.

### BERR (out)

BERR is REAL array, dimension (NRHS) The componentwise relative backward error of each solution vector X(j) (i.e., the smallest relative change in any element of A or B that makes X(j) an exact solution).

### WORK (out)

WORK is REAL array, dimension (3*N)

### IWORK (out)

IWORK is INTEGER array, dimension (N)

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

