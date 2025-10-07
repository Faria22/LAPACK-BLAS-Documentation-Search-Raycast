# CLASET

## Function Signature

```fortran
CLASET(UPLO, M, N, ALPHA, BETA, A, LDA)
```

## Description


 CLASET initializes a 2-D array A to BETA on the diagonal and
 ALPHA on the offdiagonals.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 Specifies the part of the matrix A to be set. = 'U': Upper triangular part is set. The lower triangle is unchanged. = 'L': Lower triangular part is set. The upper triangle is unchanged. Otherwise: All of the matrix A is set.

### M (in)

M is INTEGER On entry, M specifies the number of rows of A.

### N (in)

N is INTEGER On entry, N specifies the number of columns of A.

### ALPHA (in)

ALPHA is COMPLEX All the offdiagonal array elements are set to ALPHA.

### BETA (in)

BETA is COMPLEX All the diagonal array elements are set to BETA.

### A (out)

A is COMPLEX array, dimension (LDA,N) On entry, the m by n matrix A. On exit, A(i,j) = ALPHA, 1 <= i <= m, 1 <= j <= n, i.ne.j; A(i,i) = BETA , 1 <= i <= min(m,n)

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,M).

