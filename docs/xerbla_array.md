# XERBLA_ARRAY

## Function Signature

```fortran
XERBLA_ARRAY(SRNAME_ARRAY, SRNAME_LEN, INFO)
```

## Description


 XERBLA_ARRAY assists other languages in calling XERBLA, the LAPACK
 and BLAS error handler.  Rather than taking a Fortran string argument
 as the function's name, XERBLA_ARRAY takes an array of single
 characters along with the array's length.  XERBLA_ARRAY then copies
 up to 32 characters of that array into a Fortran string and passes
 that to XERBLA.  If called with a non-positive SRNAME_LEN,
 XERBLA_ARRAY will call XERBLA with a string of all blank characters.

 Say some macro or other device makes XERBLA_ARRAY available to C99
 by a name lapack_xerbla and with a common Fortran calling convention.
 Then a C99 program could invoke XERBLA via:
    {
      int flen = strlen(__func__);
      lapack_xerbla(__func__, &flen, &info);
    }

 Providing XERBLA_ARRAY is not necessary for intercepting LAPACK
 errors.  XERBLA_ARRAY calls XERBLA.

## Parameters

### SRNAME_ARRAY (in)

SRNAME_ARRAY is CHARACTER(1) array, dimension (SRNAME_LEN) The name of the routine which called XERBLA_ARRAY.

### SRNAME_LEN (in)

SRNAME_LEN is INTEGER The length of the name in SRNAME_ARRAY.

### INFO (in)

INFO is INTEGER The position of the invalid parameter in the parameter list of the calling routine.

