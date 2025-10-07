# ZPPTRF

## Function Signature

```fortran
ZPPTRF(UPLO, N, AP, INFO)
```

## Description


 ZPPTRF computes the Cholesky factorization of a complex Hermitian
 positive definite matrix A stored in packed format.

 The factorization has the form
    A = U**H * U,  if UPLO = 'U', or
    A = L  * L**H,  if UPLO = 'L',
 where U is an upper triangular matrix and L is lower triangular.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 = 'U': Upper triangle of A is stored; = 'L': Lower triangle of A is stored.

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### AP (in,out)

AP is COMPLEX*16 array, dimension (N*(N+1)/2) On entry, the upper or lower triangle of the Hermitian matrix A, packed columnwise in a linear array. The j-th column of A is stored in the array AP as follows: if UPLO = 'U', AP(i + (j-1)*j/2) = A(i,j) for 1<=i<=j; if UPLO = 'L', AP(i + (j-1)*(2n-j)/2) = A(i,j) for j<=i<=n. See below for further details. On exit, if INFO = 0, the triangular factor U or L from the Cholesky factorization A = U**H*U or A = L*L**H, in the same storage format as A.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value > 0: if INFO = i, the leading principal minor of order i is not positive, and the factorization could not be completed.

