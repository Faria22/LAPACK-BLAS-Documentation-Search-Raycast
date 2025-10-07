# SLASQ3

## Function Signature

```fortran
SLASQ3(I0, N0, Z, PP, DMIN, SIGMA, DESIG, QMAX, NFAIL,
*                          ITER, NDIV, IEEE, TTYPE, DMIN1, DMIN2, DN, DN1,
*                          DN2, G, TAU)
```

## Description


 SLASQ3 checks for deflation, computes a shift (TAU) and calls dqds.
 In case of failure it changes shifts, and tries again until output
 is positive.

## Parameters

### I0 (in)

I0 is INTEGER First index.

### N0 (in,out)

N0 is INTEGER Last index.

### Z (in,out)

Z is REAL array, dimension ( 4*N0 ) Z holds the qd array.

### PP (in,out)

PP is INTEGER PP=0 for ping, PP=1 for pong. PP=2 indicates that flipping was applied to the Z array and that the initial tests for deflation should not be performed.

### DMIN (out)

DMIN is REAL Minimum value of d.

### SIGMA (out)

SIGMA is REAL Sum of shifts used in current segment.

### DESIG (in,out)

DESIG is REAL Lower order part of SIGMA

### QMAX (in)

QMAX is REAL Maximum value of q.

### NFAIL (in,out)

NFAIL is INTEGER Increment NFAIL by 1 each time the shift was too big.

### ITER (in,out)

ITER is INTEGER Increment ITER by 1 for each iteration.

### NDIV (in,out)

NDIV is INTEGER Increment NDIV by 1 for each division.

### IEEE (in)

IEEE is LOGICAL Flag for IEEE or non IEEE arithmetic (passed to SLASQ5).

### TTYPE (in,out)

TTYPE is INTEGER Shift type.

### DMIN1 (in,out)

DMIN1 is REAL

### DMIN2 (in,out)

DMIN2 is REAL

### DN (in,out)

DN is REAL

### DN1 (in,out)

DN1 is REAL

### DN2 (in,out)

DN2 is REAL

### G (in,out)

G is REAL

### TAU (in,out)

TAU is REAL These are passed as arguments in order to save their values between calls to SLASQ3.

