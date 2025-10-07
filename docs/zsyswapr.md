# ZSYSWAPR

## Function Signature

```fortran
ZSYSWAPR(UPLO, N, A, LDA, I1, I2)
```

## Description


 ZSYSWAPR applies an elementary permutation on the rows and the columns of
 a symmetric matrix.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 Specifies whether the details of the factorization are stored as an upper or lower triangular matrix. = 'U': Upper triangular, form is A = U*D*U**T; = 'L': Lower triangular, form is A = L*D*L**T.

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### A (in,out)

A is COMPLEX*16 array, dimension (LDA,*) On entry, the N-by-N matrix A. On exit, the permuted matrix where the rows I1 and I2 and columns I1 and I2 are interchanged. If UPLO = 'U', the interchanges are applied to the upper triangular part and the strictly lower triangular part of A is not referenced; if UPLO = 'L', the interchanges are applied to the lower triangular part and the part of A above the diagonal is not referenced.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### I1 (in)

I1 is INTEGER Index of the first row to swap

### I2 (in)

I2 is INTEGER Index of the second row to swap

