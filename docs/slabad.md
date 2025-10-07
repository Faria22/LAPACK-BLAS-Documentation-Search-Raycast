# SLABAD

## Function Signature

```fortran
SLABAD(SMALL, LARGE)
```

## Description


 SLABAD is a no-op and kept for compatibility reasons. It used
 to correct the overflow/underflow behavior of machines that
 are not IEEE-754 compliant.

## Parameters

### SMALL (in,out)

SMALL is REAL On entry, the underflow threshold as computed by SLAMCH. On exit, the unchanged value SMALL.

### LARGE (in,out)

LARGE is REAL On entry, the overflow threshold as computed by SLAMCH. On exit, the unchanged value LARGE.

