# ZLA_GERPVGRW

## Function Signature

```fortran
ZLA_GERPVGRW(N, NCOLS, A, LDA, AF,
*                                               LDAF)
```

## Description



 ZLA_GERPVGRW computes the reciprocal pivot growth factor
 norm(A)/norm(U). The "max absolute element" norm is used. If this is
 much less than 1, the stability of the LU factorization of the
 (equilibrated) matrix A could be poor. This also means that the
 solution X, estimated condition numbers, and error bounds could be
 unreliable.

## Parameters

### N (in)

N is INTEGER The number of linear equations, i.e., the order of the matrix A. N >= 0.

### NCOLS (in)

NCOLS is INTEGER The number of columns of the matrix A. NCOLS >= 0.

### A (in)

A is COMPLEX*16 array, dimension (LDA,N) On entry, the N-by-N matrix A.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### AF (in)

AF is COMPLEX*16 array, dimension (LDAF,N) The factors L and U from the factorization A = P*L*U as computed by ZGETRF.

### LDAF (in)

LDAF is INTEGER The leading dimension of the array AF. LDAF >= max(1,N).

