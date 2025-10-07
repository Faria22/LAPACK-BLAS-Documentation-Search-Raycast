# DLAQR2

## Function Signature

```fortran
DLAQR2(WANTT, WANTZ, N, KTOP, KBOT, NW, H, LDH, ILOZ,
*                          IHIZ, Z, LDZ, NS, ND, SR, SI, V, LDV, NH, T,
*                          LDT, NV, WV, LDWV, WORK, LWORK)
```

## Description


    DLAQR2 is identical to DLAQR3 except that it avoids
    recursion by calling DLAHQR instead of DLAQR4.

    Aggressive early deflation:

    This subroutine accepts as input an upper Hessenberg matrix
    H and performs an orthogonal similarity transformation
    designed to detect and deflate fully converged eigenvalues from
    a trailing principal submatrix.  On output H has been over-
    written by a new Hessenberg matrix that is a perturbation of
    an orthogonal similarity transformation of H.  It is to be
    hoped that the final version of H has many zero subdiagonal
    entries.

## Parameters

### WANTT (in)

WANTT is LOGICAL If .TRUE., then the Hessenberg matrix H is fully updated so that the quasi-triangular Schur factor may be computed (in cooperation with the calling subroutine). If .FALSE., then only enough of H is updated to preserve the eigenvalues.

### WANTZ (in)

WANTZ is LOGICAL If .TRUE., then the orthogonal matrix Z is updated so so that the orthogonal Schur factor may be computed (in cooperation with the calling subroutine). If .FALSE., then Z is not referenced.

### N (in)

N is INTEGER The order of the matrix H and (if WANTZ is .TRUE.) the order of the orthogonal matrix Z.

### KTOP (in)

KTOP is INTEGER It is assumed that either KTOP = 1 or H(KTOP,KTOP-1)=0. KBOT and KTOP together determine an isolated block along the diagonal of the Hessenberg matrix.

### KBOT (in)

KBOT is INTEGER It is assumed without a check that either KBOT = N or H(KBOT+1,KBOT)=0. KBOT and KTOP together determine an isolated block along the diagonal of the Hessenberg matrix.

### NW (in)

NW is INTEGER Deflation window size. 1 <= NW <= (KBOT-KTOP+1).

### H (in,out)

H is DOUBLE PRECISION array, dimension (LDH,N) On input the initial N-by-N section of H stores the Hessenberg matrix undergoing aggressive early deflation. On output H has been transformed by an orthogonal similarity transformation, perturbed, and the returned to Hessenberg form that (it is to be hoped) has some zero subdiagonal entries.

### LDH (in)

LDH is INTEGER Leading dimension of H just as declared in the calling subroutine. N <= LDH

### ILOZ (in)

ILOZ is INTEGER

### IHIZ (in)

IHIZ is INTEGER Specify the rows of Z to which transformations must be applied if WANTZ is .TRUE.. 1 <= ILOZ <= IHIZ <= N.

### Z (in,out)

Z is DOUBLE PRECISION array, dimension (LDZ,N) IF WANTZ is .TRUE., then on output, the orthogonal similarity transformation mentioned above has been accumulated into Z(ILOZ:IHIZ,ILOZ:IHIZ) from the right. If WANTZ is .FALSE., then Z is unreferenced.

### LDZ (in)

LDZ is INTEGER The leading dimension of Z just as declared in the calling subroutine. 1 <= LDZ.

### NS (out)

NS is INTEGER The number of unconverged (ie approximate) eigenvalues returned in SR and SI that may be used as shifts by the calling subroutine.

### ND (out)

ND is INTEGER The number of converged eigenvalues uncovered by this subroutine.

### SR (out)

SR is DOUBLE PRECISION array, dimension (KBOT)

### SI (out)

SI is DOUBLE PRECISION array, dimension (KBOT) On output, the real and imaginary parts of approximate eigenvalues that may be used for shifts are stored in SR(KBOT-ND-NS+1) through SR(KBOT-ND) and SI(KBOT-ND-NS+1) through SI(KBOT-ND), respectively. The real and imaginary parts of converged eigenvalues are stored in SR(KBOT-ND+1) through SR(KBOT) and SI(KBOT-ND+1) through SI(KBOT), respectively.

### V (out)

V is DOUBLE PRECISION array, dimension (LDV,NW) An NW-by-NW work array.

### LDV (in)

LDV is INTEGER The leading dimension of V just as declared in the calling subroutine. NW <= LDV

### NH (in)

NH is INTEGER The number of columns of T. NH >= NW.

### T (out)

T is DOUBLE PRECISION array, dimension (LDT,NW)

### LDT (in)

LDT is INTEGER The leading dimension of T just as declared in the calling subroutine. NW <= LDT

### NV (in)

NV is INTEGER The number of rows of work array WV available for workspace. NV >= NW.

### WV (out)

WV is DOUBLE PRECISION array, dimension (LDWV,NW)

### LDWV (in)

LDWV is INTEGER The leading dimension of W just as declared in the calling subroutine. NW <= LDV

### WORK (out)

WORK is DOUBLE PRECISION array, dimension (LWORK) On exit, WORK(1) is set to an estimate of the optimal value of LWORK for the given values of N, NW, KTOP and KBOT.

### LWORK (in)

LWORK is INTEGER The dimension of the work array WORK. LWORK = 2*NW suffices, but greater efficiency may result from larger values of LWORK. If LWORK = -1, then a workspace query is assumed; DLAQR2 only estimates the optimal workspace size for the given values of N, NW, KTOP and KBOT. The estimate is returned in WORK(1). No error message related to LWORK is issued by XERBLA. Neither H nor Z are accessed.

