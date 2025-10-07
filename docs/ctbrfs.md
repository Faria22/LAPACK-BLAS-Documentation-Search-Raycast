# CTBRFS

## Function Signature

```fortran
CTBRFS(UPLO, TRANS, DIAG, N, KD, NRHS, AB, LDAB, B,
*                          LDB, X, LDX, FERR, BERR, WORK, RWORK, INFO)
```

## Description


 CTBRFS provides error bounds and backward error estimates for the
 solution to a system of linear equations with a triangular band
 coefficient matrix.

 The solution matrix X must be computed by CTBTRS or some other
 means before entering this routine.  CTBRFS does not do iterative
 refinement because doing so cannot improve the backward error.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 = 'U': A is upper triangular; = 'L': A is lower triangular.

### TRANS (in)

TRANS is CHARACTER*1 Specifies the form of the system of equations: = 'N': A * X = B (No transpose) = 'T': A**T * X = B (Transpose) = 'C': A**H * X = B (Conjugate transpose)

### DIAG (in)

DIAG is CHARACTER*1 = 'N': A is non-unit triangular; = 'U': A is unit triangular.

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### KD (in)

KD is INTEGER The number of superdiagonals or subdiagonals of the triangular band matrix A. KD >= 0.

### NRHS (in)

NRHS is INTEGER The number of right hand sides, i.e., the number of columns of the matrices B and X. NRHS >= 0.

### AB (in)

AB is COMPLEX array, dimension (LDAB,N) The upper or lower triangular band matrix A, stored in the first kd+1 rows of the array. The j-th column of A is stored in the j-th column of the array AB as follows: if UPLO = 'U', AB(kd+1+i-j,j) = A(i,j) for max(1,j-kd)<=i<=j; if UPLO = 'L', AB(1+i-j,j) = A(i,j) for j<=i<=min(n,j+kd). If DIAG = 'U', the diagonal elements of A are not referenced and are assumed to be 1.

### LDAB (in)

LDAB is INTEGER The leading dimension of the array AB. LDAB >= KD+1.

### B (in)

B is COMPLEX array, dimension (LDB,NRHS) The right hand side matrix B.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,N).

### X (in)

X is COMPLEX array, dimension (LDX,NRHS) The solution matrix X.

### LDX (in)

LDX is INTEGER The leading dimension of the array X. LDX >= max(1,N).

### FERR (out)

FERR is REAL array, dimension (NRHS) The estimated forward error bound for each solution vector X(j) (the j-th column of the solution matrix X). If XTRUE is the true solution corresponding to X(j), FERR(j) is an estimated upper bound for the magnitude of the largest element in (X(j) - XTRUE) divided by the magnitude of the largest element in X(j). The estimate is as reliable as the estimate for RCOND, and is almost always a slight overestimate of the true error.

### BERR (out)

BERR is REAL array, dimension (NRHS) The componentwise relative backward error of each solution vector X(j) (i.e., the smallest relative change in any element of A or B that makes X(j) an exact solution).

### WORK (out)

WORK is COMPLEX array, dimension (2*N)

### RWORK (out)

RWORK is REAL array, dimension (N)

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

