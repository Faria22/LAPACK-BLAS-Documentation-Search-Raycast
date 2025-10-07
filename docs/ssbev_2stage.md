# SSBEV_2STAGE

SSBEV_2STAGE computes the eigenvalues and, optionally, the left and/or right eigenvectors for OTHER matrices

## Function Signature

```fortran
SSBEV_2STAGE(JOBZ, UPLO, N, KD, AB, LDAB, W, Z, LDZ,
*                                WORK, LWORK, INFO)
```

## Description


 SSBEV_2STAGE computes all the eigenvalues and, optionally, eigenvectors of
 a real symmetric band matrix A using the 2stage technique for
 the reduction to tridiagonal.

## Parameters

### JOBZ (in)

JOBZ is CHARACTER*1 = 'N': Compute eigenvalues only; = 'V': Compute eigenvalues and eigenvectors. Not available in this release.

### UPLO (in)

UPLO is CHARACTER*1 = 'U': Upper triangle of A is stored; = 'L': Lower triangle of A is stored.

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### KD (in)

KD is INTEGER The number of superdiagonals of the matrix A if UPLO = 'U', or the number of subdiagonals if UPLO = 'L'. KD >= 0.

### AB (in,out)

AB is REAL array, dimension (LDAB, N) On entry, the upper or lower triangle of the symmetric band matrix A, stored in the first KD+1 rows of the array. The j-th column of A is stored in the j-th column of the array AB as follows: if UPLO = 'U', AB(kd+1+i-j,j) = A(i,j) for max(1,j-kd)<=i<=j; if UPLO = 'L', AB(1+i-j,j) = A(i,j) for j<=i<=min(n,j+kd). On exit, AB is overwritten by values generated during the reduction to tridiagonal form. If UPLO = 'U', the first superdiagonal and the diagonal of the tridiagonal matrix T are returned in rows KD and KD+1 of AB, and if UPLO = 'L', the diagonal and first subdiagonal of T are returned in the first two rows of AB.

### LDAB (in)

LDAB is INTEGER The leading dimension of the array AB. LDAB >= KD + 1.

### W (out)

W is REAL array, dimension (N) If INFO = 0, the eigenvalues in ascending order.

### Z (out)

Z is REAL array, dimension (LDZ, N) If JOBZ = 'V', then if INFO = 0, Z contains the orthonormal eigenvectors of the matrix A, with the i-th column of Z holding the eigenvector associated with W(i). If JOBZ = 'N', then Z is not referenced.

### LDZ (in)

LDZ is INTEGER The leading dimension of the array Z. LDZ >= 1, and if JOBZ = 'V', LDZ >= max(1,N).

### WORK (out)

WORK is REAL array, dimension LWORK On exit, if INFO = 0, WORK(1) returns the optimal LWORK.

### LWORK (in)

LWORK is INTEGER The length of the array WORK. LWORK >= 1, when N <= 1; otherwise If JOBZ = 'N' and N > 1, LWORK must be queried. LWORK = MAX(1, dimension) where dimension = (2KD+1)*N + KD*NTHREADS + N where KD is the size of the band. NTHREADS is the number of threads used when openMP compilation is enabled, otherwise =1. If JOBZ = 'V' and N > 1, LWORK must be queried. Not yet available. If LWORK = -1, then a workspace query is assumed; the routine only calculates the optimal size of the WORK array, returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value > 0: if INFO = i, the algorithm failed to converge; i off-diagonal elements of an intermediate tridiagonal form did not converge to zero.

