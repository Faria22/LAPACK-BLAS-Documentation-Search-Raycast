# DLAEIN

## Function Signature

```fortran
DLAEIN(RIGHTV, NOINIT, N, H, LDH, WR, WI, VR, VI, B,
*                          LDB, WORK, EPS3, SMLNUM, BIGNUM, INFO)
```

## Description


 DLAEIN uses inverse iteration to find a right or left eigenvector
 corresponding to the eigenvalue (WR,WI) of a real upper Hessenberg
 matrix H.

## Parameters

### RIGHTV (in)

RIGHTV is LOGICAL = .TRUE. : compute right eigenvector; = .FALSE.: compute left eigenvector.

### NOINIT (in)

NOINIT is LOGICAL = .TRUE. : no initial vector supplied in (VR,VI). = .FALSE.: initial vector supplied in (VR,VI).

### N (in)

N is INTEGER The order of the matrix H. N >= 0.

### H (in)

H is DOUBLE PRECISION array, dimension (LDH,N) The upper Hessenberg matrix H.

### LDH (in)

LDH is INTEGER The leading dimension of the array H. LDH >= max(1,N).

### WR (in)

WR is DOUBLE PRECISION

### WI (in)

WI is DOUBLE PRECISION The real and imaginary parts of the eigenvalue of H whose corresponding right or left eigenvector is to be computed.

### VR (in,out)

VR is DOUBLE PRECISION array, dimension (N)

### VI (in,out)

VI is DOUBLE PRECISION array, dimension (N) On entry, if NOINIT = .FALSE. and WI = 0.0, VR must contain a real starting vector for inverse iteration using the real eigenvalue WR; if NOINIT = .FALSE. and WI.ne.0.0, VR and VI must contain the real and imaginary parts of a complex starting vector for inverse iteration using the complex eigenvalue (WR,WI); otherwise VR and VI need not be set. On exit, if WI = 0.0 (real eigenvalue), VR contains the computed real eigenvector; if WI.ne.0.0 (complex eigenvalue), VR and VI contain the real and imaginary parts of the computed complex eigenvector. The eigenvector is normalized so that the component of largest magnitude has magnitude 1; here the magnitude of a complex number (x,y) is taken to be |x| + |y|. VI is not referenced if WI = 0.0.

### B (out)

B is DOUBLE PRECISION array, dimension (LDB,N)

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= N+1.

### WORK (out)

WORK is DOUBLE PRECISION array, dimension (N)

### EPS3 (in)

EPS3 is DOUBLE PRECISION A small machine-dependent value which is used to perturb close eigenvalues, and to replace zero pivots.

### SMLNUM (in)

SMLNUM is DOUBLE PRECISION A machine-dependent value close to the underflow threshold.

### BIGNUM (in)

BIGNUM is DOUBLE PRECISION A machine-dependent value close to the overflow threshold.

### INFO (out)

INFO is INTEGER = 0: successful exit = 1: inverse iteration did not converge; VR is set to the last iterate, and so is VI if WI.ne.0.0.

