# SSTEV

SSTEV computes the eigenvalues and, optionally, the left and/or right eigenvectors for OTHER matrices

## Function Signature

```fortran
SSTEV(JOBZ, N, D, E, Z, LDZ, WORK, INFO)
```

## Description


 SSTEV computes all eigenvalues and, optionally, eigenvectors of a
 real symmetric tridiagonal matrix A.

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

WORK is REAL array, dimension (max(1,2*N-2)) If JOBZ = 'N', WORK is not referenced.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value > 0: if INFO = i, the algorithm failed to converge; i off-diagonal elements of E did not converge to zero.

