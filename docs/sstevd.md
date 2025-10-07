# SSTEVD

SSTEVD computes the eigenvalues and, optionally, the left and/or right eigenvectors for OTHER matrices

## Function Signature

```fortran
SSTEVD(JOBZ, N, D, E, Z, LDZ, WORK, LWORK, IWORK,
*                          LIWORK, INFO)
```

## Description


 SSTEVD computes all eigenvalues and, optionally, eigenvectors of a
 real symmetric tridiagonal matrix. If eigenvectors are desired, it
 uses a divide and conquer algorithm.


## Parameters

### JOBZ (in)

JOBZ is CHARACTER*1 = 'N': Compute eigenvalues only; = 'V': Compute eigenvalues and eigenvectors.

### N (in)

N is INTEGER The order of the matrix. N >= 0.

### D (in,out)

D is REAL array, dimension (N) On entry, the n diagonal elements of the tridiagonal matrix A. On exit, if INFO = 0, the eigenvalues in ascending order.

### E (in,out)

E is REAL array, dimension (N-1) On entry, the (n-1) subdiagonal elements of the tridiagonal matrix A, stored in elements 1 to N-1 of E. On exit, the contents of E are destroyed.

### Z (out)

Z is REAL array, dimension (LDZ, N) If JOBZ = 'V', then if INFO = 0, Z contains the orthonormal eigenvectors of the matrix A, with the i-th column of Z holding the eigenvector associated with D(i). If JOBZ = 'N', then Z is not referenced.

### LDZ (in)

LDZ is INTEGER The leading dimension of the array Z. LDZ >= 1, and if JOBZ = 'V', LDZ >= max(1,N).

### WORK (out)

WORK is REAL array, dimension (LWORK) On exit, if INFO = 0, WORK(1) returns the optimal LWORK.

### LWORK (in)

LWORK is INTEGER The dimension of the array WORK. If JOBZ = 'N' or N <= 1 then LWORK must be at least 1. If JOBZ = 'V' and N > 1 then LWORK must be at least ( 1 + 4*N + N**2 ). If LWORK = -1, then a workspace query is assumed; the routine only calculates the optimal sizes of the WORK and IWORK arrays, returns these values as the first entries of the WORK and IWORK arrays, and no error message related to LWORK or LIWORK is issued by XERBLA.

### IWORK (out)

IWORK is INTEGER array, dimension (MAX(1,LIWORK)) On exit, if INFO = 0, IWORK(1) returns the optimal LIWORK.

### LIWORK (in)

LIWORK is INTEGER The dimension of the array IWORK. If JOBZ = 'N' or N <= 1 then LIWORK must be at least 1. If JOBZ = 'V' and N > 1 then LIWORK must be at least 3+5*N. If LIWORK = -1, then a workspace query is assumed; the routine only calculates the optimal sizes of the WORK and IWORK arrays, returns these values as the first entries of the WORK and IWORK arrays, and no error message related to LWORK or LIWORK is issued by XERBLA.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value > 0: if INFO = i, the algorithm failed to converge; i off-diagonal elements of E did not converge to zero.

