# ZGBTRS

## Function Signature

```fortran
ZGBTRS(TRANS, N, KL, KU, NRHS, AB, LDAB, IPIV, B, LDB,
*                          INFO)
```

## Description


 ZGBTRS solves a system of linear equations
    A * X = B,  A**T * X = B,  or  A**H * X = B
 with a general band matrix A using the LU factorization computed
 by ZGBTRF.

## Parameters

### TRANS (in)

TRANS is CHARACTER*1 Specifies the form of the system of equations. = 'N': A * X = B (No transpose) = 'T': A**T * X = B (Transpose) = 'C': A**H * X = B (Conjugate transpose)

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### KL (in)

KL is INTEGER The number of subdiagonals within the band of A. KL >= 0.

### KU (in)

KU is INTEGER The number of superdiagonals within the band of A. KU >= 0.

### NRHS (in)

NRHS is INTEGER The number of right hand sides, i.e., the number of columns of the matrix B. NRHS >= 0.

### AB (in)

AB is COMPLEX*16 array, dimension (LDAB,N) Details of the LU factorization of the band matrix A, as computed by ZGBTRF. U is stored as an upper triangular band matrix with KL+KU superdiagonals in rows 1 to KL+KU+1, and the multipliers used during the factorization are stored in rows KL+KU+2 to 2*KL+KU+1.

### LDAB (in)

LDAB is INTEGER The leading dimension of the array AB. LDAB >= 2*KL+KU+1.

### IPIV (in)

IPIV is INTEGER array, dimension (N) The pivot indices; for 1 <= i <= N, row i of the matrix was interchanged with row IPIV(i).

### B (in,out)

B is COMPLEX*16 array, dimension (LDB,NRHS) On entry, the right hand side matrix B. On exit, the solution matrix X.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,N).

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

