# SLASD4

## Function Signature

```fortran
SLASD4(N, I, D, Z, DELTA, RHO, SIGMA, WORK, INFO)
```

## Description


 This subroutine computes the square root of the I-th updated
 eigenvalue of a positive symmetric rank-one modification to
 a positive diagonal matrix whose entries are given as the squares
 of the corresponding entries in the array d, and that

        0 <= D(i) < D(j)  for  i < j

 and that RHO > 0. This is arranged by the calling routine, and is
 no loss in generality.  The rank-one modified system is thus

        diag( D ) * diag( D ) +  RHO * Z * Z_transpose.

 where we assume the Euclidean norm of Z is 1.

 The method consists of approximating the rational functions in the
 secular equation by simpler interpolating rational functions.

## Parameters

### N (in)

N is INTEGER The length of all arrays.

### I (in)

I is INTEGER The index of the eigenvalue to be computed. 1 <= I <= N.

### D (in)

D is REAL array, dimension ( N ) The original eigenvalues. It is assumed that they are in order, 0 <= D(I) < D(J) for I < J.

### Z (in)

Z is REAL array, dimension ( N ) The components of the updating vector.

### DELTA (out)

DELTA is REAL array, dimension ( N ) If N .ne. 1, DELTA contains (D(j) - sigma_I) in its j-th component. If N = 1, then DELTA(1) = 1. The vector DELTA contains the information necessary to construct the (singular) eigenvectors.

### RHO (in)

RHO is REAL The scalar in the symmetric updating formula.

### SIGMA (out)

SIGMA is REAL The computed sigma_I, the I-th updated eigenvalue.

### WORK (out)

WORK is REAL array, dimension ( N ) If N .ne. 1, WORK contains (D(j) + sigma_I) in its j-th component. If N = 1, then WORK( 1 ) = 1.

### INFO (out)

INFO is INTEGER = 0: successful exit > 0: if INFO = 1, the updating process failed.

