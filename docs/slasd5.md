# SLASD5

## Function Signature

```fortran
SLASD5(I, D, Z, DELTA, RHO, DSIGMA, WORK)
```

## Description


 This subroutine computes the square root of the I-th eigenvalue
 of a positive symmetric rank-one modification of a 2-by-2 diagonal
 matrix

            diag( D ) * diag( D ) +  RHO * Z * transpose(Z) .

 The diagonal entries in the array D are assumed to satisfy

            0 <= D(i) < D(j)  for  i < j .

 We also assume RHO > 0 and that the Euclidean norm of the vector
 Z is one.

## Parameters

### I (in)

I is INTEGER The index of the eigenvalue to be computed. I = 1 or I = 2.

### D (in)

D is REAL array, dimension (2) The original eigenvalues. We assume 0 <= D(1) < D(2).

### Z (in)

Z is REAL array, dimension (2) The components of the updating vector.

### DELTA (out)

DELTA is REAL array, dimension (2) Contains (D(j) - sigma_I) in its j-th component. The vector DELTA contains the information necessary to construct the eigenvectors.

### RHO (in)

RHO is REAL The scalar in the symmetric updating formula.

### DSIGMA (out)

DSIGMA is REAL The computed sigma_I, the I-th updated eigenvalue.

### WORK (out)

WORK is REAL array, dimension (2) WORK contains (D(j) + sigma_I) in its j-th component.

