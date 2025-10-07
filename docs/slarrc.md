# SLARRC

## Function Signature

```fortran
SLARRC(JOBT, N, VL, VU, D, E, PIVMIN,
*                                   EIGCNT, LCNT, RCNT, INFO)
```

## Description


 Find the number of eigenvalues of the symmetric tridiagonal matrix T
 that are in the interval (VL,VU] if JOBT = 'T', and of L D L^T
 if JOBT = 'L'.

## Parameters

### JOBT (in)

JOBT is CHARACTER*1 = 'T': Compute Sturm count for matrix T. = 'L': Compute Sturm count for matrix L D L^T.

### N (in)

N is INTEGER The order of the matrix. N > 0.

### VL (in)

VL is REAL The lower bound for the eigenvalues.

### VU (in)

VU is REAL The upper bound for the eigenvalues.

### D (in)

D is REAL array, dimension (N) JOBT = 'T': The N diagonal elements of the tridiagonal matrix T. JOBT = 'L': The N diagonal elements of the diagonal matrix D.

### E (in)

E is REAL array, dimension (N) JOBT = 'T': The N-1 offdiagonal elements of the matrix T. JOBT = 'L': The N-1 offdiagonal elements of the matrix L.

### PIVMIN (in)

PIVMIN is REAL The minimum pivot in the Sturm sequence for T.

### EIGCNT (out)

EIGCNT is INTEGER The number of eigenvalues of the symmetric tridiagonal matrix T that are in the interval (VL,VU]

### LCNT (out)

LCNT is INTEGER

### RCNT (out)

RCNT is INTEGER The left and right negcounts of the interval.

### INFO (out)

INFO is INTEGER

