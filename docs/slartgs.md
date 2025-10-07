# SLARTGS

## Function Signature

```fortran
SLARTGS(X, Y, SIGMA, CS, SN)
```

## Description


 SLARTGS generates a plane rotation designed to introduce a bulge in
 Golub-Reinsch-style implicit QR iteration for the bidiagonal SVD
 problem. X and Y are the top-row entries, and SIGMA is the shift.
 The computed CS and SN define a plane rotation satisfying

    [  CS  SN  ]  .  [ X^2 - SIGMA ]  =  [ R ],
    [ -SN  CS  ]     [    X * Y    ]     [ 0 ]

 with R nonnegative.  If X^2 - SIGMA and X * Y are 0, then the
 rotation is by PI/2.

## Parameters

### X (in)

X is REAL The (1,1) entry of an upper bidiagonal matrix.

### Y (in)

Y is REAL The (1,2) entry of an upper bidiagonal matrix.

### SIGMA (in)

SIGMA is REAL The shift.

### CS (out)

CS is REAL The cosine of the rotation.

### SN (out)

SN is REAL The sine of the rotation.

