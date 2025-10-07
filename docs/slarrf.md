# SLARRF

## Function Signature

```fortran
SLARRF(N, D, L, LD, CLSTRT, CLEND,
*                          W, WGAP, WERR,
*                          SPDIAM, CLGAPL, CLGAPR, PIVMIN, SIGMA,
*                          DPLUS, LPLUS, WORK, INFO)
```

## Description


 Given the initial representation L D L^T and its cluster of close
 eigenvalues (in a relative measure), W( CLSTRT ), W( CLSTRT+1 ), ...
 W( CLEND ), SLARRF finds a new relatively robust representation
 L D L^T - SIGMA I = L(+) D(+) L(+)^T such that at least one of the
 eigenvalues of L(+) D(+) L(+)^T is relatively isolated.

## Parameters

### N (in)

N is INTEGER The order of the matrix (subblock, if the matrix split).

### D (in)

D is REAL array, dimension (N) The N diagonal elements of the diagonal matrix D.

### L (in)

L is REAL array, dimension (N-1) The (N-1) subdiagonal elements of the unit bidiagonal matrix L.

### LD (in)

LD is REAL array, dimension (N-1) The (N-1) elements L(i)*D(i).

### CLSTRT (in)

CLSTRT is INTEGER The index of the first eigenvalue in the cluster.

### CLEND (in)

CLEND is INTEGER The index of the last eigenvalue in the cluster.

### W (in)

W is REAL array, dimension dimension is >= (CLEND-CLSTRT+1) The eigenvalue APPROXIMATIONS of L D L^T in ascending order. W( CLSTRT ) through W( CLEND ) form the cluster of relatively close eigenalues.

### WGAP (in,out)

WGAP is REAL array, dimension dimension is >= (CLEND-CLSTRT+1) The separation from the right neighbor eigenvalue in W.

### WERR (in)

WERR is REAL array, dimension dimension is >= (CLEND-CLSTRT+1) WERR contain the semiwidth of the uncertainty interval of the corresponding eigenvalue APPROXIMATION in W

### SPDIAM (in)

SPDIAM is REAL estimate of the spectral diameter obtained from the Gerschgorin intervals

### CLGAPL (in)

CLGAPL is REAL

### CLGAPR (in)

CLGAPR is REAL absolute gap on each end of the cluster. Set by the calling routine to protect against shifts too close to eigenvalues outside the cluster.

### PIVMIN (in)

PIVMIN is REAL The minimum pivot allowed in the Sturm sequence.

### SIGMA (out)

SIGMA is REAL The shift used to form L(+) D(+) L(+)^T.

### DPLUS (out)

DPLUS is REAL array, dimension (N) The N diagonal elements of the diagonal matrix D(+).

### LPLUS (out)

LPLUS is REAL array, dimension (N-1) The first (N-1) elements of LPLUS contain the subdiagonal elements of the unit bidiagonal matrix L(+).

### WORK (out)

WORK is REAL array, dimension (2*N) Workspace.

### INFO (out)

INFO is INTEGER Signals processing OK (=0) or failure (=1)

