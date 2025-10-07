# CLAESY

## Function Signature

```fortran
CLAESY(A, B, C, RT1, RT2, EVSCAL, CS1, SN1)
```

## Description


 CLAESY computes the eigendecomposition of a 2-by-2 symmetric matrix
    ( ( A, B );( B, C ) )
 provided the norm of the matrix of eigenvectors is larger than
 some threshold value.

 RT1 is the eigenvalue of larger absolute value, and RT2 of
 smaller absolute value.  If the eigenvectors are computed, then
 on return ( CS1, SN1 ) is the unit eigenvector for RT1, hence

 [  CS1     SN1   ] . [ A  B ] . [ CS1    -SN1   ] = [ RT1  0  ]
 [ -SN1     CS1   ]   [ B  C ]   [ SN1     CS1   ]   [  0  RT2 ]

## Parameters

### A (in)

A is COMPLEX The ( 1, 1 ) element of input matrix.

### B (in)

B is COMPLEX The ( 1, 2 ) element of input matrix. The ( 2, 1 ) element is also given by B, since the 2-by-2 matrix is symmetric.

### C (in)

C is COMPLEX The ( 2, 2 ) element of input matrix.

### RT1 (out)

RT1 is COMPLEX The eigenvalue of larger modulus.

### RT2 (out)

RT2 is COMPLEX The eigenvalue of smaller modulus.

### EVSCAL (out)

EVSCAL is COMPLEX The complex value by which the eigenvector matrix was scaled to make it orthonormal. If EVSCAL is zero, the eigenvectors were not computed. This means one of two things: the 2-by-2 matrix could not be diagonalized, or the norm of the matrix of eigenvectors before scaling was larger than the threshold value THRESH (set below).

### CS1 (out)

CS1 is COMPLEX

### SN1 (out)

SN1 is COMPLEX If EVSCAL .NE. 0, ( CS1, SN1 ) is the unit right eigenvector for RT1.

