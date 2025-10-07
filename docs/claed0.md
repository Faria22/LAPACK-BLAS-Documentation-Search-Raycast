# CLAED0

## Function Signature

```fortran
CLAED0(QSIZ, N, D, E, Q, LDQ, QSTORE, LDQS, RWORK,
*                          IWORK, INFO)
```

## Description


 Using the divide and conquer method, CLAED0 computes all eigenvalues
 of a symmetric tridiagonal matrix which is one diagonal block of
 those from reducing a dense or band Hermitian matrix and
 corresponding eigenvectors of the dense or band matrix.

## Parameters

### QSIZ (in)

QSIZ is INTEGER The dimension of the unitary matrix used to reduce the full matrix to tridiagonal form. QSIZ >= N if ICOMPQ = 1.

### N (in)

N is INTEGER The dimension of the symmetric tridiagonal matrix. N >= 0.

### D (in,out)

D is REAL array, dimension (N) On entry, the diagonal elements of the tridiagonal matrix. On exit, the eigenvalues in ascending order.

### E (in,out)

E is REAL array, dimension (N-1) On entry, the off-diagonal elements of the tridiagonal matrix. On exit, E has been destroyed.

### Q (in,out)

Q is COMPLEX array, dimension (LDQ,N) On entry, Q must contain an QSIZ x N matrix whose columns unitarily orthonormal. It is a part of the unitary matrix that reduces the full dense Hermitian matrix to a (reducible) symmetric tridiagonal matrix.

### LDQ (in)

LDQ is INTEGER The leading dimension of the array Q. LDQ >= max(1,N).

### IWORK (out)

IWORK is INTEGER array, the dimension of IWORK must be at least 6 + 6*N + 5*N*lg N ( lg( N ) = smallest integer k such that 2^k >= N )

### RWORK (out)

RWORK is REAL array, dimension (1 + 3*N + 2*N*lg N + 3*N**2) ( lg( N ) = smallest integer k such that 2^k >= N )

### QSTORE (out)

QSTORE is COMPLEX array, dimension (LDQS, N) Used to store parts of the eigenvector matrix when the updating matrix multiplies take place.

### LDQS (in)

LDQS is INTEGER The leading dimension of the array QSTORE. LDQS >= max(1,N).

### INFO (out)

INFO is INTEGER = 0: successful exit. < 0: if INFO = -i, the i-th argument had an illegal value. > 0: The algorithm failed to compute an eigenvalue while working on the submatrix lying in rows and columns INFO/(N+1) through mod(INFO,N+1).

