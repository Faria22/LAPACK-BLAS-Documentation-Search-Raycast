# DLARRD

## Function Signature

```fortran
DLARRD(RANGE, ORDER, N, VL, VU, IL, IU, GERS,
*                           RELTOL, D, E, E2, PIVMIN, NSPLIT, ISPLIT,
*                           M, W, WERR, WL, WU, IBLOCK, INDEXW,
*                           WORK, IWORK, INFO)
```

## Description


 DLARRD computes the eigenvalues of a symmetric tridiagonal
 matrix T to suitable accuracy. This is an auxiliary code to be
 called from DSTEMR.
 The user may ask for all eigenvalues, all eigenvalues
 in the half-open interval (VL, VU], or the IL-th through IU-th
 eigenvalues.

 To avoid overflow, the matrix must be scaled so that its
 largest element is no greater than overflow**(1/2) * underflow**(1/4) in absolute value, and for greatest
 accuracy, it should not be much smaller than that.

 See W. Kahan "Accurate Eigenvalues of a Symmetric Tridiagonal
 Matrix", Report CS41, Computer Science Dept., Stanford
 University, July 21, 1966.

## Parameters

### RANGE (in)

RANGE is CHARACTER*1 = 'A': ("All") all eigenvalues will be found. = 'V': ("Value") all eigenvalues in the half-open interval (VL, VU] will be found. = 'I': ("Index") the IL-th through IU-th eigenvalues (of the entire matrix) will be found.

### ORDER (in)

ORDER is CHARACTER*1 = 'B': ("By Block") the eigenvalues will be grouped by split-off block (see IBLOCK, ISPLIT) and ordered from smallest to largest within the block. = 'E': ("Entire matrix") the eigenvalues for the entire matrix will be ordered from smallest to largest.

### N (in)

N is INTEGER The order of the tridiagonal matrix T. N >= 0.

### VL (in)

VL is DOUBLE PRECISION If RANGE='V', the lower bound of the interval to be searched for eigenvalues. Eigenvalues less than or equal to VL, or greater than VU, will not be returned. VL < VU. Not referenced if RANGE = 'A' or 'I'.

### VU (in)

VU is DOUBLE PRECISION If RANGE='V', the upper bound of the interval to be searched for eigenvalues. Eigenvalues less than or equal to VL, or greater than VU, will not be returned. VL < VU. Not referenced if RANGE = 'A' or 'I'.

### IL (in)

IL is INTEGER If RANGE='I', the index of the smallest eigenvalue to be returned. 1 <= IL <= IU <= N, if N > 0; IL = 1 and IU = 0 if N = 0. Not referenced if RANGE = 'A' or 'V'.

### IU (in)

IU is INTEGER If RANGE='I', the index of the largest eigenvalue to be returned. 1 <= IL <= IU <= N, if N > 0; IL = 1 and IU = 0 if N = 0. Not referenced if RANGE = 'A' or 'V'.

### GERS (in)

GERS is DOUBLE PRECISION array, dimension (2*N) The N Gerschgorin intervals (the i-th Gerschgorin interval is (GERS(2*i-1), GERS(2*i)).

### RELTOL (in)

RELTOL is DOUBLE PRECISION The minimum relative width of an interval. When an interval is narrower than RELTOL times the larger (in magnitude) endpoint, then it is considered to be sufficiently small, i.e., converged. Note: this should always be at least radix*machine epsilon.

### D (in)

D is DOUBLE PRECISION array, dimension (N) The n diagonal elements of the tridiagonal matrix T.

### E (in)

E is DOUBLE PRECISION array, dimension (N-1) The (n-1) off-diagonal elements of the tridiagonal matrix T.

### E2 (in)

E2 is DOUBLE PRECISION array, dimension (N-1) The (n-1) squared off-diagonal elements of the tridiagonal matrix T.

### PIVMIN (in)

PIVMIN is DOUBLE PRECISION The minimum pivot allowed in the Sturm sequence for T.

### NSPLIT (in)

NSPLIT is INTEGER The number of diagonal blocks in the matrix T. 1 <= NSPLIT <= N.

### ISPLIT (in)

ISPLIT is INTEGER array, dimension (N) The splitting points, at which T breaks up into submatrices. The first submatrix consists of rows/columns 1 to ISPLIT(1), the second of rows/columns ISPLIT(1)+1 through ISPLIT(2), etc., and the NSPLIT-th consists of rows/columns ISPLIT(NSPLIT-1)+1 through ISPLIT(NSPLIT)=N. (Only the first NSPLIT elements will actually be used, but since the user cannot know a priori what value NSPLIT will have, N words must be reserved for ISPLIT.)

### M (out)

M is INTEGER The actual number of eigenvalues found. 0 <= M <= N. (See also the description of INFO=2,3.)

### W (out)

W is DOUBLE PRECISION array, dimension (N) On exit, the first M elements of W will contain the eigenvalue approximations. DLARRD computes an interval I_j = (a_j, b_j] that includes eigenvalue j. The eigenvalue approximation is given as the interval midpoint W(j)= ( a_j + b_j)/2. The corresponding error is bounded by WERR(j) = abs( a_j - b_j)/2

### WERR (out)

WERR is DOUBLE PRECISION array, dimension (N) The error bound on the corresponding eigenvalue approximation in W.

### WL (out)

WL is DOUBLE PRECISION

### WU (out)

WU is DOUBLE PRECISION The interval (WL, WU] contains all the wanted eigenvalues. If RANGE='V', then WL=VL and WU=VU. If RANGE='A', then WL and WU are the global Gerschgorin bounds on the spectrum. If RANGE='I', then WL and WU are computed by DLAEBZ from the index range specified.

### IBLOCK (out)

IBLOCK is INTEGER array, dimension (N) At each row/column j where E(j) is zero or small, the matrix T is considered to split into a block diagonal matrix. On exit, if INFO = 0, IBLOCK(i) specifies to which block (from 1 to the number of blocks) the eigenvalue W(i) belongs. (DLARRD may use the remaining N-M elements as workspace.)

### INDEXW (out)

INDEXW is INTEGER array, dimension (N) The indices of the eigenvalues within each block (submatrix); for example, INDEXW(i)= j and IBLOCK(i)=k imply that the i-th eigenvalue W(i) is the j-th eigenvalue in block k.

### WORK (out)

WORK is DOUBLE PRECISION array, dimension (4*N)

### IWORK (out)

IWORK is INTEGER array, dimension (3*N)

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value > 0: some or all of the eigenvalues failed to converge or were not computed: =1 or 3: Bisection failed to converge for some eigenvalues; these eigenvalues are flagged by a negative block number. The effect is that the eigenvalues may not be as accurate as the absolute and relative tolerances. This is generally caused by unexpectedly inaccurate arithmetic. =2 or 3: RANGE='I' only: Not all of the eigenvalues IL:IU were found. Effect: M < IU+1-IL Cause: non-monotonic arithmetic, causing the Sturm sequence to be non-monotonic. Cure: recalculate, using RANGE='A', and pick out eigenvalues IL:IU. In some cases, increasing the PARAMETER "FUDGE" may make things work. = 4: RANGE='I', and the Gershgorin interval initially used was too small. No eigenvalues were computed. Probable cause: your machine has sloppy floating-point arithmetic. Cure: Increase the PARAMETER "FUDGE", recompile, and try again.

