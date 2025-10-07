# ZHPEV

ZHPEV computes the eigenvalues and, optionally, the left and/or right eigenvectors for OTHER matrices

## Function Signature

```fortran
ZHPEV(JOBZ, UPLO, N, AP, W, Z, LDZ, WORK, RWORK,
*                         INFO)
```

## Description


 ZHPEV computes all the eigenvalues and, optionally, eigenvectors of a
 complex Hermitian matrix in packed storage.

## Parameters

### JOBZ (in)

JOBZ is CHARACTER*1 = 'N': Compute eigenvalues only; = 'V': Compute eigenvalues and eigenvectors.

### UPLO (in)

UPLO is CHARACTER*1 = 'U': Upper triangle of A is stored; = 'L': Lower triangle of A is stored.

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### AP (in,out)

AP is COMPLEX*16 array, dimension (N*(N+1)/2) On entry, the upper or lower triangle of the Hermitian matrix A, packed columnwise in a linear array. The j-th column of A is stored in the array AP as follows: if UPLO = 'U', AP(i + (j-1)*j/2) = A(i,j) for 1<=i<=j; if UPLO = 'L', AP(i + (j-1)*(2*n-j)/2) = A(i,j) for j<=i<=n. On exit, AP is overwritten by values generated during the reduction to tridiagonal form. If UPLO = 'U', the diagonal and first superdiagonal of the tridiagonal matrix T overwrite the corresponding elements of A, and if UPLO = 'L', the diagonal and first subdiagonal of T overwrite the corresponding elements of A.

### W (out)

W is DOUBLE PRECISION array, dimension (N) If INFO = 0, the eigenvalues in ascending order.

### Z (out)

Z is COMPLEX*16 array, dimension (LDZ, N) If JOBZ = 'V', then if INFO = 0, Z contains the orthonormal eigenvectors of the matrix A, with the i-th column of Z holding the eigenvector associated with W(i). If JOBZ = 'N', then Z is not referenced.

### LDZ (in)

LDZ is INTEGER The leading dimension of the array Z. LDZ >= 1, and if JOBZ = 'V', LDZ >= max(1,N).

### WORK (out)

WORK is COMPLEX*16 array, dimension (max(1, 2*N-1))

### RWORK (out)

RWORK is DOUBLE PRECISION array, dimension (max(1, 3*N-2))

### INFO (out)

INFO is INTEGER = 0: successful exit. < 0: if INFO = -i, the i-th argument had an illegal value. > 0: if INFO = i, the algorithm failed to converge; i off-diagonal elements of an intermediate tridiagonal form did not converge to zero.

