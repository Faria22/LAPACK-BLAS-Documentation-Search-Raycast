# ZGBRFS

## Function Signature

```fortran
ZGBRFS(TRANS, N, KL, KU, NRHS, AB, LDAB, AFB, LDAFB,
*                          IPIV, B, LDB, X, LDX, FERR, BERR, WORK, RWORK,
*                          INFO)
```

## Description


 ZGBRFS improves the computed solution to a system of linear
 equations when the coefficient matrix is banded, and provides
 error bounds and backward error estimates for the solution.

## Parameters

### TRANS (in)

TRANS is CHARACTER*1 Specifies the form of the system of equations: = 'N': A * X = B (No transpose) = 'T': A**T * X = B (Transpose) = 'C': A**H * X = B (Conjugate transpose)

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### KL (in)

KL is INTEGER The number of subdiagonals within the band of A. KL >= 0.

### KU (in)

KU is INTEGER The number of superdiagonals within the band of A. KU >= 0.

### NRHS (in)

NRHS is INTEGER The number of right hand sides, i.e., the number of columns of the matrices B and X. NRHS >= 0.

### AB (in)

AB is COMPLEX*16 array, dimension (LDAB,N) The original band matrix A, stored in rows 1 to KL+KU+1. The j-th column of A is stored in the j-th column of the array AB as follows: AB(ku+1+i-j,j) = A(i,j) for max(1,j-ku)<=i<=min(n,j+kl).

### LDAB (in)

LDAB is INTEGER The leading dimension of the array AB. LDAB >= KL+KU+1.

### AFB (in)

AFB is COMPLEX*16 array, dimension (LDAFB,N) Details of the LU factorization of the band matrix A, as computed by ZGBTRF. U is stored as an upper triangular band matrix with KL+KU superdiagonals in rows 1 to KL+KU+1, and the multipliers used during the factorization are stored in rows KL+KU+2 to 2*KL+KU+1.

### LDAFB (in)

LDAFB is INTEGER The leading dimension of the array AFB. LDAFB >= 2*KL*KU+1.

### IPIV (in)

IPIV is INTEGER array, dimension (N) The pivot indices from ZGBTRF; for 1<=i<=N, row i of the matrix was interchanged with row IPIV(i).

### B (in)

B is COMPLEX*16 array, dimension (LDB,NRHS) The right hand side matrix B.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,N).

### X (in,out)

X is COMPLEX*16 array, dimension (LDX,NRHS) On entry, the solution matrix X, as computed by ZGBTRS. On exit, the improved solution matrix X.

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

