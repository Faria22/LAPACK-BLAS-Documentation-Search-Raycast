# DSPTRD

## Function Signature

```fortran
DSPTRD(UPLO, N, AP, D, E, TAU, INFO)
```

## Description


 DSPTRD reduces a real symmetric matrix A stored in packed form to
 symmetric tridiagonal form T by an orthogonal similarity
 transformation: Q**T * A * Q = T.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 = 'U': Upper triangle of A is stored; = 'L': Lower triangle of A is stored.

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### AP (in,out)

AP is DOUBLE PRECISION array, dimension (N*(N+1)/2) On entry, the upper or lower triangle of the symmetric matrix A, packed columnwise in a linear array. The j-th column of A is stored in the array AP as follows: if UPLO = 'U', AP(i + (j-1)*j/2) = A(i,j) for 1<=i<=j; if UPLO = 'L', AP(i + (j-1)*(2*n-j)/2) = A(i,j) for j<=i<=n. On exit, if UPLO = 'U', the diagonal and first superdiagonal of A are overwritten by the corresponding elements of the tridiagonal matrix T, and the elements above the first superdiagonal, with the array TAU, represent the orthogonal matrix Q as a product of elementary reflectors; if UPLO = 'L', the diagonal and first subdiagonal of A are over- written by the corresponding elements of the tridiagonal matrix T, and the elements below the first subdiagonal, with the array TAU, represent the orthogonal matrix Q as a product of elementary reflectors. See Further Details.

### D (out)

D is DOUBLE PRECISION array, dimension (N) The diagonal elements of the tridiagonal matrix T: D(i) = A(i,i).

### E (out)

E is DOUBLE PRECISION array, dimension (N-1) The off-diagonal elements of the tridiagonal matrix T: E(i) = A(i,i+1) if UPLO = 'U', E(i) = A(i+1,i) if UPLO = 'L'.

### TAU (out)

TAU is DOUBLE PRECISION array, dimension (N-1) The scalar factors of the elementary reflectors (see Further Details).

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

