# DLAE2

## Function Signature

```fortran
DLAE2(A, B, C, RT1, RT2)
```

## Description


 DLAE2  computes the eigenvalues of a 2-by-2 symmetric matrix
    [  A   B  ]
    [  B   C  ].
 On return, RT1 is the eigenvalue of larger absolute value, and RT2
 is the eigenvalue of smaller absolute value.

## Parameters

### A (in)

A is DOUBLE PRECISION The (1,1) element of the 2-by-2 matrix.

### B (in)

B is DOUBLE PRECISION The (1,2) and (2,1) elements of the 2-by-2 matrix.

### C (in)

C is DOUBLE PRECISION The (2,2) element of the 2-by-2 matrix.

### RT1 (out)

RT1 is DOUBLE PRECISION The eigenvalue of larger absolute value.

### RT2 (out)

RT2 is DOUBLE PRECISION The eigenvalue of smaller absolute value.

