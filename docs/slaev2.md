# SLAEV2

## Function Signature

```fortran
SLAEV2(A, B, C, RT1, RT2, CS1, SN1)
```

## Description


 SLAEV2 computes the eigendecomposition of a 2-by-2 symmetric matrix
    [  A   B  ]
    [  B   C  ].
 On return, RT1 is the eigenvalue of larger absolute value, RT2 is the
 eigenvalue of smaller absolute value, and (CS1,SN1) is the unit right
 eigenvector for RT1, giving the decomposition

    [ CS1  SN1 ] [  A   B  ] [ CS1 -SN1 ]  =  [ RT1  0  ]
    [-SN1  CS1 ] [  B   C  ] [ SN1  CS1 ]     [  0  RT2 ].

## Parameters

### A (in)

A is REAL The (1,1) element of the 2-by-2 matrix.

### B (in)

B is REAL The (1,2) element and the conjugate of the (2,1) element of the 2-by-2 matrix.

### C (in)

C is REAL The (2,2) element of the 2-by-2 matrix.

### RT1 (out)

RT1 is REAL The eigenvalue of larger absolute value.

### RT2 (out)

RT2 is REAL The eigenvalue of smaller absolute value.

### CS1 (out)

CS1 is REAL

### SN1 (out)

SN1 is REAL The vector (CS1, SN1) is a unit right eigenvector for RT1.

