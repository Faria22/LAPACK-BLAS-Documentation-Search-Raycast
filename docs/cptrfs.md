# CPTRFS

## Function Signature

```fortran
CPTRFS(UPLO, N, NRHS, D, E, DF, EF, B, LDB, X, LDX,
*                          FERR, BERR, WORK, RWORK, INFO)
```

## Description


 CPTRFS improves the computed solution to a system of linear
 equations when the coefficient matrix is Hermitian positive definite
 and tridiagonal, and provides error bounds and backward error
 estimates for the solution.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 Specifies whether the superdiagonal or the subdiagonal of the tridiagonal matrix A is stored and the form of the factorization: = 'U': E is the superdiagonal of A, and A = U**H*D*U; = 'L': E is the subdiagonal of A, and A = L*D*L**H. (The two forms are equivalent if A is real.)

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### NRHS (in)

NRHS is INTEGER The number of right hand sides, i.e., the number of columns of the matrix B. NRHS >= 0.

### D (in)

D is REAL array, dimension (N) The n real diagonal elements of the tridiagonal matrix A.

### E (in)

E is COMPLEX array, dimension (N-1) The (n-1) off-diagonal elements of the tridiagonal matrix A (see UPLO).

### DF (in)

DF is REAL array, dimension (N) The n diagonal elements of the diagonal matrix D from the factorization computed by CPTTRF.

### EF (in)

EF is COMPLEX array, dimension (N-1) The (n-1) off-diagonal elements of the unit bidiagonal factor U or L from the factorization computed by CPTTRF (see UPLO).

### B (in)

B is COMPLEX array, dimension (LDB,NRHS) The right hand side matrix B.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,N).

### X (in,out)

X is COMPLEX array, dimension (LDX,NRHS) On entry, the solution matrix X, as computed by CPTTRS. On exit, the improved solution matrix X.

### LDX (in)

LDX is INTEGER The leading dimension of the array X. LDX >= max(1,N).

### FERR (out)

FERR is REAL array, dimension (NRHS) The forward error bound for each solution vector X(j) (the j-th column of the solution matrix X). If XTRUE is the true solution corresponding to X(j), FERR(j) is an estimated upper bound for the magnitude of the largest element in (X(j) - XTRUE) divided by the magnitude of the largest element in X(j).

### BERR (out)

BERR is REAL array, dimension (NRHS) The componentwise relative backward error of each solution vector X(j) (i.e., the smallest relative change in any element of A or B that makes X(j) an exact solution).

### WORK (out)

WORK is COMPLEX array, dimension (N)

### RWORK (out)

RWORK is REAL array, dimension (N)

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

