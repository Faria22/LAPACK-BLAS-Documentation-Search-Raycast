# ZSYTRI_ROOK

## Function Signature

```fortran
ZSYTRI_ROOK(UPLO, N, A, LDA, IPIV, WORK, INFO)
```

## Description


 ZSYTRI_ROOK computes the inverse of a complex symmetric
 matrix A using the factorization A = U*D*U**T or A = L*D*L**T
 computed by ZSYTRF_ROOK.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 Specifies whether the details of the factorization are stored as an upper or lower triangular matrix. = 'U': Upper triangular, form is A = U*D*U**T; = 'L': Lower triangular, form is A = L*D*L**T.

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### A (in,out)

A is COMPLEX*16 array, dimension (LDA,N) On entry, the block diagonal matrix D and the multipliers used to obtain the factor U or L as computed by ZSYTRF_ROOK. On exit, if INFO = 0, the (symmetric) inverse of the original matrix. If UPLO = 'U', the upper triangular part of the inverse is formed and the part of A below the diagonal is not referenced; if UPLO = 'L' the lower triangular part of the inverse is formed and the part of A above the diagonal is not referenced.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### IPIV (in)

IPIV is INTEGER array, dimension (N) Details of the interchanges and the block structure of D as determined by ZSYTRF_ROOK.

### WORK (out)

WORK is COMPLEX*16 array, dimension (N)

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value > 0: if INFO = i, D(i,i) = 0; the matrix is singular and its inverse could not be computed.

