# DLARRE

## Function Signature

```fortran
DLARRE(RANGE, N, VL, VU, IL, IU, D, E, E2,
*                           RTOL1, RTOL2, SPLTOL, NSPLIT, ISPLIT, M,
*                           W, WERR, WGAP, IBLOCK, INDEXW, GERS, PIVMIN,
*                           WORK, IWORK, INFO)
```

## Description


 To find the desired eigenvalues of a given real symmetric
 tridiagonal matrix T, DLARRE sets any "small" off-diagonal
 elements to zero, and for each unreduced block T_i, it finds
 (a) a suitable shift at one end of the block's spectrum,
 (b) the base representation, T_i - sigma_i I = L_i D_i L_i^T, and
 (c) eigenvalues of each L_i D_i L_i^T.
 The representations and eigenvalues found are then used by
 DSTEMR to compute the eigenvectors of T.
 The accuracy varies depending on whether bisection is used to
 find a few eigenvalues or the dqds algorithm (subroutine DLASQ2) to
 compute all and then discard any unwanted one.
 As an added benefit, DLARRE also outputs the n
 Gerschgorin intervals for the matrices L_i D_i L_i^T.

## Parameters

### RANGE (in)

RANGE is CHARACTER*1 = 'A': ("All") all eigenvalues will be found. = 'V': ("Value") all eigenvalues in the half-open interval (VL, VU] will be found. = 'I': ("Index") the IL-th through IU-th eigenvalues (of the entire matrix) will be found.

### N (in)

N is INTEGER The order of the matrix. N > 0.

### VL (in,out)

VL is DOUBLE PRECISION If RANGE='V', the lower bound for the eigenvalues. Eigenvalues less than or equal to VL, or greater than VU, will not be returned. VL < VU. If RANGE='I' or ='A', DLARRE computes bounds on the desired part of the spectrum.

### VU (in,out)

VU is DOUBLE PRECISION If RANGE='V', the upper bound for the eigenvalues. Eigenvalues less than or equal to VL, or greater than VU, will not be returned. VL < VU. If RANGE='I' or ='A', DLARRE computes bounds on the desired part of the spectrum.

### IL (in)

IL is INTEGER If RANGE='I', the index of the smallest eigenvalue to be returned. 1 <= IL <= IU <= N.

### IU (in)

IU is INTEGER If RANGE='I', the index of the largest eigenvalue to be returned. 1 <= IL <= IU <= N.

### D (in,out)

D is DOUBLE PRECISION array, dimension (N) On entry, the N diagonal elements of the tridiagonal matrix T. On exit, the N diagonal elements of the diagonal matrices D_i.

### E (in,out)

E is DOUBLE PRECISION array, dimension (N) On entry, the first (N-1) entries contain the subdiagonal elements of the tridiagonal matrix T; E(N) need not be set. On exit, E contains the subdiagonal elements of the unit bidiagonal matrices L_i. The entries E( ISPLIT( I ) ), 1 <= I <= NSPLIT, contain the base points sigma_i on output.

### E2 (in,out)

E2 is DOUBLE PRECISION array, dimension (N) On entry, the first (N-1) entries contain the SQUARES of the subdiagonal elements of the tridiagonal matrix T; E2(N) need not be set. On exit, the entries E2( ISPLIT( I ) ), 1 <= I <= NSPLIT, have been set to zero

### RTOL1 (in)

RTOL1 is DOUBLE PRECISION

### RTOL2 (in)

RTOL2 is DOUBLE PRECISION Parameters for bisection. An interval [LEFT,RIGHT] has converged if RIGHT-LEFT < MAX( RTOL1*GAP, RTOL2*MAX(|LEFT|,|RIGHT|) )

### SPLTOL (in)

SPLTOL is DOUBLE PRECISION The threshold for splitting.

### NSPLIT (out)

NSPLIT is INTEGER The number of blocks T splits into. 1 <= NSPLIT <= N.

### ISPLIT (out)

ISPLIT is INTEGER array, dimension (N) The splitting points, at which T breaks up into blocks. The first block consists of rows/columns 1 to ISPLIT(1), the second of rows/columns ISPLIT(1)+1 through ISPLIT(2), etc., and the NSPLIT-th consists of rows/columns ISPLIT(NSPLIT-1)+1 through ISPLIT(NSPLIT)=N.

### M (out)

M is INTEGER The total number of eigenvalues (of all L_i D_i L_i^T) found.

### W (out)

W is DOUBLE PRECISION array, dimension (N) The first M elements contain the eigenvalues. The eigenvalues of each of the blocks, L_i D_i L_i^T, are sorted in ascending order ( DLARRE may use the remaining N-M elements as workspace).

### WERR (out)

WERR is DOUBLE PRECISION array, dimension (N) The error bound on the corresponding eigenvalue in W.

### WGAP (out)

WGAP is DOUBLE PRECISION array, dimension (N) The separation from the right neighbor eigenvalue in W. The gap is only with respect to the eigenvalues of the same block as each block has its own representation tree. Exception: at the right end of a block we store the left gap

### IBLOCK (out)

IBLOCK is INTEGER array, dimension (N) The indices of the blocks (submatrices) associated with the corresponding eigenvalues in W; IBLOCK(i)=1 if eigenvalue W(i) belongs to the first block from the top, =2 if W(i) belongs to the second block, etc.

### INDEXW (out)

INDEXW is INTEGER array, dimension (N) The indices of the eigenvalues within each block (submatrix); for example, INDEXW(i)= 10 and IBLOCK(i)=2 imply that the i-th eigenvalue W(i) is the 10-th eigenvalue in block 2

### GERS (out)

GERS is DOUBLE PRECISION array, dimension (2*N) The N Gerschgorin intervals (the i-th Gerschgorin interval is (GERS(2*i-1), GERS(2*i)).

### PIVMIN (out)

PIVMIN is DOUBLE PRECISION The minimum pivot in the Sturm sequence for T.

### WORK (out)

WORK is DOUBLE PRECISION array, dimension (6*N) Workspace.

### IWORK (out)

IWORK is INTEGER array, dimension (5*N) Workspace.

### INFO (out)

INFO is INTEGER = 0: successful exit > 0: A problem occurred in DLARRE. < 0: One of the called subroutines signaled an internal problem. Needs inspection of the corresponding parameter IINFO for further information. =-1: Problem in DLARRD. = 2: No base representation could be found in MAXTRY iterations. Increasing MAXTRY and recompilation might be a remedy. =-3: Problem in DLARRB when computing the refined root representation for DLASQ2. =-4: Problem in DLARRB when preforming bisection on the desired part of the spectrum. =-5: Problem in DLASQ2. =-6: Problem in DLASQ2.

