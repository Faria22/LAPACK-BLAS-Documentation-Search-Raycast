# DLARRB

## Function Signature

```fortran
DLARRB(N, D, LLD, IFIRST, ILAST, RTOL1,
*                          RTOL2, OFFSET, W, WGAP, WERR, WORK, IWORK,
*                          PIVMIN, SPDIAM, TWIST, INFO)
```

## Description


 Given the relatively robust representation(RRR) L D L^T, DLARRB
 does "limited" bisection to refine the eigenvalues of L D L^T,
 W( IFIRST-OFFSET ) through W( ILAST-OFFSET ), to more accuracy. Initial
 guesses for these eigenvalues are input in W, the corresponding estimate
 of the error in these guesses and their gaps are input in WERR
 and WGAP, respectively. During bisection, intervals
 [left, right] are maintained by storing their mid-points and
 semi-widths in the arrays W and WERR respectively.

## Parameters

### N (in)

N is INTEGER The order of the matrix.

### D (in)

D is DOUBLE PRECISION array, dimension (N) The N diagonal elements of the diagonal matrix D.

### LLD (in)

LLD is DOUBLE PRECISION array, dimension (N-1) The (N-1) elements L(i)*L(i)*D(i).

### IFIRST (in)

IFIRST is INTEGER The index of the first eigenvalue to be computed.

### ILAST (in)

ILAST is INTEGER The index of the last eigenvalue to be computed.

### RTOL1 (in)

RTOL1 is DOUBLE PRECISION

### RTOL2 (in)

RTOL2 is DOUBLE PRECISION Tolerance for the convergence of the bisection intervals. An interval [LEFT,RIGHT] has converged if RIGHT-LEFT < MAX( RTOL1*GAP, RTOL2*MAX(|LEFT|,|RIGHT|) ) where GAP is the (estimated) distance to the nearest eigenvalue.

### OFFSET (in)

OFFSET is INTEGER Offset for the arrays W, WGAP and WERR, i.e., the IFIRST-OFFSET through ILAST-OFFSET elements of these arrays are to be used.

### W (in,out)

W is DOUBLE PRECISION array, dimension (N) On input, W( IFIRST-OFFSET ) through W( ILAST-OFFSET ) are estimates of the eigenvalues of L D L^T indexed IFIRST through ILAST. On output, these estimates are refined.

### WGAP (in,out)

WGAP is DOUBLE PRECISION array, dimension (N-1) On input, the (estimated) gaps between consecutive eigenvalues of L D L^T, i.e., WGAP(I-OFFSET) is the gap between eigenvalues I and I+1. Note that if IFIRST = ILAST then WGAP(IFIRST-OFFSET) must be set to ZERO. On output, these gaps are refined.

### WERR (in,out)

WERR is DOUBLE PRECISION array, dimension (N) On input, WERR( IFIRST-OFFSET ) through WERR( ILAST-OFFSET ) are the errors in the estimates of the corresponding elements in W. On output, these errors are refined.

### WORK (out)

WORK is DOUBLE PRECISION array, dimension (2*N) Workspace.

### IWORK (out)

IWORK is INTEGER array, dimension (2*N) Workspace.

### PIVMIN (in)

PIVMIN is DOUBLE PRECISION The minimum pivot in the Sturm sequence.

### SPDIAM (in)

SPDIAM is DOUBLE PRECISION The spectral diameter of the matrix.

### TWIST (in)

TWIST is INTEGER The twist index for the twisted factorization that is used for the negcount. TWIST = N: Compute negcount from L D L^T - LAMBDA I = L+ D+ L+^T TWIST = 1: Compute negcount from L D L^T - LAMBDA I = U- D- U-^T TWIST = R: Compute negcount from L D L^T - LAMBDA I = N(r) D(r) N(r)

### INFO (out)

INFO is INTEGER Error flag.

