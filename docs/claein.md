# CLAEIN

## Function Signature

```fortran
CLAEIN(RIGHTV, NOINIT, N, H, LDH, W, V, B, LDB, RWORK,
*                          EPS3, SMLNUM, INFO)
```

## Description


 CLAEIN uses inverse iteration to find a right or left eigenvector
 corresponding to the eigenvalue W of a complex upper Hessenberg
 matrix H.

## Parameters

### RIGHTV (in)

RIGHTV is LOGICAL = .TRUE. : compute right eigenvector; = .FALSE.: compute left eigenvector.

### NOINIT (in)

NOINIT is LOGICAL = .TRUE. : no initial vector supplied in V = .FALSE.: initial vector supplied in V.

### N (in)

N is INTEGER The order of the matrix H. N >= 0.

### H (in)

H is COMPLEX array, dimension (LDH,N) The upper Hessenberg matrix H.

### LDH (in)

LDH is INTEGER The leading dimension of the array H. LDH >= max(1,N).

### W (in)

W is COMPLEX The eigenvalue of H whose corresponding right or left eigenvector is to be computed.

### V (in,out)

V is COMPLEX array, dimension (N) On entry, if NOINIT = .FALSE., V must contain a starting vector for inverse iteration; otherwise V need not be set. On exit, V contains the computed eigenvector, normalized so that the component of largest magnitude has magnitude 1; here the magnitude of a complex number (x,y) is taken to be |x| + |y|.

### B (out)

B is COMPLEX array, dimension (LDB,N)

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,N).

### RWORK (out)

RWORK is REAL array, dimension (N)

### EPS3 (in)

EPS3 is REAL A small machine-dependent value which is used to perturb close eigenvalues, and to replace zero pivots.

### SMLNUM (in)

SMLNUM is REAL A machine-dependent value close to the underflow threshold.

### INFO (out)

INFO is INTEGER = 0: successful exit = 1: inverse iteration did not converge; V is set to the last iterate.

