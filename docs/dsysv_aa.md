# DSYSV_AA

DSYSV_AA computes the solution to system of linear equations A * X = B for SY matrices

## Function Signature

```fortran
DSYSV_AA(UPLO, N, NRHS, A, LDA, IPIV, B, LDB, WORK,
*                            LWORK, INFO)
```

## Description


 DSYSV computes the solution to a real system of linear equations
    A * X = B,
 where A is an N-by-N symmetric matrix and X and B are N-by-NRHS
 matrices.

 Aasen's algorithm is used to factor A as
    A = U**T * T * U,  if UPLO = 'U', or
    A = L * T * L**T,  if UPLO = 'L',
 where U (or L) is a product of permutation and unit upper (lower)
 triangular matrices, and T is symmetric tridiagonal. The factored
 form of A is then used to solve the system of equations A * X = B.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 = 'U': Upper triangle of A is stored; = 'L': Lower triangle of A is stored.

### N (in)

N is INTEGER The number of linear equations, i.e., the order of the matrix A. N >= 0.

### NRHS (in)

NRHS is INTEGER The number of right hand sides, i.e., the number of columns of the matrix B. NRHS >= 0.

### A (in,out)

A is DOUBLE PRECISION array, dimension (LDA,N) On entry, the symmetric matrix A. If UPLO = 'U', the leading N-by-N upper triangular part of A contains the upper triangular part of the matrix A, and the strictly lower triangular part of A is not referenced. If UPLO = 'L', the leading N-by-N lower triangular part of A contains the lower triangular part of the matrix A, and the strictly upper triangular part of A is not referenced. On exit, if INFO = 0, the tridiagonal matrix T and the multipliers used to obtain the factor U or L from the factorization A = U**T*T*U or A = L*T*L**T as computed by DSYTRF.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### IPIV (out)

IPIV is INTEGER array, dimension (N) On exit, it contains the details of the interchanges, i.e., the row and column k of A were interchanged with the row and column IPIV(k).

### B (in,out)

B is DOUBLE PRECISION array, dimension (LDB,NRHS) On entry, the N-by-NRHS right hand side matrix B. On exit, if INFO = 0, the N-by-NRHS solution matrix X.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,N).

### WORK (out)

WORK is DOUBLE PRECISION array, dimension (MAX(1,LWORK)) On exit, if INFO = 0, WORK(1) returns the optimal LWORK.

### LWORK (in)

LWORK is INTEGER The length of WORK. LWORK >= MAX(1,2*N,3*N-2), and for the best performance, LWORK >= MAX(1,N*NB), where NB is the optimal blocksize for DSYTRF_AA. If LWORK = -1, then a workspace query is assumed; the routine only calculates the optimal size of the WORK array, returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value > 0: if INFO = i, D(i,i) is exactly zero. The factorization has been completed, but the block diagonal matrix D is exactly singular, so the solution could not be computed.

