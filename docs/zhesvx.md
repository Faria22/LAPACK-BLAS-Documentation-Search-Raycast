# ZHESVX

ZHESVX computes the solution to system of linear equations A * X = B for HE matrices

## Function Signature

```fortran
ZHESVX(FACT, UPLO, N, NRHS, A, LDA, AF, LDAF, IPIV, B,
*                          LDB, X, LDX, RCOND, FERR, BERR, WORK, LWORK,
*                          RWORK, INFO)
```

## Description


 ZHESVX uses the diagonal pivoting factorization to compute the
 solution to a complex system of linear equations A * X = B,
 where A is an N-by-N Hermitian matrix and X and B are N-by-NRHS
 matrices.

 Error bounds on the solution and a condition estimate are also
 provided.

## Parameters

### FACT (in)

FACT is CHARACTER*1 Specifies whether or not the factored form of A has been supplied on entry. = 'F': On entry, AF and IPIV contain the factored form of A. A, AF and IPIV will not be modified. = 'N': The matrix A will be copied to AF and factored.

### UPLO (in)

UPLO is CHARACTER*1 = 'U': Upper triangle of A is stored; = 'L': Lower triangle of A is stored.

### N (in)

N is INTEGER The number of linear equations, i.e., the order of the matrix A. N >= 0.

### NRHS (in)

NRHS is INTEGER The number of right hand sides, i.e., the number of columns of the matrices B and X. NRHS >= 0.

### A (in)

A is COMPLEX*16 array, dimension (LDA,N) The Hermitian matrix A. If UPLO = 'U', the leading N-by-N upper triangular part of A contains the upper triangular part of the matrix A, and the strictly lower triangular part of A is not referenced. If UPLO = 'L', the leading N-by-N lower triangular part of A contains the lower triangular part of the matrix A, and the strictly upper triangular part of A is not referenced.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### AF (in,out)

AF is COMPLEX*16 array, dimension (LDAF,N) If FACT = 'F', then AF is an input argument and on entry contains the block diagonal matrix D and the multipliers used to obtain the factor U or L from the factorization A = U*D*U**H or A = L*D*L**H as computed by ZHETRF. If FACT = 'N', then AF is an output argument and on exit returns the block diagonal matrix D and the multipliers used to obtain the factor U or L from the factorization A = U*D*U**H or A = L*D*L**H.

### LDAF (in)

LDAF is INTEGER The leading dimension of the array AF. LDAF >= max(1,N).

### IPIV (in,out)

IPIV is INTEGER array, dimension (N) If FACT = 'F', then IPIV is an input argument and on entry contains details of the interchanges and the block structure of D, as determined by ZHETRF. If IPIV(k) > 0, then rows and columns k and IPIV(k) were interchanged and D(k,k) is a 1-by-1 diagonal block. If UPLO = 'U' and IPIV(k) = IPIV(k-1) < 0, then rows and columns k-1 and -IPIV(k) were interchanged and D(k-1:k,k-1:k) is a 2-by-2 diagonal block. If UPLO = 'L' and IPIV(k) = IPIV(k+1) < 0, then rows and columns k+1 and -IPIV(k) were interchanged and D(k:k+1,k:k+1) is a 2-by-2 diagonal block. If FACT = 'N', then IPIV is an output argument and on exit contains details of the interchanges and the block structure of D, as determined by ZHETRF.

### B (in)

B is COMPLEX*16 array, dimension (LDB,NRHS) The N-by-NRHS right hand side matrix B.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,N).

### X (out)

X is COMPLEX*16 array, dimension (LDX,NRHS) If INFO = 0 or INFO = N+1, the N-by-NRHS solution matrix X.

### LDX (in)

LDX is INTEGER The leading dimension of the array X. LDX >= max(1,N).

### RCOND (out)

RCOND is DOUBLE PRECISION The estimate of the reciprocal condition number of the matrix A. If RCOND is less than the machine precision (in particular, if RCOND = 0), the matrix is singular to working precision. This condition is indicated by a return code of INFO > 0.

### FERR (out)

FERR is DOUBLE PRECISION array, dimension (NRHS) The estimated forward error bound for each solution vector X(j) (the j-th column of the solution matrix X). If XTRUE is the true solution corresponding to X(j), FERR(j) is an estimated upper bound for the magnitude of the largest element in (X(j) - XTRUE) divided by the magnitude of the largest element in X(j). The estimate is as reliable as the estimate for RCOND, and is almost always a slight overestimate of the true error.

### BERR (out)

BERR is DOUBLE PRECISION array, dimension (NRHS) The componentwise relative backward error of each solution vector X(j) (i.e., the smallest relative change in any element of A or B that makes X(j) an exact solution).

### WORK (out)

WORK is COMPLEX*16 array, dimension (MAX(1,LWORK)) On exit, if INFO = 0, WORK(1) returns the optimal LWORK.

### LWORK (in)

LWORK is INTEGER The length of WORK. LWORK >= MAX(1,2*N), and for best performance, when FACT = 'N', LWORK >= MAX(1,2*N,N*NB), where NB is the optimal blocksize for ZHETRF. If LWORK = -1, then a workspace query is assumed; the routine only calculates the optimal size of the WORK array, returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA.

### RWORK (out)

RWORK is DOUBLE PRECISION array, dimension (N)

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value > 0: if INFO = i, and i is <= N: D(i,i) is exactly zero. The factorization has been completed but the factor D is exactly singular, so the solution and error bounds could not be computed. RCOND = 0 is returned. = N+1: D is nonsingular, but RCOND is less than machine precision, meaning that the matrix is singular to working precision. Nevertheless, the solution and error bounds are computed because there are a number of situations where the computed solution can be more accurate than the value of RCOND would suggest.

