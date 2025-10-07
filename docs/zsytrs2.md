# ZSYTRS2

## Function Signature

```fortran
ZSYTRS2(UPLO, N, NRHS, A, LDA, IPIV, B, LDB,
*                           WORK, INFO)
```

## Description


 ZSYTRS2 solves a system of linear equations A*X = B with a complex
 symmetric matrix A using the factorization A = U*D*U**T or
 A = L*D*L**T computed by ZSYTRF and converted by ZSYCONV.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 Specifies whether the details of the factorization are stored as an upper or lower triangular matrix. = 'U': Upper triangular, form is A = U*D*U**T; = 'L': Lower triangular, form is A = L*D*L**T.

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### NRHS (in)

NRHS is INTEGER The number of right hand sides, i.e., the number of columns of the matrix B. NRHS >= 0.

### A (in,out)

A is COMPLEX*16 array, dimension (LDA,N) The block diagonal matrix D and the multipliers used to obtain the factor U or L as computed by ZSYTRF. Note that A is input / output. This might be counter-intuitive, and one may think that A is input only. A is input / output. This is because, at the start of the subroutine, we permute A in a "better" form and then we permute A back to its original form at the end.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### IPIV (in)

IPIV is INTEGER array, dimension (N) Details of the interchanges and the block structure of D as determined by ZSYTRF.

### B (in,out)

B is COMPLEX*16 array, dimension (LDB,NRHS) On entry, the right hand side matrix B. On exit, the solution matrix X.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,N).

### WORK (out)

WORK is COMPLEX*16 array, dimension (N)

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

