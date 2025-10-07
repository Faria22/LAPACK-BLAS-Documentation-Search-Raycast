# SLARRA

## Function Signature

```fortran
SLARRA(N, D, E, E2, SPLTOL, TNRM,
*                           NSPLIT, ISPLIT, INFO)
```

## Description


 Compute the splitting points with threshold SPLTOL.
 SLARRA sets any "small" off-diagonal elements to zero.

## Parameters

### N (in)

N is INTEGER The order of the matrix. N > 0.

### D (in)

D is REAL array, dimension (N) On entry, the N diagonal elements of the tridiagonal matrix T.

### E (in,out)

E is REAL array, dimension (N) On entry, the first (N-1) entries contain the subdiagonal elements of the tridiagonal matrix T; E(N) need not be set. On exit, the entries E( ISPLIT( I ) ), 1 <= I <= NSPLIT, are set to zero, the other entries of E are untouched.

### E2 (in,out)

E2 is REAL array, dimension (N) On entry, the first (N-1) entries contain the SQUARES of the subdiagonal elements of the tridiagonal matrix T; E2(N) need not be set. On exit, the entries E2( ISPLIT( I ) ), 1 <= I <= NSPLIT, have been set to zero

### SPLTOL (in)

SPLTOL is REAL The threshold for splitting. Two criteria can be used: SPLTOL<0 : criterion based on absolute off-diagonal value SPLTOL>0 : criterion that preserves relative accuracy

### TNRM (in)

TNRM is REAL The norm of the matrix.

### NSPLIT (out)

NSPLIT is INTEGER The number of blocks T splits into. 1 <= NSPLIT <= N.

### ISPLIT (out)

ISPLIT is INTEGER array, dimension (N) The splitting points, at which T breaks up into blocks. The first block consists of rows/columns 1 to ISPLIT(1), the second of rows/columns ISPLIT(1)+1 through ISPLIT(2), etc., and the NSPLIT-th consists of rows/columns ISPLIT(NSPLIT-1)+1 through ISPLIT(NSPLIT)=N.

### INFO (out)

INFO is INTEGER = 0: successful exit

