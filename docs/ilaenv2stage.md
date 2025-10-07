# ILAENV2STAGE

## Function Signature

```fortran
ILAENV2STAGE(ISPEC, NAME, OPTS, N1, N2, N3, N4)
```

## Description


 ILAENV2STAGE is called from the LAPACK routines to choose problem-dependent
 parameters for the local environment.  See ISPEC for a description of
 the parameters.
 It sets problem and machine dependent parameters useful for *_2STAGE and
 related subroutines.

 ILAENV2STAGE returns an INTEGER
 if ILAENV2STAGE >= 0: ILAENV2STAGE returns the value of the parameter
                       specified by ISPEC
 if ILAENV2STAGE < 0:  if ILAENV2STAGE = -k, the k-th argument had an
                       illegal value.

 This version provides a set of parameters which should give good,
 but not optimal, performance on many of the currently available
 computers for the 2-stage solvers. Users are encouraged to modify this
 subroutine to set the tuning parameters for their particular machine using
 the option and problem size information in the arguments.

 This routine will not function correctly if it is converted to all
 lower case.  Converting it to all upper case is allowed.

## Parameters

### ISPEC (in)

ISPEC is INTEGER Specifies the parameter to be returned as the value of ILAENV2STAGE. = 1: the optimal blocksize nb for the reduction to BAND = 2: the optimal blocksize ib for the eigenvectors singular vectors update routine = 3: The length of the array that store the Housholder representation for the second stage Band to Tridiagonal or Bidiagonal = 4: The workspace needed for the routine in input. = 5: For future release.

### NAME (in)

NAME is CHARACTER*(*) The name of the calling subroutine, in either upper case or lower case.

### OPTS (in)

OPTS is CHARACTER*(*) The character options to the subroutine NAME, concatenated into a single character string. For example, UPLO = 'U', TRANS = 'T', and DIAG = 'N' for a triangular routine would be specified as OPTS = 'UTN'.

### N1 (in)

N1 is INTEGER

### N2 (in)

N2 is INTEGER

### N3 (in)

N3 is INTEGER

### N4 (in)

N4 is INTEGER Problem dimensions for the subroutine NAME; these may not all be required.

