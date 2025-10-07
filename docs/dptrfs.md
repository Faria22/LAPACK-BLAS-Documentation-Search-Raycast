# DPTRFS

## Function Signature

```fortran
DPTRFS(N, NRHS, D, E, DF, EF, B, LDB, X, LDX, FERR,
*                          BERR, WORK, INFO)
```

## Description


 DPTRFS improves the computed solution to a system of linear
 equations when the coefficient matrix is symmetric positive definite
 and tridiagonal, and provides error bounds and backward error
 estimates for the solution.

## Parameters

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### NRHS (in)

NRHS is INTEGER The number of right hand sides, i.e., the number of columns of the matrix B. NRHS >= 0.

### D (in)

D is DOUBLE PRECISION array, dimension (N) The n diagonal elements of the tridiagonal matrix A.

### E (in)

E is DOUBLE PRECISION array, dimension (N-1) The (n-1) subdiagonal elements of the tridiagonal matrix A.

### DF (in)

DF is DOUBLE PRECISION array, dimension (N) The n diagonal elements of the diagonal matrix D from the factorization computed by DPTTRF.

### EF (in)

EF is DOUBLE PRECISION array, dimension (N-1) The (n-1) subdiagonal elements of the unit bidiagonal factor L from the factorization computed by DPTTRF.

### B (in)

B is DOUBLE PRECISION array, dimension (LDB,NRHS) The right hand side matrix B.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,N).

### X (in,out)

X is DOUBLE PRECISION array, dimension (LDX,NRHS) On entry, the solution matrix X, as computed by DPTTRS. On exit, the improved solution matrix X.

### LDX (in)

LDX is INTEGER The leading dimension of the array X. LDX >= max(1,N).

### FERR (out)

FERR is DOUBLE PRECISION array, dimension (NRHS) The forward error bound for each solution vector X(j) (the j-th column of the solution matrix X). If XTRUE is the true solution corresponding to X(j), FERR(j) is an estimated upper bound for the magnitude of the largest element in (X(j) - XTRUE) divided by the magnitude of the largest element in X(j).

### BERR (out)

BERR is DOUBLE PRECISION array, dimension (NRHS) The componentwise relative backward error of each solution vector X(j) (i.e., the smallest relative change in any element of A or B that makes X(j) an exact solution).

### WORK (out)

WORK is DOUBLE PRECISION array, dimension (2*N)

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

