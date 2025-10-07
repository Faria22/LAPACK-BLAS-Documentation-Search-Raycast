# CHPGVD

## Function Signature

```fortran
CHPGVD(ITYPE, JOBZ, UPLO, N, AP, BP, W, Z, LDZ, WORK,
*                          LWORK, RWORK, LRWORK, IWORK, LIWORK, INFO)
```

## Description


 CHPGVD computes all the eigenvalues and, optionally, the eigenvectors
 of a complex generalized Hermitian-definite eigenproblem, of the form
 A*x=(lambda)*B*x,  A*Bx=(lambda)*x,  or B*A*x=(lambda)*x.  Here A and
 B are assumed to be Hermitian, stored in packed format, and B is also
 positive definite.
 If eigenvectors are desired, it uses a divide and conquer algorithm.


## Parameters

### ITYPE (in)

ITYPE is INTEGER Specifies the problem type to be solved: = 1: A*x = (lambda)*B*x = 2: A*B*x = (lambda)*x = 3: B*A*x = (lambda)*x

### JOBZ (in)

JOBZ is CHARACTER*1 = 'N': Compute eigenvalues only; = 'V': Compute eigenvalues and eigenvectors.

### UPLO (in)

UPLO is CHARACTER*1 = 'U': Upper triangles of A and B are stored; = 'L': Lower triangles of A and B are stored.

### N (in)

N is INTEGER The order of the matrices A and B. N >= 0.

### AP (in,out)

AP is COMPLEX array, dimension (N*(N+1)/2) On entry, the upper or lower triangle of the Hermitian matrix A, packed columnwise in a linear array. The j-th column of A is stored in the array AP as follows: if UPLO = 'U', AP(i + (j-1)*j/2) = A(i,j) for 1<=i<=j; if UPLO = 'L', AP(i + (j-1)*(2*n-j)/2) = A(i,j) for j<=i<=n. On exit, the contents of AP are destroyed.

### BP (in,out)

BP is COMPLEX array, dimension (N*(N+1)/2) On entry, the upper or lower triangle of the Hermitian matrix B, packed columnwise in a linear array. The j-th column of B is stored in the array BP as follows: if UPLO = 'U', BP(i + (j-1)*j/2) = B(i,j) for 1<=i<=j; if UPLO = 'L', BP(i + (j-1)*(2*n-j)/2) = B(i,j) for j<=i<=n. On exit, the triangular factor U or L from the Cholesky factorization B = U**H*U or B = L*L**H, in the same storage format as B.

### W (out)

W is REAL array, dimension (N) If INFO = 0, the eigenvalues in ascending order.

### Z (out)

Z is COMPLEX array, dimension (LDZ, N) If JOBZ = 'V', then if INFO = 0, Z contains the matrix Z of eigenvectors. The eigenvectors are normalized as follows: if ITYPE = 1 or 2, Z**H*B*Z = I; if ITYPE = 3, Z**H*inv(B)*Z = I. If JOBZ = 'N', then Z is not referenced.

### LDZ (in)

LDZ is INTEGER The leading dimension of the array Z. LDZ >= 1, and if JOBZ = 'V', LDZ >= max(1,N).

### WORK (out)

WORK is COMPLEX array, dimension (MAX(1,LWORK)) On exit, if INFO = 0, WORK(1) returns the required LWORK.

### LWORK (in)

LWORK is INTEGER The dimension of array WORK. If N <= 1, LWORK >= 1. If JOBZ = 'N' and N > 1, LWORK >= N. If JOBZ = 'V' and N > 1, LWORK >= 2*N. If LWORK = -1, then a workspace query is assumed; the routine only calculates the required sizes of the WORK, RWORK and IWORK arrays, returns these values as the first entries of the WORK, RWORK and IWORK arrays, and no error message related to LWORK or LRWORK or LIWORK is issued by XERBLA.

### RWORK (out)

RWORK is REAL array, dimension (MAX(1,LRWORK)) On exit, if INFO = 0, RWORK(1) returns the required LRWORK.

### LRWORK (in)

LRWORK is INTEGER The dimension of array RWORK. If N <= 1, LRWORK >= 1. If JOBZ = 'N' and N > 1, LRWORK >= N. If JOBZ = 'V' and N > 1, LRWORK >= 1 + 5*N + 2*N**2. If LRWORK = -1, then a workspace query is assumed; the routine only calculates the required sizes of the WORK, RWORK and IWORK arrays, returns these values as the first entries of the WORK, RWORK and IWORK arrays, and no error message related to LWORK or LRWORK or LIWORK is issued by XERBLA.

### IWORK (out)

IWORK is INTEGER array, dimension (MAX(1,LIWORK)) On exit, if INFO = 0, IWORK(1) returns the required LIWORK.

### LIWORK (in)

LIWORK is INTEGER The dimension of array IWORK. If JOBZ = 'N' or N <= 1, LIWORK >= 1. If JOBZ = 'V' and N > 1, LIWORK >= 3 + 5*N. If LIWORK = -1, then a workspace query is assumed; the routine only calculates the required sizes of the WORK, RWORK and IWORK arrays, returns these values as the first entries of the WORK, RWORK and IWORK arrays, and no error message related to LWORK or LRWORK or LIWORK is issued by XERBLA.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value > 0: CPPTRF or CHPEVD returned an error code: <= N: if INFO = i, CHPEVD failed to converge; i off-diagonal elements of an intermediate tridiagonal form did not convergeto zero; > N: if INFO = N + i, for 1 <= i <= n, then the leading principal minor of order i of B is not positive. The factorization of B could not be completed and no eigenvalues or eigenvectors were computed.

