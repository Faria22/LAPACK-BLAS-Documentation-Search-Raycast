# ZSTEQR

## Function Signature

```fortran
ZSTEQR(COMPZ, N, D, E, Z, LDZ, WORK, INFO)
```

## Description


 ZSTEQR computes all eigenvalues and, optionally, eigenvectors of a
 symmetric tridiagonal matrix using the implicit QL or QR method.
 The eigenvectors of a full or band complex Hermitian matrix can also
 be found if ZHETRD or ZHPTRD or ZHBTRD has been used to reduce this
 matrix to tridiagonal form.

## Parameters

### COMPZ (in)

COMPZ is CHARACTER*1 = 'N': Compute eigenvalues only. = 'V': Compute eigenvalues and eigenvectors of the original Hermitian matrix. On entry, Z must contain the unitary matrix used to reduce the original matrix to tridiagonal form. = 'I': Compute eigenvalues and eigenvectors of the tridiagonal matrix. Z is initialized to the identity matrix.

### N (in)

N is INTEGER The order of the matrix. N >= 0.

### D (in,out)

D is DOUBLE PRECISION array, dimension (N) On entry, the diagonal elements of the tridiagonal matrix. On exit, if INFO = 0, the eigenvalues in ascending order.

### E (in,out)

E is DOUBLE PRECISION array, dimension (N-1) On entry, the (n-1) subdiagonal elements of the tridiagonal matrix. On exit, E has been destroyed.

### Z (in,out)

Z is COMPLEX*16 array, dimension (LDZ, N) On entry, if COMPZ = 'V', then Z contains the unitary matrix used in the reduction to tridiagonal form. On exit, if INFO = 0, then if COMPZ = 'V', Z contains the orthonormal eigenvectors of the original Hermitian matrix, and if COMPZ = 'I', Z contains the orthonormal eigenvectors of the symmetric tridiagonal matrix. If COMPZ = 'N', then Z is not referenced.

### LDZ (in)

LDZ is INTEGER The leading dimension of the array Z. LDZ >= 1, and if eigenvectors are desired, then LDZ >= max(1,N).

### WORK (out)

WORK is DOUBLE PRECISION array, dimension (max(1,2*N-2)) If COMPZ = 'N', then WORK is not referenced.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value > 0: the algorithm has failed to find all the eigenvalues in a total of 30*N iterations; if INFO = i, then i elements of E have not converged to zero; on exit, D and E contain the elements of a symmetric tridiagonal matrix which is unitarily similar to the original matrix.

