# SPORFS

## Function Signature

```fortran
SPORFS(UPLO, N, NRHS, A, LDA, AF, LDAF, B, LDB, X,
*                          LDX, FERR, BERR, WORK, IWORK, INFO)
```

## Description


 SPORFS improves the computed solution to a system of linear
 equations when the coefficient matrix is symmetric positive definite,
 and provides error bounds and backward error estimates for the
 solution.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 = 'U': Upper triangle of A is stored; = 'L': Lower triangle of A is stored.

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### NRHS (in)

NRHS is INTEGER The number of right hand sides, i.e., the number of columns of the matrices B and X. NRHS >= 0.

### A (in)

A is REAL array, dimension (LDA,N) The symmetric matrix A. If UPLO = 'U', the leading N-by-N upper triangular part of A contains the upper triangular part of the matrix A, and the strictly lower triangular part of A is not referenced. If UPLO = 'L', the leading N-by-N lower triangular part of A contains the lower triangular part of the matrix A, and the strictly upper triangular part of A is not referenced.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### AF (in)

AF is REAL array, dimension (LDAF,N) The triangular factor U or L from the Cholesky factorization A = U**T*U or A = L*L**T, as computed by SPOTRF.

### LDAF (in)

LDAF is INTEGER The leading dimension of the array AF. LDAF >= max(1,N).

### B (in)

B is REAL array, dimension (LDB,NRHS) The right hand side matrix B.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,N).

### X (in,out)

X is REAL array, dimension (LDX,NRHS) On entry, the solution matrix X, as computed by SPOTRS. On exit, the improved solution matrix X.

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

