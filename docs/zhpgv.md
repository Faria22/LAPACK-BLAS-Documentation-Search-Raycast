# ZHPGV

## Function Signature

```fortran
ZHPGV(ITYPE, JOBZ, UPLO, N, AP, BP, W, Z, LDZ, WORK,
*                         RWORK, INFO)
```

## Description


 ZHPGV computes all the eigenvalues and, optionally, the eigenvectors
 of a complex generalized Hermitian-definite eigenproblem, of the form
 A*x=(lambda)*B*x,  A*Bx=(lambda)*x,  or B*A*x=(lambda)*x.
 Here A and B are assumed to be Hermitian, stored in packed format,
 and B is also positive definite.

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

AP is COMPLEX*16 array, dimension (N*(N+1)/2) On entry, the upper or lower triangle of the Hermitian matrix A, packed columnwise in a linear array. The j-th column of A is stored in the array AP as follows: if UPLO = 'U', AP(i + (j-1)*j/2) = A(i,j) for 1<=i<=j; if UPLO = 'L', AP(i + (j-1)*(2*n-j)/2) = A(i,j) for j<=i<=n. On exit, the contents of AP are destroyed.

### BP (in,out)

BP is COMPLEX*16 array, dimension (N*(N+1)/2) On entry, the upper or lower triangle of the Hermitian matrix B, packed columnwise in a linear array. The j-th column of B is stored in the array BP as follows: if UPLO = 'U', BP(i + (j-1)*j/2) = B(i,j) for 1<=i<=j; if UPLO = 'L', BP(i + (j-1)*(2*n-j)/2) = B(i,j) for j<=i<=n. On exit, the triangular factor U or L from the Cholesky factorization B = U**H*U or B = L*L**H, in the same storage format as B.

### W (out)

W is DOUBLE PRECISION array, dimension (N) If INFO = 0, the eigenvalues in ascending order.

### Z (out)

Z is COMPLEX*16 array, dimension (LDZ, N) If JOBZ = 'V', then if INFO = 0, Z contains the matrix Z of eigenvectors. The eigenvectors are normalized as follows: if ITYPE = 1 or 2, Z**H*B*Z = I; if ITYPE = 3, Z**H*inv(B)*Z = I. If JOBZ = 'N', then Z is not referenced.

### LDZ (in)

LDZ is INTEGER The leading dimension of the array Z. LDZ >= 1, and if JOBZ = 'V', LDZ >= max(1,N).

### WORK (out)

WORK is COMPLEX*16 array, dimension (max(1, 2*N-1))

### RWORK (out)

RWORK is DOUBLE PRECISION array, dimension (max(1, 3*N-2))

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value > 0: ZPPTRF or ZHPEV returned an error code: <= N: if INFO = i, ZHPEV failed to converge; i off-diagonal elements of an intermediate tridiagonal form did not convergeto zero; > N: if INFO = N + i, for 1 <= i <= n, then the leading principal minor of order i of B is not positive. The factorization of B could not be completed and no eigenvalues or eigenvectors were computed.

