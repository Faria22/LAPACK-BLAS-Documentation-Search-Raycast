# DSBGVD

## Function Signature

```fortran
DSBGVD(JOBZ, UPLO, N, KA, KB, AB, LDAB, BB, LDBB, W,
*                          Z, LDZ, WORK, LWORK, IWORK, LIWORK, INFO)
```

## Description


 DSBGVD computes all the eigenvalues, and optionally, the eigenvectors
 of a real generalized symmetric-definite banded eigenproblem, of the
 form A*x=(lambda)*B*x.  Here A and B are assumed to be symmetric and
 banded, and B is also positive definite.  If eigenvectors are
 desired, it uses a divide and conquer algorithm.


## Parameters

### JOBZ (in)

JOBZ is CHARACTER*1 = 'N': Compute eigenvalues only; = 'V': Compute eigenvalues and eigenvectors.

### UPLO (in)

UPLO is CHARACTER*1 = 'U': Upper triangles of A and B are stored; = 'L': Lower triangles of A and B are stored.

### N (in)

N is INTEGER The order of the matrices A and B. N >= 0.

### KA (in)

KA is INTEGER The number of superdiagonals of the matrix A if UPLO = 'U', or the number of subdiagonals if UPLO = 'L'. KA >= 0.

### KB (in)

KB is INTEGER The number of superdiagonals of the matrix B if UPLO = 'U', or the number of subdiagonals if UPLO = 'L'. KB >= 0.

### AB (in,out)

AB is DOUBLE PRECISION array, dimension (LDAB, N) On entry, the upper or lower triangle of the symmetric band matrix A, stored in the first ka+1 rows of the array. The j-th column of A is stored in the j-th column of the array AB as follows: if UPLO = 'U', AB(ka+1+i-j,j) = A(i,j) for max(1,j-ka)<=i<=j; if UPLO = 'L', AB(1+i-j,j) = A(i,j) for j<=i<=min(n,j+ka). On exit, the contents of AB are destroyed.

### LDAB (in)

LDAB is INTEGER The leading dimension of the array AB. LDAB >= KA+1.

### BB (in,out)

BB is DOUBLE PRECISION array, dimension (LDBB, N) On entry, the upper or lower triangle of the symmetric band matrix B, stored in the first kb+1 rows of the array. The j-th column of B is stored in the j-th column of the array BB as follows: if UPLO = 'U', BB(ka+1+i-j,j) = B(i,j) for max(1,j-kb)<=i<=j; if UPLO = 'L', BB(1+i-j,j) = B(i,j) for j<=i<=min(n,j+kb). On exit, the factor S from the split Cholesky factorization B = S**T*S, as returned by DPBSTF.

### LDBB (in)

LDBB is INTEGER The leading dimension of the array BB. LDBB >= KB+1.

### W (out)

W is DOUBLE PRECISION array, dimension (N) If INFO = 0, the eigenvalues in ascending order.

### Z (out)

Z is DOUBLE PRECISION array, dimension (LDZ, N) If JOBZ = 'V', then if INFO = 0, Z contains the matrix Z of eigenvectors, with the i-th column of Z holding the eigenvector associated with W(i). The eigenvectors are normalized so Z**T*B*Z = I. If JOBZ = 'N', then Z is not referenced.

### LDZ (in)

LDZ is INTEGER The leading dimension of the array Z. LDZ >= 1, and if JOBZ = 'V', LDZ >= max(1,N).

### WORK (out)

WORK is DOUBLE PRECISION array, dimension (MAX(1,LWORK)) On exit, if INFO = 0, WORK(1) returns the optimal LWORK.

### LWORK (in)

LWORK is INTEGER The dimension of the array WORK. If N <= 1, LWORK >= 1. If JOBZ = 'N' and N > 1, LWORK >= 2*N. If JOBZ = 'V' and N > 1, LWORK >= 1 + 5*N + 2*N**2. If LWORK = -1, then a workspace query is assumed; the routine only calculates the optimal sizes of the WORK and IWORK arrays, returns these values as the first entries of the WORK and IWORK arrays, and no error message related to LWORK or LIWORK is issued by XERBLA.

### IWORK (out)

IWORK is INTEGER array, dimension (MAX(1,LIWORK)) On exit, if LIWORK > 0, IWORK(1) returns the optimal LIWORK.

### LIWORK (in)

LIWORK is INTEGER The dimension of the array IWORK. If JOBZ = 'N' or N <= 1, LIWORK >= 1. If JOBZ = 'V' and N > 1, LIWORK >= 3 + 5*N. If LIWORK = -1, then a workspace query is assumed; the routine only calculates the optimal sizes of the WORK and IWORK arrays, returns these values as the first entries of the WORK and IWORK arrays, and no error message related to LWORK or LIWORK is issued by XERBLA.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value > 0: if INFO = i, and i is: <= N: the algorithm failed to converge: i off-diagonal elements of an intermediate tridiagonal form did not converge to zero; > N: if INFO = N + i, for 1 <= i <= N, then DPBSTF returned INFO = i: B is not positive definite. The factorization of B could not be completed and no eigenvalues or eigenvectors were computed.

