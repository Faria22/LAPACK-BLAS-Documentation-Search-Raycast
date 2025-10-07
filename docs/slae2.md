# SLAE2

## Function Signature

```fortran
SLAE2(A, B, C, RT1, RT2)
```

## Description


 SLAE2  computes the eigenvalues of a 2-by-2 symmetric matrix
    [  A   B  ]
    [  B   C  ].
 On return, RT1 is the eigenvalue of larger absolute value, and RT2
 is the eigenvalue of smaller absolute value.

## Parameters

### A (in)

A is REAL The (1,1) element of the 2-by-2 matrix.

### B (in)

B is REAL The (1,2) and (2,1) elements of the 2-by-2 matrix.

### C (in)

C is REAL The (2,2) element of the 2-by-2 matrix.

### RT1 (out)

RT1 is REAL The eigenvalue of larger absolute value.

### RT2 (out)

RT2 is REAL The eigenvalue of smaller absolute value.

