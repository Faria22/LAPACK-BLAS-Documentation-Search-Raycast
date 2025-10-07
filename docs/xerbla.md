# XERBLA

## Function Signature

```fortran
XERBLA(SRNAME, INFO)
```

## Description


 XERBLA  is an error handler for the LAPACK routines.
 It is called by an LAPACK routine if an input parameter has an
 invalid value.  A message is printed and execution stops.

 Installers may consider modifying the STOP statement in order to
 call system-specific exception-handling facilities.

## Parameters

### SRNAME (in)

SRNAME is CHARACTER*(*) The name of the routine which called XERBLA.

### INFO (in)

INFO is INTEGER The position of the invalid parameter in the parameter list of the calling routine.

