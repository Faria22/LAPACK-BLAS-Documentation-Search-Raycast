# ILATRANS

## Function Signature

```fortran
ILATRANS(TRANS)
```

## Description


 This subroutine translates from a character string specifying a
 transposition operation to the relevant BLAST-specified integer
 constant.

 ILATRANS returns an INTEGER.  If ILATRANS < 0, then the input is not
 a character indicating a transposition operator.  Otherwise ILATRANS
 returns the constant value corresponding to TRANS.

