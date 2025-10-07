# ZGTSV

ZGTSV computes the solution to system of linear equations A * X = B for GT matrices

## Function Signature

```fortran
ZGTSV(N, NRHS, DL, D, DU, B, LDB, INFO)
```

## Description


 ZGTSV  solves the equation

    A*X = B,

 where A is an N-by-N tridiagonal matrix, by Gaussian elimination with
 partial pivoting.

 Note that the equation  A**T *X = B  may be solved by interchanging the
 order of the arguments DU and DL.

## Parameters

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### NRHS (in)

NRHS is INTEGER The number of right hand sides, i.e., the number of columns of the matrix B. NRHS >= 0.

### DL (in,out)

DL is COMPLEX*16 array, dimension (N-1) On entry, DL must contain the (n-1) subdiagonal elements of A. On exit, DL is overwritten by the (n-2) elements of the second superdiagonal of the upper triangular matrix U from the LU factorization of A, in DL(1), ..., DL(n-2).

### D (in,out)

D is COMPLEX*16 array, dimension (N) On entry, D must contain the diagonal elements of A. On exit, D is overwritten by the n diagonal elements of U.

### DU (in,out)

DU is COMPLEX*16 array, dimension (N-1) On entry, DU must contain the (n-1) superdiagonal elements of A. On exit, DU is overwritten by the (n-1) elements of the first superdiagonal of U.

### B (in,out)

B is COMPLEX*16 array, dimension (LDB,NRHS) On entry, the N-by-NRHS right hand side matrix B. On exit, if INFO = 0, the N-by-NRHS solution matrix X.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,N).

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value > 0: if INFO = i, U(i,i) is exactly zero, and the solution has not been computed. The factorization has not been completed unless i = N.

