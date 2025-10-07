# ZSYSV_ROOK

ZSYSV_ROOK computes the solution to system of linear equations A * X = B for SY matrices

## Function Signature

```fortran
ZSYSV_ROOK(UPLO, N, NRHS, A, LDA, IPIV, B, LDB, WORK,
*                         LWORK, INFO)
```

## Description


 ZSYSV_ROOK computes the solution to a complex system of linear
 equations
    A * X = B,
 where A is an N-by-N symmetric matrix and X and B are N-by-NRHS
 matrices.

 The diagonal pivoting method is used to factor A as
    A = U * D * U**T,  if UPLO = 'U', or
    A = L * D * L**T,  if UPLO = 'L',
 where U (or L) is a product of permutation and unit upper (lower)
 triangular matrices, and D is symmetric and block diagonal with
 1-by-1 and 2-by-2 diagonal blocks.

 ZSYTRF_ROOK is called to compute the factorization of a complex
 symmetric matrix A using the bounded Bunch-Kaufman ("rook") diagonal
 pivoting method.

 The factored form of A is then used to solve the system
 of equations A * X = B by calling ZSYTRS_ROOK.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 = 'U': Upper triangle of A is stored; = 'L': Lower triangle of A is stored.

### N (in)

N is INTEGER The number of linear equations, i.e., the order of the matrix A. N >= 0.

### NRHS (in)

NRHS is INTEGER The number of right hand sides, i.e., the number of columns of the matrix B. NRHS >= 0.

### A (in,out)

A is COMPLEX*16 array, dimension (LDA,N) On entry, the symmetric matrix A. If UPLO = 'U', the leading N-by-N upper triangular part of A contains the upper triangular part of the matrix A, and the strictly lower triangular part of A is not referenced. If UPLO = 'L', the leading N-by-N lower triangular part of A contains the lower triangular part of the matrix A, and the strictly upper triangular part of A is not referenced. On exit, if INFO = 0, the block diagonal matrix D and the multipliers used to obtain the factor U or L from the factorization A = U*D*U**T or A = L*D*L**T as computed by ZSYTRF_ROOK.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### IPIV (out)

IPIV is INTEGER array, dimension (N) Details of the interchanges and the block structure of D, as determined by ZSYTRF_ROOK. If UPLO = 'U': If IPIV(k) > 0, then rows and columns k and IPIV(k) were interchanged and D(k,k) is a 1-by-1 diagonal block. If IPIV(k) < 0 and IPIV(k-1) < 0, then rows and columns k and -IPIV(k) were interchanged and rows and columns k-1 and -IPIV(k-1) were inerchaged, D(k-1:k,k-1:k) is a 2-by-2 diagonal block. If UPLO = 'L': If IPIV(k) > 0, then rows and columns k and IPIV(k) were interchanged and D(k,k) is a 1-by-1 diagonal block. If IPIV(k) < 0 and IPIV(k+1) < 0, then rows and columns k and -IPIV(k) were interchanged and rows and columns k+1 and -IPIV(k+1) were inerchaged, D(k:k+1,k:k+1) is a 2-by-2 diagonal block.

### B (in,out)

B is COMPLEX*16 array, dimension (LDB,NRHS) On entry, the N-by-NRHS right hand side matrix B. On exit, if INFO = 0, the N-by-NRHS solution matrix X.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,N).

### WORK (out)

WORK is COMPLEX*16 array, dimension (MAX(1,LWORK)) On exit, if INFO = 0, WORK(1) returns the optimal LWORK.

### LWORK (in)

LWORK is INTEGER The length of WORK. LWORK >= 1, and for best performance LWORK >= max(1,N*NB), where NB is the optimal blocksize for ZSYTRF_ROOK. TRS will be done with Level 2 BLAS If LWORK = -1, then a workspace query is assumed; the routine only calculates the optimal size of the WORK array, returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value > 0: if INFO = i, D(i,i) is exactly zero. The factorization has been completed, but the block diagonal matrix D is exactly singular, so the solution could not be computed.

