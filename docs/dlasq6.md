# DLASQ6

## Function Signature

```fortran
DLASQ6(I0, N0, Z, PP, DMIN, DMIN1, DMIN2, DN,
*                          DNM1, DNM2)
```

## Description


 DLASQ6 computes one dqd (shift equal to zero) transform in
 ping-pong form, with protection against underflow and overflow.

## Parameters

### I0 (in)

I0 is INTEGER First index.

### N0 (in)

N0 is INTEGER Last index.

### Z (in)

Z is DOUBLE PRECISION array, dimension ( 4*N ) Z holds the qd array. EMIN is stored in Z(4*N0) to avoid an extra argument.

### PP (in)

PP is INTEGER PP=0 for ping, PP=1 for pong.

### DMIN (out)

DMIN is DOUBLE PRECISION Minimum value of d.

### DMIN1 (out)

DMIN1 is DOUBLE PRECISION Minimum value of d, excluding D( N0 ).

### DMIN2 (out)

DMIN2 is DOUBLE PRECISION Minimum value of d, excluding D( N0 ) and D( N0-1 ).

### DN (out)

DN is DOUBLE PRECISION d(N0), the last value of d.

### DNM1 (out)

DNM1 is DOUBLE PRECISION d(N0-1).

### DNM2 (out)

DNM2 is DOUBLE PRECISION d(N0-2).

