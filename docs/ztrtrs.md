# ZTRTRS

## Function Signature

```fortran
ZTRTRS(UPLO, TRANS, DIAG, N, NRHS, A, LDA, B, LDB,
*                          INFO)
```

## Description


 ZTRTRS solves a triangular system of the form

    A * X = B,  A**T * X = B,  or  A**H * X = B,

 where A is a triangular matrix of order N, and B is an N-by-NRHS matrix.

 This subroutine verifies that A is nonsingular, but callers should note that only exact
 singularity is detected. It is conceivable for one or more diagonal elements of A to be
 subnormally tiny numbers without this subroutine signalling an error.

 If a possible loss of numerical precision due to near-singular matrices is a concern, the
 caller should verify that A is nonsingular within some tolerance before calling this subroutine.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 = 'U': A is upper triangular; = 'L': A is lower triangular.

### TRANS (in)

TRANS is CHARACTER*1 Specifies the form of the system of equations: = 'N': A * X = B (No transpose) = 'T': A**T * X = B (Transpose) = 'C': A**H * X = B (Conjugate transpose)

### DIAG (in)

DIAG is CHARACTER*1 = 'N': A is non-unit triangular; = 'U': A is unit triangular.

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### NRHS (in)

NRHS is INTEGER The number of right hand sides, i.e., the number of columns of the matrix B. NRHS >= 0.

### A (in)

A is COMPLEX*16 array, dimension (LDA,N) The triangular matrix A. If UPLO = 'U', the leading N-by-N upper triangular part of the array A contains the upper triangular matrix, and the strictly lower triangular part of A is not referenced. If UPLO = 'L', the leading N-by-N lower triangular part of the array A contains the lower triangular matrix, and the strictly upper triangular part of A is not referenced. If DIAG = 'U', the diagonal elements of A are also not referenced and are assumed to be 1.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### B (in,out)

B is COMPLEX*16 array, dimension (LDB,NRHS) On entry, the right hand side matrix B. On exit, if INFO = 0, the solution matrix X.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,N).

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value > 0: if INFO = i, the i-th diagonal element of A is exactly zero, indicating that the matrix is singular and the solutions X have not been computed.

