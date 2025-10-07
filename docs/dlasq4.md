# DLASQ4

## Function Signature

```fortran
DLASQ4(I0, N0, Z, PP, N0IN, DMIN, DMIN1, DMIN2, DN,
*                          DN1, DN2, TAU, TTYPE, G)
```

## Description


 DLASQ4 computes an approximation TAU to the smallest eigenvalue
 using values of d from the previous transform.

## Parameters

### I0 (in)

I0 is INTEGER First index.

### N0 (in)

N0 is INTEGER Last index.

### Z (in)

Z is DOUBLE PRECISION array, dimension ( 4*N0 ) Z holds the qd array.

### PP (in)

PP is INTEGER PP=0 for ping, PP=1 for pong.

### N0IN (in)

N0IN is INTEGER The value of N0 at start of EIGTEST.

### DMIN (in)

DMIN is DOUBLE PRECISION Minimum value of d.

### DMIN1 (in)

DMIN1 is DOUBLE PRECISION Minimum value of d, excluding D( N0 ).

### DMIN2 (in)

DMIN2 is DOUBLE PRECISION Minimum value of d, excluding D( N0 ) and D( N0-1 ).

### DN (in)

DN is DOUBLE PRECISION d(N)

### DN1 (in)

DN1 is DOUBLE PRECISION d(N-1)

### DN2 (in)

DN2 is DOUBLE PRECISION d(N-2)

### TAU (out)

TAU is DOUBLE PRECISION This is the shift.

### TTYPE (out)

TTYPE is INTEGER Shift type.

### G (in,out)

G is DOUBLE PRECISION G is passed as an argument in order to save its value between calls to DLASQ4.

