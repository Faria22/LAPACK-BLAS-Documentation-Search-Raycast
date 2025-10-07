# SLASQ4

## Function Signature

```fortran
SLASQ4(I0, N0, Z, PP, N0IN, DMIN, DMIN1, DMIN2, DN,
*                          DN1, DN2, TAU, TTYPE, G)
```

## Description


 SLASQ4 computes an approximation TAU to the smallest eigenvalue
 using values of d from the previous transform.

## Parameters

### I0 (in)

I0 is INTEGER First index.

### N0 (in)

N0 is INTEGER Last index.

### Z (in)

Z is REAL array, dimension ( 4*N0 ) Z holds the qd array.

### PP (in)

PP is INTEGER PP=0 for ping, PP=1 for pong.

### N0IN (in)

N0IN is INTEGER The value of N0 at start of EIGTEST.

### DMIN (in)

DMIN is REAL Minimum value of d.

### DMIN1 (in)

DMIN1 is REAL Minimum value of d, excluding D( N0 ).

### DMIN2 (in)

DMIN2 is REAL Minimum value of d, excluding D( N0 ) and D( N0-1 ).

### DN (in)

DN is REAL d(N)

### DN1 (in)

DN1 is REAL d(N-1)

### DN2 (in)

DN2 is REAL d(N-2)

### TAU (out)

TAU is REAL This is the shift.

### TTYPE (out)

TTYPE is INTEGER Shift type.

### G (in,out)

G is REAL G is passed as an argument in order to save its value between calls to SLASQ4.

