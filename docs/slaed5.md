# SLAED5

## Function Signature

```fortran
SLAED5(I, D, Z, DELTA, RHO, DLAM)
```

## Description


 This subroutine computes the I-th eigenvalue of a symmetric rank-one
 modification of a 2-by-2 diagonal matrix

            diag( D )  +  RHO * Z * transpose(Z) .

 The diagonal elements in the array D are assumed to satisfy

            D(i) < D(j)  for  i < j .

 We also assume RHO > 0 and that the Euclidean norm of the vector
 Z is one.

## Parameters

### I (in)

I is INTEGER The index of the eigenvalue to be computed. I = 1 or I = 2.

### D (in)

D is REAL array, dimension (2) The original eigenvalues. We assume D(1) < D(2).

### Z (in)

Z is REAL array, dimension (2) The components of the updating vector.

### DELTA (out)

DELTA is REAL array, dimension (2) The vector DELTA contains the information necessary to construct the eigenvectors.

### RHO (in)

RHO is REAL The scalar in the symmetric updating formula.

### DLAM (out)

DLAM is REAL The computed lambda_I, the I-th updated eigenvalue.

