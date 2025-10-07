# DLASQ3

## Function Signature

```fortran
DLASQ3(I0, N0, Z, PP, DMIN, SIGMA, DESIG, QMAX, NFAIL,
*                          ITER, NDIV, IEEE, TTYPE, DMIN1, DMIN2, DN, DN1,
*                          DN2, G, TAU)
```

## Description


 DLASQ3 checks for deflation, computes a shift (TAU) and calls dqds.
 In case of failure it changes shifts, and tries again until output
 is positive.

## Parameters

### I0 (in)

I0 is INTEGER First index.

### N0 (in,out)

N0 is INTEGER Last index.

### Z (in,out)

Z is DOUBLE PRECISION array, dimension ( 4*N0 ) Z holds the qd array.

### PP (in,out)

PP is INTEGER PP=0 for ping, PP=1 for pong. PP=2 indicates that flipping was applied to the Z array and that the initial tests for deflation should not be performed.

### DMIN (out)

DMIN is DOUBLE PRECISION Minimum value of d.

### SIGMA (out)

SIGMA is DOUBLE PRECISION Sum of shifts used in current segment.

### DESIG (in,out)

DESIG is DOUBLE PRECISION Lower order part of SIGMA

### QMAX (in)

QMAX is DOUBLE PRECISION Maximum value of q.

### NFAIL (in,out)

NFAIL is INTEGER Increment NFAIL by 1 each time the shift was too big.

### ITER (in,out)

ITER is INTEGER Increment ITER by 1 for each iteration.

### NDIV (in,out)

NDIV is INTEGER Increment NDIV by 1 for each division.

### IEEE (in)

IEEE is LOGICAL Flag for IEEE or non IEEE arithmetic (passed to DLASQ5).

### TTYPE (in,out)

TTYPE is INTEGER Shift type.

### DMIN1 (in,out)

DMIN1 is DOUBLE PRECISION

### DMIN2 (in,out)

DMIN2 is DOUBLE PRECISION

### DN (in,out)

DN is DOUBLE PRECISION

### DN1 (in,out)

DN1 is DOUBLE PRECISION

### DN2 (in,out)

DN2 is DOUBLE PRECISION

### G (in,out)

G is DOUBLE PRECISION

### TAU (in,out)

TAU is DOUBLE PRECISION These are passed as arguments in order to save their values between calls to DLASQ3.

