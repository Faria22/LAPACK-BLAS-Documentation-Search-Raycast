# DLANV2

## Function Signature

```fortran
DLANV2(A, B, C, D, RT1R, RT1I, RT2R, RT2I, CS, SN)
```

## Description


 DLANV2 computes the Schur factorization of a real 2-by-2 nonsymmetric
 matrix in standard form:

      [ A  B ] = [ CS -SN ] [ AA  BB ] [ CS  SN ]
      [ C  D ]   [ SN  CS ] [ CC  DD ] [-SN  CS ]

 where either
 1) CC = 0 so that AA and DD are real eigenvalues of the matrix, or
 2) AA = DD and BB*CC < 0, so that AA + or - sqrt(BB*CC) are complex
 conjugate eigenvalues.

## Parameters

### A (in,out)

A is DOUBLE PRECISION

### B (in,out)

B is DOUBLE PRECISION

### C (in,out)

C is DOUBLE PRECISION

### D (in,out)

D is DOUBLE PRECISION On entry, the elements of the input matrix. On exit, they are overwritten by the elements of the standardised Schur form.

### RT1R (out)

RT1R is DOUBLE PRECISION

### RT1I (out)

RT1I is DOUBLE PRECISION

### RT2R (out)

RT2R is DOUBLE PRECISION

### RT2I (out)

RT2I is DOUBLE PRECISION The real and imaginary parts of the eigenvalues. If the eigenvalues are a complex conjugate pair, RT1I > 0.

### CS (out)

CS is DOUBLE PRECISION

### SN (out)

SN is DOUBLE PRECISION Parameters of the rotation matrix.

