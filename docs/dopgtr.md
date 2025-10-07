# DOPGTR

## Function Signature

```fortran
DOPGTR(UPLO, N, AP, TAU, Q, LDQ, WORK, INFO)
```

## Description


 DOPGTR generates a real orthogonal matrix Q which is defined as the
 product of n-1 elementary reflectors H(i) of order n, as returned by
 DSPTRD using packed storage:

 if UPLO = 'U', Q = H(n-1) . . . H(2) H(1),

 if UPLO = 'L', Q = H(1) H(2) . . . H(n-1).

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 = 'U': Upper triangular packed storage used in previous call to DSPTRD; = 'L': Lower triangular packed storage used in previous call to DSPTRD.

### N (in)

N is INTEGER The order of the matrix Q. N >= 0.

### AP (in)

AP is DOUBLE PRECISION array, dimension (N*(N+1)/2) The vectors which define the elementary reflectors, as returned by DSPTRD.

### TAU (in)

TAU is DOUBLE PRECISION array, dimension (N-1) TAU(i) must contain the scalar factor of the elementary reflector H(i), as returned by DSPTRD.

### Q (out)

Q is DOUBLE PRECISION array, dimension (LDQ,N) The N-by-N orthogonal matrix Q.

### LDQ (in)

LDQ is INTEGER The leading dimension of the array Q. LDQ >= max(1,N).

### WORK (out)

WORK is DOUBLE PRECISION array, dimension (N-1)

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

