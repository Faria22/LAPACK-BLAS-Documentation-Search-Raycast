# ZPTTRS

## Function Signature

```fortran
ZPTTRS(UPLO, N, NRHS, D, E, B, LDB, INFO)
```

## Description


 ZPTTRS solves a tridiagonal system of the form
    A * X = B
 using the factorization A = U**H *D* U or A = L*D*L**H computed by ZPTTRF.
 D is a diagonal matrix specified in the vector D, U (or L) is a unit
 bidiagonal matrix whose superdiagonal (subdiagonal) is specified in
 the vector E, and X and B are N by NRHS matrices.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 Specifies the form of the factorization and whether the vector E is the superdiagonal of the upper bidiagonal factor U or the subdiagonal of the lower bidiagonal factor L. = 'U': A = U**H *D*U, E is the superdiagonal of U = 'L': A = L*D*L**H, E is the subdiagonal of L

### N (in)

N is INTEGER The order of the tridiagonal matrix A. N >= 0.

### NRHS (in)

NRHS is INTEGER The number of right hand sides, i.e., the number of columns of the matrix B. NRHS >= 0.

### D (in)

D is DOUBLE PRECISION array, dimension (N) The n diagonal elements of the diagonal matrix D from the factorization A = U**H *D*U or A = L*D*L**H.

### E (in)

E is COMPLEX*16 array, dimension (N-1) If UPLO = 'U', the (n-1) superdiagonal elements of the unit bidiagonal factor U from the factorization A = U**H*D*U. If UPLO = 'L', the (n-1) subdiagonal elements of the unit bidiagonal factor L from the factorization A = L*D*L**H.

### B (in,out)

B is COMPLEX*16 array, dimension (LDB,NRHS) On entry, the right hand side vectors B for the system of linear equations. On exit, the solution vectors, X.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,N).

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -k, the k-th argument had an illegal value

