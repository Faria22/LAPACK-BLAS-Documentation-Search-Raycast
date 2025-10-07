# SLASQ5

SLASQ5 computes one dqds transform in ping-pong form. Used by sbdsqr and sstegr.

## Function Signature

```fortran
SLASQ5(I0, N0, Z, PP, TAU, SIGMA, DMIN, DMIN1, DMIN2, DN,
*                          DNM1, DNM2, IEEE, EPS)
```

## Description


 SLASQ5 computes one dqds transform in ping-pong form, one
 version for IEEE machines another for non IEEE machines.

## Parameters

### I0 (in)

I0 is INTEGER First index.

### N0 (in)

N0 is INTEGER Last index.

### Z (in)

Z is REAL array, dimension ( 4*N ) Z holds the qd array. EMIN is stored in Z(4*N0) to avoid an extra argument.

### PP (in)

PP is INTEGER PP=0 for ping, PP=1 for pong.

### TAU (in)

TAU is REAL This is the shift.

### SIGMA (in)

SIGMA is REAL This is the accumulated shift up to this step.

### DMIN (out)

DMIN is REAL Minimum value of d.

### DMIN1 (out)

DMIN1 is REAL Minimum value of d, excluding D( N0 ).

### DMIN2 (out)

DMIN2 is REAL Minimum value of d, excluding D( N0 ) and D( N0-1 ).

### DN (out)

DN is REAL d(N0), the last value of d.

### DNM1 (out)

DNM1 is REAL d(N0-1).

### DNM2 (out)

DNM2 is REAL d(N0-2).

### IEEE (in)

IEEE is LOGICAL Flag for IEEE or non IEEE arithmetic.

### EPS (in)

EPS is REAL This is the value of epsilon used.

