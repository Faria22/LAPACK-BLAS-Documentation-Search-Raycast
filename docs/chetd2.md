# CHETD2

## Function Signature

```fortran
CHETD2(UPLO, N, A, LDA, D, E, TAU, INFO)
```

## Description


 CHETD2 reduces a complex Hermitian matrix A to real symmetric
 tridiagonal form T by a unitary similarity transformation:
 Q**H * A * Q = T.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 Specifies whether the upper or lower triangular part of the Hermitian matrix A is stored: = 'U': Upper triangular = 'L': Lower triangular

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### A (in,out)

A is COMPLEX array, dimension (LDA,N) On entry, the Hermitian matrix A. If UPLO = 'U', the leading n-by-n upper triangular part of A contains the upper triangular part of the matrix A, and the strictly lower triangular part of A is not referenced. If UPLO = 'L', the leading n-by-n lower triangular part of A contains the lower triangular part of the matrix A, and the strictly upper triangular part of A is not referenced. On exit, if UPLO = 'U', the diagonal and first superdiagonal of A are overwritten by the corresponding elements of the tridiagonal matrix T, and the elements above the first superdiagonal, with the array TAU, represent the unitary matrix Q as a product of elementary reflectors; if UPLO = 'L', the diagonal and first subdiagonal of A are over- written by the corresponding elements of the tridiagonal matrix T, and the elements below the first subdiagonal, with the array TAU, represent the unitary matrix Q as a product of elementary reflectors. See Further Details.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### D (out)

D is REAL array, dimension (N) The diagonal elements of the tridiagonal matrix T: D(i) = A(i,i).

### E (out)

E is REAL array, dimension (N-1) The off-diagonal elements of the tridiagonal matrix T: E(i) = A(i,i+1) if UPLO = 'U', E(i) = A(i+1,i) if UPLO = 'L'.

### TAU (out)

TAU is COMPLEX array, dimension (N-1) The scalar factors of the elementary reflectors (see Further Details).

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value.

