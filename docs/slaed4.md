# SLAED4

## Function Signature

```fortran
SLAED4(N, I, D, Z, DELTA, RHO, DLAM, INFO)
```

## Description


 This subroutine computes the I-th updated eigenvalue of a symmetric
 rank-one modification to a diagonal matrix whose elements are
 given in the array d, and that

            D(i) < D(j)  for  i < j

 and that RHO > 0.  This is arranged by the calling routine, and is
 no loss in generality.  The rank-one modified system is thus

            diag( D )  +  RHO * Z * Z_transpose.

 where we assume the Euclidean norm of Z is 1.

 The method consists of approximating the rational functions in the
 secular equation by simpler interpolating rational functions.

## Parameters

### N (in)

N is INTEGER The length of all arrays.

### I (in)

I is INTEGER The index of the eigenvalue to be computed. 1 <= I <= N.

### D (in)

D is REAL array, dimension (N) The original eigenvalues. It is assumed that they are in order, D(I) < D(J) for I < J.

### Z (in)

Z is REAL array, dimension (N) The components of the updating vector.

### DELTA (out)

DELTA is REAL array, dimension (N) If N > 2, DELTA contains (D(j) - lambda_I) in its j-th component. If N = 1, then DELTA(1) = 1. If N = 2, see SLAED5 for detail. The vector DELTA contains the information necessary to construct the eigenvectors by SLAED3 and SLAED9.

### RHO (in)

RHO is REAL The scalar in the symmetric updating formula.

### DLAM (out)

DLAM is REAL The computed lambda_I, the I-th updated eigenvalue.

### INFO (out)

INFO is INTEGER = 0: successful exit > 0: if INFO = 1, the updating process failed.

