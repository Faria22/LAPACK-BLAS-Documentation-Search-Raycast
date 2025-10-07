# DLARTGS

## Function Signature

```fortran
DLARTGS(X, Y, SIGMA, CS, SN)
```

## Description


 DLARTGS generates a plane rotation designed to introduce a bulge in
 Golub-Reinsch-style implicit QR iteration for the bidiagonal SVD
 problem. X and Y are the top-row entries, and SIGMA is the shift.
 The computed CS and SN define a plane rotation satisfying

    [  CS  SN  ]  .  [ X^2 - SIGMA ]  =  [ R ],
    [ -SN  CS  ]     [    X * Y    ]     [ 0 ]

 with R nonnegative.  If X^2 - SIGMA and X * Y are 0, then the
 rotation is by PI/2.

## Parameters

### X (in)

X is DOUBLE PRECISION The (1,1) entry of an upper bidiagonal matrix.

### Y (in)

Y is DOUBLE PRECISION The (1,2) entry of an upper bidiagonal matrix.

### SIGMA (in)

SIGMA is DOUBLE PRECISION The shift.

### CS (out)

CS is DOUBLE PRECISION The cosine of the rotation.

### SN (out)

SN is DOUBLE PRECISION The sine of the rotation.

