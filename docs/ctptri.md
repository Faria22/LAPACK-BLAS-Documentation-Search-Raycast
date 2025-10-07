# CTPTRI

## Function Signature

```fortran
CTPTRI(UPLO, DIAG, N, AP, INFO)
```

## Description


 CTPTRI computes the inverse of a complex upper or lower triangular
 matrix A stored in packed format.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 = 'U': A is upper triangular; = 'L': A is lower triangular.

### DIAG (in)

DIAG is CHARACTER*1 = 'N': A is non-unit triangular; = 'U': A is unit triangular.

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### AP (in,out)

AP is COMPLEX array, dimension (N*(N+1)/2) On entry, the upper or lower triangular matrix A, stored columnwise in a linear array. The j-th column of A is stored in the array AP as follows: if UPLO = 'U', AP(i + (j-1)*j/2) = A(i,j) for 1<=i<=j; if UPLO = 'L', AP(i + (j-1)*((2*n-j)/2) = A(i,j) for j<=i<=n. See below for further details. On exit, the (triangular) inverse of the original matrix, in the same packed storage format.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value > 0: if INFO = i, A(i,i) is exactly zero. The triangular matrix is singular and its inverse can not be computed.

