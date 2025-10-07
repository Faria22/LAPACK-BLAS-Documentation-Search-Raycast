# ILADIAG

## Function Signature

```fortran
ILADIAG(DIAG)
```

## Description


 This subroutine translated from a character string specifying if a
 matrix has unit diagonal or not to the relevant BLAST-specified
 integer constant.

 ILADIAG returns an INTEGER.  If ILADIAG < 0, then the input is not a
 character indicating a unit or non-unit diagonal.  Otherwise ILADIAG
 returns the constant value corresponding to DIAG.

