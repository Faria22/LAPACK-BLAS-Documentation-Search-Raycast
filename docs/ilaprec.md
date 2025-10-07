# ILAPREC

## Function Signature

```fortran
ILAPREC(PREC)
```

## Description


 This subroutine translated from a character string specifying an
 intermediate precision to the relevant BLAST-specified integer
 constant.

 ILAPREC returns an INTEGER.  If ILAPREC < 0, then the input is not a
 character indicating a supported intermediate precision.  Otherwise
 ILAPREC returns the constant value corresponding to PREC.

