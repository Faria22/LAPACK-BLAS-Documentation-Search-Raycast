# DLAQR5

## Function Signature

```fortran
DLAQR5(WANTT, WANTZ, KACC22, N, KTOP, KBOT, NSHFTS,
*                          SR, SI, H, LDH, ILOZ, IHIZ, Z, LDZ, V, LDV, U,
*                          LDU, NV, WV, LDWV, NH, WH, LDWH)
```

## Description


    DLAQR5, called by DLAQR0, performs a
    single small-bulge multi-shift QR sweep.

## Parameters

### WANTT (in)

WANTT is LOGICAL WANTT = .true. if the quasi-triangular Schur factor is being computed. WANTT is set to .false. otherwise.

### WANTZ (in)

WANTZ is LOGICAL WANTZ = .true. if the orthogonal Schur factor is being computed. WANTZ is set to .false. otherwise.

### KACC22 (in)

KACC22 is INTEGER with value 0, 1, or 2. Specifies the computation mode of far-from-diagonal orthogonal updates. = 0: DLAQR5 does not accumulate reflections and does not use matrix-matrix multiply to update far-from-diagonal matrix entries. = 1: DLAQR5 accumulates reflections and uses matrix-matrix multiply to update the far-from-diagonal matrix entries. = 2: Same as KACC22 = 1. This option used to enable exploiting the 2-by-2 structure during matrix multiplications, but this is no longer supported.

### N (in)

N is INTEGER N is the order of the Hessenberg matrix H upon which this subroutine operates.

### KTOP (in)

KTOP is INTEGER

### KBOT (in)

KBOT is INTEGER These are the first and last rows and columns of an isolated diagonal block upon which the QR sweep is to be applied. It is assumed without a check that either KTOP = 1 or H(KTOP,KTOP-1) = 0 and either KBOT = N or H(KBOT+1,KBOT) = 0.

### NSHFTS (in)

NSHFTS is INTEGER NSHFTS gives the number of simultaneous shifts. NSHFTS must be positive and even.

### SR (in,out)

SR is DOUBLE PRECISION array, dimension (NSHFTS)

### SI (in,out)

SI is DOUBLE PRECISION array, dimension (NSHFTS) SR contains the real parts and SI contains the imaginary parts of the NSHFTS shifts of origin that define the multi-shift QR sweep. On output SR and SI may be reordered.

### H (in,out)

H is DOUBLE PRECISION array, dimension (LDH,N) On input H contains a Hessenberg matrix. On output a multi-shift QR sweep with shifts SR(J)+i*SI(J) is applied to the isolated diagonal block in rows and columns KTOP through KBOT.

### LDH (in)

LDH is INTEGER LDH is the leading dimension of H just as declared in the calling procedure. LDH >= MAX(1,N).

### ILOZ (in)

ILOZ is INTEGER

### IHIZ (in)

IHIZ is INTEGER Specify the rows of Z to which transformations must be applied if WANTZ is .TRUE.. 1 <= ILOZ <= IHIZ <= N

### Z (in,out)

Z is DOUBLE PRECISION array, dimension (LDZ,IHIZ) If WANTZ = .TRUE., then the QR Sweep orthogonal similarity transformation is accumulated into Z(ILOZ:IHIZ,ILOZ:IHIZ) from the right. If WANTZ = .FALSE., then Z is unreferenced.

### LDZ (in)

LDZ is INTEGER LDA is the leading dimension of Z just as declared in the calling procedure. LDZ >= N.

### V (out)

V is DOUBLE PRECISION array, dimension (LDV,NSHFTS/2)

### LDV (in)

LDV is INTEGER LDV is the leading dimension of V as declared in the calling procedure. LDV >= 3.

### U (out)

U is DOUBLE PRECISION array, dimension (LDU,2*NSHFTS)

### LDU (in)

LDU is INTEGER LDU is the leading dimension of U just as declared in the in the calling subroutine. LDU >= 2*NSHFTS.

### NV (in)

NV is INTEGER NV is the number of rows in WV agailable for workspace. NV >= 1.

### WV (out)

WV is DOUBLE PRECISION array, dimension (LDWV,2*NSHFTS)

### LDWV (in)

LDWV is INTEGER LDWV is the leading dimension of WV as declared in the in the calling subroutine. LDWV >= NV.

### NH (in)

NH is INTEGER NH is the number of columns in array WH available for workspace. NH >= 1.

### WH (out)

WH is DOUBLE PRECISION array, dimension (LDWH,NH)

### LDWH (in)

LDWH is INTEGER Leading dimension of WH just as declared in the calling procedure. LDWH >= 2*NSHFTS.

