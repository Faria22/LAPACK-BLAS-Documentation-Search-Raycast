# ZPBRFS

## Function Signature

```fortran
ZPBRFS(UPLO, N, KD, NRHS, AB, LDAB, AFB, LDAFB, B,
*                          LDB, X, LDX, FERR, BERR, WORK, RWORK, INFO)
```

## Description


 ZPBRFS improves the computed solution to a system of linear
 equations when the coefficient matrix is Hermitian positive definite
 and banded, and provides error bounds and backward error estimates
 for the solution.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 = 'U': Upper triangle of A is stored; = 'L': Lower triangle of A is stored.

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### KD (in)

KD is INTEGER The number of superdiagonals of the matrix A if UPLO = 'U', or the number of subdiagonals if UPLO = 'L'. KD >= 0.

### NRHS (in)

NRHS is INTEGER The number of right hand sides, i.e., the number of columns of the matrices B and X. NRHS >= 0.

### AB (in)

AB is COMPLEX*16 array, dimension (LDAB,N) The upper or lower triangle of the Hermitian band matrix A, stored in the first KD+1 rows of the array. The j-th column of A is stored in the j-th column of the array AB as follows: if UPLO = 'U', AB(kd+1+i-j,j) = A(i,j) for max(1,j-kd)<=i<=j; if UPLO = 'L', AB(1+i-j,j) = A(i,j) for j<=i<=min(n,j+kd).

### LDAB (in)

LDAB is INTEGER The leading dimension of the array AB. LDAB >= KD+1.

### AFB (in)

AFB is COMPLEX*16 array, dimension (LDAFB,N) The triangular factor U or L from the Cholesky factorization A = U**H*U or A = L*L**H of the band matrix A as computed by ZPBTRF, in the same storage format as A (see AB).

### LDAFB (in)

LDAFB is INTEGER The leading dimension of the array AFB. LDAFB >= KD+1.

### B (in)

B is COMPLEX*16 array, dimension (LDB,NRHS) The right hand side matrix B.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,N).

### X (in,out)

X is COMPLEX*16 array, dimension (LDX,NRHS) On entry, the solution matrix X, as computed by ZPBTRS. On exit, the improved solution matrix X.

### LDX (in)

LDX is INTEGER The leading dimension of the array X. LDX >= max(1,N).

### FERR (out)

FERR is DOUBLE PRECISION array, dimension (NRHS) The estimated forward error bound for each solution vector X(j) (the j-th column of the solution matrix X). If XTRUE is the true solution corresponding to X(j), FERR(j) is an estimated upper bound for the magnitude of the largest element in (X(j) - XTRUE) divided by the magnitude of the largest element in X(j). The estimate is as reliable as the estimate for RCOND, and is almost always a slight overestimate of the true error.

### BERR (out)

BERR is DOUBLE PRECISION array, dimension (NRHS) The componentwise relative backward error of each solution vector X(j) (i.e., the smallest relative change in any element of A or B that makes X(j) an exact solution).

### WORK (out)

WORK is COMPLEX*16 array, dimension (2*N)

### RWORK (out)

RWORK is DOUBLE PRECISION array, dimension (N)

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

