# IPARMQ

## Function Signature

```fortran
IPARMQ(ISPEC, NAME, OPTS, N, ILO, IHI, LWORK)
```

## Description


      This program sets problem and machine dependent parameters
      useful for xHSEQR and related subroutines for eigenvalue
      problems. It is called whenever
      IPARMQ is called with 12 <= ISPEC <= 16

## Parameters

### ISPEC (in)

ISPEC is INTEGER ISPEC specifies which tunable parameter IPARMQ should return. ISPEC=12: (INMIN) Matrices of order nmin or less are sent directly to xLAHQR, the implicit double shift QR algorithm. NMIN must be at least 11. ISPEC=13: (INWIN) Size of the deflation window. This is best set greater than or equal to the number of simultaneous shifts NS. Larger matrices benefit from larger deflation windows. ISPEC=14: (INIBL) Determines when to stop nibbling and invest in an (expensive) multi-shift QR sweep. If the aggressive early deflation subroutine finds LD converged eigenvalues from an order NW deflation window and LD > (NW*NIBBLE)/100, then the next QR sweep is skipped and early deflation is applied immediately to the remaining active diagonal block. Setting IPARMQ(ISPEC=14) = 0 causes TTQRE to skip a multi-shift QR sweep whenever early deflation finds a converged eigenvalue. Setting IPARMQ(ISPEC=14) greater than or equal to 100 prevents TTQRE from skipping a multi-shift QR sweep. ISPEC=15: (NSHFTS) The number of simultaneous shifts in a multi-shift QR iteration. ISPEC=16: (IACC22) IPARMQ is set to 0, 1 or 2 with the following meanings. 0: During the multi-shift QR/QZ sweep, blocked eigenvalue reordering, blocked Hessenberg-triangular reduction, reflections and/or rotations are not accumulated when updating the far-from-diagonal matrix entries. 1: During the multi-shift QR/QZ sweep, blocked eigenvalue reordering, blocked Hessenberg-triangular reduction, reflections and/or rotations are accumulated, and matrix-matrix multiplication is used to update the far-from-diagonal matrix entries. 2: During the multi-shift QR/QZ sweep, blocked eigenvalue reordering, blocked Hessenberg-triangular reduction, reflections and/or rotations are accumulated, and 2-by-2 block structure is exploited during matrix-matrix multiplies. (If xTRMM is slower than xGEMM, then IPARMQ(ISPEC=16)=1 may be more efficient than IPARMQ(ISPEC=16)=2 despite the greater level of arithmetic work implied by the latter choice.) ISPEC=17: (ICOST) An estimate of the relative cost of flops within the near-the-diagonal shift chase compared to flops within the BLAS calls of a QZ sweep.

### NAME (in)

NAME is CHARACTER string Name of the calling subroutine

### OPTS (in)

OPTS is CHARACTER string This is a concatenation of the string arguments to TTQRE.

### N (in)

N is INTEGER N is the order of the Hessenberg matrix H.

### ILO (in)

ILO is INTEGER

### IHI (in)

IHI is INTEGER It is assumed that H is already upper triangular in rows and columns 1:ILO-1 and IHI+1:N.

### LWORK (in)

LWORK is INTEGER The amount of workspace available.

