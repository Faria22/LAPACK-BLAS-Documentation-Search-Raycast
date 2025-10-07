```fortran
subroutine slanv2 (
		real a,
		real b,
		real c,
		real d,
		real rt1r,
		real rt1i,
		real rt2r,
		real rt2i,
		real cs,
		real sn
)
```

 SLANV2 computes the Schur factorization of a real 2-by-2 nonsymmetric
 matrix in standard form:

      [ A  B ] = [ CS -SN ] [ AA  BB ] [ CS  SN ]
      [ C  D ]   [ SN  CS ] [ CC  DD ] [-SN  CS ]

 where either
 1) CC = 0 so that AA and DD are real eigenvalues of the matrix, or
 2) AA = DD and BB*CC < 0, so that AA + or - sqrt(BB*CC) are complex
 conjugate eigenvalues.

## Parameters
A : Real [in,out]

B : Real [in,out]

C : Real [in,out]

D : Real [in,out]
> On entry, the elements of the input matrix.
> On exit, they are overwritten by the elements of the
> standardised Schur form.

Rt1r : Real [out]

Rt1i : Real [out]

Rt2r : Real [out]

Rt2i : Real [out]
> The real and imaginary parts of the eigenvalues. If the
> eigenvalues are a complex conjugate pair, RT1I > 0.

Cs : Real [out]

Sn : Real [out]
> Parameters of the rotation matrix.

