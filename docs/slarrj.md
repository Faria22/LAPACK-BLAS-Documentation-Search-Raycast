# SLARRJ

## Function Signature

```fortran
SLARRJ(N, D, E2, IFIRST, ILAST,
*                          RTOL, OFFSET, W, WERR, WORK, IWORK,
*                          PIVMIN, SPDIAM, INFO)
```

## Description


 Given the initial eigenvalue approximations of T, SLARRJ
 does  bisection to refine the eigenvalues of T,
 W( IFIRST-OFFSET ) through W( ILAST-OFFSET ), to more accuracy. Initial
 guesses for these eigenvalues are input in W, the corresponding estimate
 of the error in these guesses in WERR. During bisection, intervals
 [left, right] are maintained by storing their mid-points and
 semi-widths in the arrays W and WERR respectively.

## Parameters

### N (in)

N is INTEGER The order of the matrix.

### D (in)

D is REAL array, dimension (N) The N diagonal elements of T.

### E2 (in)

E2 is REAL array, dimension (N-1) The Squares of the (N-1) subdiagonal elements of T.

### IFIRST (in)

IFIRST is INTEGER The index of the first eigenvalue to be computed.

### ILAST (in)

ILAST is INTEGER The index of the last eigenvalue to be computed.

### RTOL (in)

RTOL is REAL Tolerance for the convergence of the bisection intervals. An interval [LEFT,RIGHT] has converged if RIGHT-LEFT < RTOL*MAX(|LEFT|,|RIGHT|).

### OFFSET (in)

OFFSET is INTEGER Offset for the arrays W and WERR, i.e., the IFIRST-OFFSET through ILAST-OFFSET elements of these arrays are to be used.

### W (in,out)

W is REAL array, dimension (N) On input, W( IFIRST-OFFSET ) through W( ILAST-OFFSET ) are estimates of the eigenvalues of L D L^T indexed IFIRST through ILAST. On output, these estimates are refined.

### WERR (in,out)

WERR is REAL array, dimension (N) On input, WERR( IFIRST-OFFSET ) through WERR( ILAST-OFFSET ) are the errors in the estimates of the corresponding elements in W. On output, these errors are refined.

### WORK (out)

WORK is REAL array, dimension (2*N) Workspace.

### IWORK (out)

IWORK is INTEGER array, dimension (2*N) Workspace.

### PIVMIN (in)

PIVMIN is REAL The minimum pivot in the Sturm sequence for T.

### SPDIAM (in)

SPDIAM is REAL The spectral diameter of T.

### INFO (out)

INFO is INTEGER Error flag.

