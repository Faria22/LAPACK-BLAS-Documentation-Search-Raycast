# SLAS2

## Function Signature

```fortran
SLAS2(F, G, H, SSMIN, SSMAX)
```

## Description


 SLAS2  computes the singular values of the 2-by-2 matrix
    [  F   G  ]
    [  0   H  ].
 On return, SSMIN is the smaller singular value and SSMAX is the
 larger singular value.

## Parameters

### F (in)

F is REAL The (1,1) element of the 2-by-2 matrix.

### G (in)

G is REAL The (1,2) element of the 2-by-2 matrix.

### H (in)

H is REAL The (2,2) element of the 2-by-2 matrix.

### SSMIN (out)

SSMIN is REAL The smaller singular value.

### SSMAX (out)

SSMAX is REAL The larger singular value.

