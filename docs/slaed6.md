# SLAED6

## Function Signature

```fortran
SLAED6(KNITER, ORGATI, RHO, D, Z, FINIT, TAU, INFO)
```

## Description


 SLAED6 computes the positive or negative root (closest to the origin)
 of
                  z(1)        z(2)        z(3)
 f(x) =   rho + --------- + ---------- + ---------
                 d(1)-x      d(2)-x      d(3)-x

 It is assumed that

       if ORGATI = .true. the root is between d(2) and d(3);
       otherwise it is between d(1) and d(2)

 This routine will be called by SLAED4 when necessary. In most cases,
 the root sought is the smallest in magnitude, though it might not be
 in some extremely rare situations.

## Parameters

### KNITER (in)

KNITER is INTEGER Refer to SLAED4 for its significance.

### ORGATI (in)

ORGATI is LOGICAL If ORGATI is true, the needed root is between d(2) and d(3); otherwise it is between d(1) and d(2). See SLAED4 for further details.

### RHO (in)

RHO is REAL Refer to the equation f(x) above.

### D (in)

D is REAL array, dimension (3) D satisfies d(1) < d(2) < d(3).

### Z (in)

Z is REAL array, dimension (3) Each of the elements in z must be positive.

### FINIT (in)

FINIT is REAL The value of f at 0. It is more accurate than the one evaluated inside this routine (if someone wants to do so).

### TAU (out)

TAU is REAL The root of the equation f(x).

### INFO (out)

INFO is INTEGER = 0: successful exit > 0: if INFO = 1, failure to converge

