# DPFTRS

## Function Signature

```fortran
DPFTRS(TRANSR, UPLO, N, NRHS, A, B, LDB, INFO)
```

## Description


 DPFTRS solves a system of linear equations A*X = B with a symmetric
 positive definite matrix A using the Cholesky factorization
 A = U**T*U or A = L*L**T computed by DPFTRF.

## Parameters

### TRANSR (in)

TRANSR is CHARACTER*1 = 'N': The Normal TRANSR of RFP A is stored; = 'T': The Transpose TRANSR of RFP A is stored.

### UPLO (in)

UPLO is CHARACTER*1 = 'U': Upper triangle of RFP A is stored; = 'L': Lower triangle of RFP A is stored.

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### NRHS (in)

NRHS is INTEGER The number of right hand sides, i.e., the number of columns of the matrix B. NRHS >= 0.

### A (in)

A is DOUBLE PRECISION array, dimension ( N*(N+1)/2 ). The triangular factor U or L from the Cholesky factorization of RFP A = U**T*U or RFP A = L*L**T, as computed by DPFTRF. See note below for more details about RFP A.

### B (in,out)

B is DOUBLE PRECISION array, dimension (LDB,NRHS) On entry, the right hand side matrix B. On exit, the solution matrix X.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,N).

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

