# CHESWAPR

## Function Signature

```fortran
CHESWAPR(UPLO, N, A, LDA, I1, I2)
```

## Description


 CHESWAPR applies an elementary permutation on the rows and the columns of
 a hermitian matrix.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 Specifies whether the details of the factorization are stored as an upper or lower triangular matrix. = 'U': Upper triangular, form is A = U*D*U**T; = 'L': Lower triangular, form is A = L*D*L**T.

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### A (in,out)

A is COMPLEX array, dimension (LDA,N) On entry, the NB diagonal matrix D and the multipliers used to obtain the factor U or L as computed by CSYTRF. On exit, if INFO = 0, the (symmetric) inverse of the original matrix. If UPLO = 'U', the upper triangular part of the inverse is formed and the part of A below the diagonal is not referenced; if UPLO = 'L' the lower triangular part of the inverse is formed and the part of A above the diagonal is not referenced.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### I1 (in)

I1 is INTEGER Index of the first row to swap

### I2 (in)

I2 is INTEGER Index of the second row to swap

