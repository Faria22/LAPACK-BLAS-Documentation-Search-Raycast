# DPTTRS

## Function Signature

```fortran
DPTTRS(N, NRHS, D, E, B, LDB, INFO)
```

## Description


 DPTTRS solves a tridiagonal system of the form
    A * X = B
 using the L*D*L**T factorization of A computed by DPTTRF.  D is a
 diagonal matrix specified in the vector D, L is a unit bidiagonal
 matrix whose subdiagonal is specified in the vector E, and X and B
 are N by NRHS matrices.

## Parameters

### N (in)

N is INTEGER The order of the tridiagonal matrix A. N >= 0.

### NRHS (in)

NRHS is INTEGER The number of right hand sides, i.e., the number of columns of the matrix B. NRHS >= 0.

### D (in)

D is DOUBLE PRECISION array, dimension (N) The n diagonal elements of the diagonal matrix D from the L*D*L**T factorization of A.

### E (in)

E is DOUBLE PRECISION array, dimension (N-1) The (n-1) subdiagonal elements of the unit bidiagonal factor L from the L*D*L**T factorization of A. E can also be regarded as the superdiagonal of the unit bidiagonal factor U from the factorization A = U**T*D*U.

### B (in,out)

B is DOUBLE PRECISION array, dimension (LDB,NRHS) On entry, the right hand side vectors B for the system of linear equations. On exit, the solution vectors, X.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,N).

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -k, the k-th argument had an illegal value

