# ZHPRFS

## Function Signature

```fortran
ZHPRFS(UPLO, N, NRHS, AP, AFP, IPIV, B, LDB, X, LDX,
*                          FERR, BERR, WORK, RWORK, INFO)
```

## Description


 ZHPRFS improves the computed solution to a system of linear
 equations when the coefficient matrix is Hermitian indefinite
 and packed, and provides error bounds and backward error estimates
 for the solution.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 = 'U': Upper triangle of A is stored; = 'L': Lower triangle of A is stored.

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### NRHS (in)

NRHS is INTEGER The number of right hand sides, i.e., the number of columns of the matrices B and X. NRHS >= 0.

### AP (in)

AP is COMPLEX*16 array, dimension (N*(N+1)/2) The upper or lower triangle of the Hermitian matrix A, packed columnwise in a linear array. The j-th column of A is stored in the array AP as follows: if UPLO = 'U', AP(i + (j-1)*j/2) = A(i,j) for 1<=i<=j; if UPLO = 'L', AP(i + (j-1)*(2*n-j)/2) = A(i,j) for j<=i<=n.

### AFP (in)

AFP is COMPLEX*16 array, dimension (N*(N+1)/2) The factored form of the matrix A. AFP contains the block diagonal matrix D and the multipliers used to obtain the factor U or L from the factorization A = U*D*U**H or A = L*D*L**H as computed by ZHPTRF, stored as a packed triangular matrix.

### IPIV (in)

IPIV is INTEGER array, dimension (N) Details of the interchanges and the block structure of D as determined by ZHPTRF.

### B (in)

B is COMPLEX*16 array, dimension (LDB,NRHS) The right hand side matrix B.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,N).

### X (in,out)

X is COMPLEX*16 array, dimension (LDX,NRHS) On entry, the solution matrix X, as computed by ZHPTRS. On exit, the improved solution matrix X.

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

