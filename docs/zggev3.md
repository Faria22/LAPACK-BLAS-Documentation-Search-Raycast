# ZGGEV3

ZGGEV3 computes the eigenvalues and, optionally, the left and/or right eigenvectors for GE matrices (blocked algorithm)

## Function Signature

```fortran
ZGGEV3(JOBVL, JOBVR, N, A, LDA, B, LDB, ALPHA, BETA,
*                          VL, LDVL, VR, LDVR, WORK, LWORK, RWORK, INFO)
```

## Description


 ZGGEV3 computes for a pair of N-by-N complex nonsymmetric matrices
 (A,B), the generalized eigenvalues, and optionally, the left and/or
 right generalized eigenvectors.

 A generalized eigenvalue for a pair of matrices (A,B) is a scalar
 lambda or a ratio alpha/beta = lambda, such that A - lambda*B is
 singular. It is usually represented as the pair (alpha,beta), as
 there is a reasonable interpretation for beta=0, and even for both
 being zero.

 The right generalized eigenvector v(j) corresponding to the
 generalized eigenvalue lambda(j) of (A,B) satisfies

              A * v(j) = lambda(j) * B * v(j).

 The left generalized eigenvector u(j) corresponding to the
 generalized eigenvalues lambda(j) of (A,B) satisfies

              u(j)**H * A = lambda(j) * u(j)**H * B

 where u(j)**H is the conjugate-transpose of u(j).

## Parameters

### JOBVL (in)

JOBVL is CHARACTER*1 = 'N': do not compute the left generalized eigenvectors; = 'V': compute the left generalized eigenvectors.

### JOBVR (in)

JOBVR is CHARACTER*1 = 'N': do not compute the right generalized eigenvectors; = 'V': compute the right generalized eigenvectors.

### N (in)

N is INTEGER The order of the matrices A, B, VL, and VR. N >= 0.

### A (in,out)

A is COMPLEX*16 array, dimension (LDA, N) On entry, the matrix A in the pair (A,B). On exit, A has been overwritten.

### LDA (in)

LDA is INTEGER The leading dimension of A. LDA >= max(1,N).

### B (in,out)

B is COMPLEX*16 array, dimension (LDB, N) On entry, the matrix B in the pair (A,B). On exit, B has been overwritten.

### LDB (in)

LDB is INTEGER The leading dimension of B. LDB >= max(1,N).

### ALPHA (out)

ALPHA is COMPLEX*16 array, dimension (N)

### BETA (out)

BETA is COMPLEX*16 array, dimension (N) On exit, ALPHA(j)/BETA(j), j=1,...,N, will be the generalized eigenvalues. Note: the quotients ALPHA(j)/BETA(j) may easily over- or underflow, and BETA(j) may even be zero. Thus, the user should avoid naively computing the ratio alpha/beta. However, ALPHA will be always less than and usually comparable with norm(A) in magnitude, and BETA always less than and usually comparable with norm(B).

### VL (out)

VL is COMPLEX*16 array, dimension (LDVL,N) If JOBVL = 'V', the left generalized eigenvectors u(j) are stored one after another in the columns of VL, in the same order as their eigenvalues. Each eigenvector is scaled so the largest component has abs(real part) + abs(imag. part) = 1. Not referenced if JOBVL = 'N'.

### LDVL (in)

LDVL is INTEGER The leading dimension of the matrix VL. LDVL >= 1, and if JOBVL = 'V', LDVL >= N.

### VR (out)

VR is COMPLEX*16 array, dimension (LDVR,N) If JOBVR = 'V', the right generalized eigenvectors v(j) are stored one after another in the columns of VR, in the same order as their eigenvalues. Each eigenvector is scaled so the largest component has abs(real part) + abs(imag. part) = 1. Not referenced if JOBVR = 'N'.

### LDVR (in)

LDVR is INTEGER The leading dimension of the matrix VR. LDVR >= 1, and if JOBVR = 'V', LDVR >= N.

### WORK (out)

WORK is COMPLEX*16 array, dimension (MAX(1,LWORK)) On exit, if INFO = 0, WORK(1) returns the optimal LWORK.

### LWORK (in)

LWORK is INTEGER The dimension of the array WORK. LWORK >= MAX(1,2*N). For good performance, LWORK must generally be larger. If LWORK = -1, then a workspace query is assumed; the routine only calculates the optimal size of the WORK array, returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA.

### RWORK (out)

RWORK is DOUBLE PRECISION array, dimension (8*N)

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value. =1,...,N: The QZ iteration failed. No eigenvectors have been calculated, but ALPHA(j) and BETA(j) should be correct for j=INFO+1,...,N. > N: =N+1: other then QZ iteration failed in ZHGEQZ, =N+2: error return from ZTGEVC.

