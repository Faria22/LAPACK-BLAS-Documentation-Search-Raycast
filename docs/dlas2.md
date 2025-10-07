# DLAS2

## Function Signature

```fortran
DLAS2(F, G, H, SSMIN, SSMAX)
```

## Description


 DLAS2  computes the singular values of the 2-by-2 matrix
    [  F   G  ]
    [  0   H  ].
 On return, SSMIN is the smaller singular value and SSMAX is the
 larger singular value.

## Parameters

### F (in)

F is DOUBLE PRECISION The (1,1) element of the 2-by-2 matrix.

### G (in)

G is DOUBLE PRECISION The (1,2) element of the 2-by-2 matrix.

### H (in)

H is DOUBLE PRECISION The (2,2) element of the 2-by-2 matrix.

### SSMIN (out)

SSMIN is DOUBLE PRECISION The smaller singular value.

### SSMAX (out)

SSMAX is DOUBLE PRECISION The larger singular value.

