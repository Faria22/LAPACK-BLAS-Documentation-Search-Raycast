# IEEECK

## Function Signature

```fortran
IEEECK(ISPEC, ZERO, ONE)
```

## Description


 IEEECK is called from the ILAENV to verify that Infinity and
 possibly NaN arithmetic is safe (i.e. will not trap).

## Parameters

### ISPEC (in)

ISPEC is INTEGER Specifies whether to test just for infinity arithmetic or whether to test for infinity and NaN arithmetic. = 0: Verify infinity arithmetic only. = 1: Verify infinity and NaN arithmetic.

### ZERO (in)

ZERO is REAL Must contain the value 0.0 This is passed to prevent the compiler from optimizing away this code.

### ONE (in)

ONE is REAL Must contain the value 1.0 This is passed to prevent the compiler from optimizing away this code. RETURN VALUE: INTEGER = 0: Arithmetic failed to produce the correct answers = 1: Arithmetic produced the correct answers

