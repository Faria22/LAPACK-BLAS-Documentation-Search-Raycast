# DLABAD

## Function Signature

```fortran
DLABAD(SMALL, LARGE)
```

## Description


 DLABAD is a no-op and kept for compatibility reasons. It used
 to correct the overflow/underflow behavior of machines that
 are not IEEE-754 compliant.


## Parameters

### SMALL (in,out)

SMALL is DOUBLE PRECISION On entry, the underflow threshold as computed by DLAMCH. On exit, the unchanged value SMALL.

### LARGE (in,out)

LARGE is DOUBLE PRECISION On entry, the overflow threshold as computed by DLAMCH. On exit, the unchanged value LARGE.

