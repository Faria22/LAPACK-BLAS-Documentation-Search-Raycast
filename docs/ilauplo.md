# ILAUPLO

## Function Signature

```fortran
ILAUPLO(UPLO)
```

## Description


 This subroutine translated from a character string specifying a
 upper- or lower-triangular matrix to the relevant BLAST-specified
 integer constant.

 ILAUPLO returns an INTEGER.  If ILAUPLO < 0, then the input is not
 a character indicating an upper- or lower-triangular matrix.
 Otherwise ILAUPLO returns the constant value corresponding to UPLO.

