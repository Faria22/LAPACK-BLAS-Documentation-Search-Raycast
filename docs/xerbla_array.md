```fortran
subroutine xerbla_array	(	srname_array,
		integer	srname_len,
		integer	info )
```

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
Srname_array : Character(1) Array, Dimension (srname_len) [in]
> The name of the routine which called XERBLA_ARRAY.

Srname_len : Integer [in]
> The length of the name in SRNAME_ARRAY.

Info : Integer [in]
> The position of the invalid parameter in the parameter list
> of the calling routine.

