# SLASV2

## Function Signature

```fortran
SLASV2(F, G, H, SSMIN, SSMAX, SNR, CSR, SNL, CSL)
```

## Description


 SLASV2 computes the singular value decomposition of a 2-by-2
 triangular matrix
    [  F   G  ]
    [  0   H  ].
 On return, abs(SSMAX) is the larger singular value, abs(SSMIN) is the
 smaller singular value, and (CSL,SNL) and (CSR,SNR) are the left and
 right singular vectors for abs(SSMAX), giving the decomposition

    [ CSL  SNL ] [  F   G  ] [ CSR -SNR ]  =  [ SSMAX   0   ]
    [-SNL  CSL ] [  0   H  ] [ SNR  CSR ]     [  0    SSMIN ].

## Parameters

### F (in)

F is REAL The (1,1) element of the 2-by-2 matrix.

### G (in)

G is REAL The (1,2) element of the 2-by-2 matrix.

### H (in)

H is REAL The (2,2) element of the 2-by-2 matrix.

### SSMIN (out)

SSMIN is REAL abs(SSMIN) is the smaller singular value.

### SSMAX (out)

SSMAX is REAL abs(SSMAX) is the larger singular value.

### SNL (out)

SNL is REAL

### CSL (out)

CSL is REAL The vector (CSL, SNL) is a unit left singular vector for the singular value abs(SSMAX).

### SNR (out)

SNR is REAL

### CSR (out)

CSR is REAL The vector (CSR, SNR) is a unit right singular vector for the singular value abs(SSMAX).

