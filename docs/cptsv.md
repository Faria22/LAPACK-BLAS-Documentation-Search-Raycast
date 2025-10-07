# CPTSV

CPTSV computes the solution to system of linear equations A * X = B for PT matrices

## Function Signature

```fortran
CPTSV(N, NRHS, D, E, B, LDB, INFO)
```

## Description


 CPTSV computes the solution to a complex system of linear equations
 A*X = B, where A is an N-by-N Hermitian positive definite tridiagonal
 matrix, and X and B are N-by-NRHS matrices.

 A is factored as A = L*D*L**H, and the factored form of A is then
 used to solve the system of equations.

## Parameters

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### NRHS (in)

NRHS is INTEGER The number of right hand sides, i.e., the number of columns of the matrix B. NRHS >= 0.

### D (in,out)

D is REAL array, dimension (N) On entry, the n diagonal elements of the tridiagonal matrix A. On exit, the n diagonal elements of the diagonal matrix D from the factorization A = L*D*L**H.

### E (in,out)

E is COMPLEX array, dimension (N-1) On entry, the (n-1) subdiagonal elements of the tridiagonal matrix A. On exit, the (n-1) subdiagonal elements of the unit bidiagonal factor L from the L*D*L**H factorization of A. E can also be regarded as the superdiagonal of the unit bidiagonal factor U from the U**H*D*U factorization of A.

### B (in,out)

B is COMPLEX array, dimension (LDB,NRHS) On entry, the N-by-NRHS right hand side matrix B. On exit, if INFO = 0, the N-by-NRHS solution matrix X.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,N).

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value > 0: if INFO = i, the leading principal minor of order i is not positive, and the solution has not been computed. The factorization has not been completed unless i = N.

